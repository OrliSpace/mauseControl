
import socket
import os
from dotenv import load_dotenv

host = '0.0.0.0'  # מאפשר להתחבר מכל כתובת
port = 12345

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind((host, port))
server_socket.listen(1)
real_ip = socket.gethostbyname(socket.gethostname())
print(f"Receiver IP (on local network): {real_ip}")
print(f"Reciever is listening on port {port}...")


conn, addr = server_socket.accept()
print(f"Connected by {addr}")

#get messege form the sender
data = conn.recv(1024).decode()
print("Received message:", data)

conn.close()