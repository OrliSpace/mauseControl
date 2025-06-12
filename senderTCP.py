# client.py (TCP version)
import socket
import os
from dotenv import load_dotenv
from pynput import mouse

# Load IP and port from .env file
load_dotenv()
host = os.getenv("HOST")
port = int(os.getenv("PORT"))

# Create TCP connection
sock = socket.create_connection((host, port))

# Track last sent mouse position
last_x, last_y = None, None
threshold = 5  # Only send if moved more than this

def on_move(x, y):
    global last_x, last_y

    if last_x is not None and last_y is not None:
        dx = abs(x - last_x)
        dy = abs(y - last_y)
        if dx < threshold and dy < threshold:
            return

    last_x, last_y = x, y

    try:
        msg = f"move {x} {y}\n"
        sock.sendall(msg.encode())
    except Exception as e:
        print(f"[!] Failed to send move: {e}")
        return False

def on_click(x, y, button, pressed):
    if button == mouse.Button.left and pressed:
        try:
            sock.sendall(b"click\n")
        except Exception as e:
            print(f"[!] Failed to send click: {e}")

print(f"[+] Connected to {host}:{port} – sending mouse events...")

with mouse.Listener(on_move=on_move, on_click=on_click) as listener:
    listener.join()

sock.close()
