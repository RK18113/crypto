import ssl
import socket

HOST = 'localhost'
PORT = 8000

# 1. Create a Secure Context [cite: 195-196]
context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain(certfile='cert.pem', keyfile='key.pem')

# 2. Create a standard (raw) TCP socket [cite: 198-200]
raw_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
raw_socket.bind((HOST, PORT))
raw_socket.listen(1)
print(f"SSL Server running on {PORT}...")

# 3. Wrap the socket with SSL [cite: 202-203]
with context.wrap_socket(raw_socket, server_side=True) as ssl_server:
    conn, addr = ssl_server.accept()
    print(f"Secure connection from: {addr}")

    # Send and Receive [cite: 205-206]
    conn.send(b"Hello! This message is encrypted.")
    data = conn.recv(1024).decode()
    print(f"Client sent: {data}")

    conn.close()