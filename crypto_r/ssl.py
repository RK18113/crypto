import ssl
import socket

HOST = 'localhost'
PORT = 8000

context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain(certfile='cert.pem', keyfile='key.pem')

raw_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
raw_socket.bind((HOST, PORT))
raw_socket.listen(1)
print(f"SSL Server running on {PORT}...")

with context.wrap_socket(raw_socket, server_side=True) as ssl_server:
    conn, addr = ssl_server.accept()
    print(f"Secure connection from: {addr}")

    conn.send(b"Hello! This message is encrypted.")
    data = conn.recv(1024).decode()
    print(f"Client sent: {data}")

    conn.close()




import ssl
import socket

HOST = 'localhost'
PORT = 8000

context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
context.check_hostname = False
context.verify_mode = ssl.CERT_NONE

raw_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
with context.wrap_socket(raw_socket, server_hostname=HOST) as ssl_client:
    ssl_client.connect((HOST, PORT)) 
    print("Connected securely to server.")

    ssl_client.send(b"Client says: Security established!")
    message = ssl_client.recv(1024).decode()
    print(f"Server response: {message}")


