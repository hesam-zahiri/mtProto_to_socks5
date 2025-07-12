# mtProto_to_socks5
Convert mtproto proxy to socks5

# MTProto to SOCKS5 Conversion Script

Here is a complete Python script that converts an MTProto proxy to SOCKS5:

## Usage Guide

1. **Prerequisites Installation**:
   ```bash
   pip install pysocks
   ```

2. **Configuration**:
   - `MT_PROXY_HOST`: MTProto server address
   - `MT_PROXY_PORT`: Proxy port
   - `MT_PROXY_SECRET`: MTProto proxy secret key
   - `SOCKS5_HOST` and `SOCKS5_PORT`: Local address and port for SOCKS5

3. **Running the Script**:
   ```bash
   python3 mtproto_to_socks5.py
   ```

4. **Using the Proxy**:
   - Use `127.0.0.1:1080` as your SOCKS5 proxy in applications.

## Script Features

- Support for concurrent connections using threading
- Full SOCKS5 protocol implementation
- Error handling and proper connection closing
- Capability to run as a permanent service

## Important Notes

1. This script should be run on an intermediary server that has access to both the internet and the MTProto proxy.
2. For enhanced security, you can change SOCKS5_HOST to `0.0.0.0` to make it accessible from the local network.
3. If SOCKS5 authentication is required, you'll need to add the relevant code.

### 🔴 Attention

- 1. Limitations:
The MTProto protocol is specifically designed for Telegram communications. Therefore, if software such as web browsers or other general-purpose network applications connect to this SOCKS5 proxy, they will not be able to establish a successful connection. This is because only Telegram-related traffic is recognized and handled by MTProto. Unlike protocols such as Shadowsocks or VPNs, which can tunnel all system network traffic, this solution is limited solely to Telegram traffic.
- 2. Practical Use:
This script essentially serves as an intermediary between a Telegram client and an MTProto proxy. It allows clients such as Telegram Desktop to connect to a local SOCKS5 proxy, which in turn forwards the Telegram traffic through an MTProto proxy. This method is particularly useful for enabling access to Telegram in networks where direct connections may be restricted.
