# import socket

# # create socket
# server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# # The post of the ip
# host = '0.0.0.0'  
# port = 12345

import socket
import os
from dotenv import load_dotenv

load_dotenv()

host = os.getenv("SERVER_IP", "0.0.0.0")  # ברירת מחדל: מקבל מכל כתובת
port = int(os.getenv("SERVER_PORT", "12345"))

server_socket.bind((host, port))
server_socket.listen(1)
print(f"Reciever is listening on port {port}...")

conn, addr = server_socket.accept()
print(f"Connected by {addr}")

#get messege form the sender
data = conn.recv(1024).decode()
print("Received message:", data)

conn.close()