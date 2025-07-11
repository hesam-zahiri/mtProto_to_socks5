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
