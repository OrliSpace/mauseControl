# client.py
import socket
import os
from dotenv import load_dotenv
from pynput import mouse

# Load IP and port from .env file
load_dotenv()
host = os.getenv("HOST")ד
port = int(os.getenv("PORT"))

# Callback when mouse moves
def on_move(x, y):
    try:
        msg = f"move {x} {y}\n"
        conn.sendall(msg.encode())
    except:
        return False  # Stop the listener if sending fails

# Connect to server and listen to mouse movements
with socket.create_connection((host, port)) as conn:
    print("[+] Connected to server, tracking mouse...")
    with mouse.Listener(on_move=on_move) as listener:
        listener.join()
