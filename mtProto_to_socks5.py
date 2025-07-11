#!/usr/bin/env python3
import socket
import threading
import select
from socketserver import ThreadingMixIn, TCPServer, StreamRequestHandler
import struct

MT_PROXY_HOST = 'your_mtproto_proxy_ip'
MT_PROXY_PORT = 443
MT_PROXY_SECRET = 'your_mtproto_secret'
SOCKS5_HOST = '127.0.0.1'
SOCKS5_PORT = 1080

class MTProtoProxy:
    def __init__(self, host, port, secret):
        self.host = host
        self.port = port
        self.secret = secret.encode('utf-8')
        self.conn = None
        
    def connect(self):
        """Connect to MTProto server"""
        self.conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.conn.connect((self.host, self.port))
        self.conn.sendall(self.secret)
        
    def forward(self, data):
        """Send data to MTProto proxy and receive response"""
        self.conn.sendall(data)
        return self.conn.recv(4096)

class Socks5Handler(StreamRequestHandler):
    def handle(self):
        mt_proxy = MTProtoProxy(MT_PROXY_HOST, MT_PROXY_PORT, MT_PROXY_SECRET)
        mt_proxy.connect()
        version, nmethods = struct.unpack('!BB', self.connection.recv(2))
        methods = self.connection.recv(nmethods)
        self.connection.sendall(struct.pack('!BB', 0x05, 0x00))
        version, cmd, _, addr_type = struct.unpack('!BBBB', self.connection.recv(4))
        
        if addr_type == 0x01:  # IPv4
            addr = socket.inet_ntoa(self.connection.recv(4))
        elif addr_type == 0x03:  # Domain name
            domain_length = ord(self.connection.recv(1))
            addr = self.connection.recv(domain_length)
        else:
            self.connection.close()
            return
            
        port = struct.unpack('!H', self.connection.recv(2))[0]
        self.connection.sendall(struct.pack('!BBBBIH', 0x05, 0x00, 0x00, 0x01, 
                                       0x00000000, 0x0000))
        
        try:
            while True:
                r, _, _ = select.select([self.connection, mt_proxy.conn], [], [])
                
                if self.connection in r:
                    data = self.connection.recv(4096)
                    if not data:
                        break
                    response = mt_proxy.forward(data)
                    if not response:
                        break
                    self.connection.sendall(response)
                
                if mt_proxy.conn in r:
                    data = mt_proxy.conn.recv(4096)
                    if not data:
                        break
                    self.connection.sendall(data)
                    
        except Exception as e:
            print(f"Error: {e}")
        finally:
            self.connection.close()
            mt_proxy.conn.close()

class ThreadedTCPServer(ThreadingMixIn, TCPServer):
    allow_reuse_address = True

def main():
    print(f"🚀 SOCKS5 proxy running on {SOCKS5_HOST}:{SOCKS5_PORT}")
    print(f"🔗 Connected to MTProto proxy: {MT_PROXY_HOST}:{MT_PROXY_PORT}")
    
    server = ThreadedTCPServer((SOCKS5_HOST, SOCKS5_PORT), Socks5Handler)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n⏹️ Stopping server...")
        server.shutdown()

if __name__ == "__main__":
    main()
