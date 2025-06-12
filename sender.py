import socket
import os
from dotenv import load_dotenv

load_dotenv() #get the variables 
server_ip = os.getenv("SERVER_IP")
port = int(os.getenv("SERVER_PORT"))

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((server_ip, port))

message = "Hello, World!"
client_socket.send(message.encode())

client_socket.close()