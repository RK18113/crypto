import ssl
import socket

HOST = 'localhost'
PORT = 8000

# 1. Create Client Context [cite: 217]
context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
# Since our cert is self-signed, we skip official verification [cite: 218-219]
context.check_hostname = False
context.verify_mode = ssl.CERT_NONE

# 2. Create raw socket and wrap it [cite: 220-221]
raw_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
with context.wrap_socket(raw_socket, server_hostname=HOST) as ssl_client:
    ssl_client.connect((HOST, PORT)) # [cite: 222]
    print("Connected securely to server.")

    # Exchange data [cite: 224-225]
    ssl_client.send(b"Client says: Security established!")
    message = ssl_client.recv(1024).decode()
    print(f"Server response: {message}")