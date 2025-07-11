# sender.py (UDP version with movement threshold and click support)
import socket
import os
from dotenv import load_dotenv
from pynput import mouse

# Load IP and port from .env file
load_dotenv()
host = os.getenv("HOST")
port = int(os.getenv("PORT"))

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Track last sent mouse position
last_x, last_y = None, None
threshold = 5  # Minimum pixel distance to trigger sending

# Callback when mouse moves
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
        sock.sendto(msg.encode(), (host, port))
    except Exception as e:
        print(f"[!] Error sending data: {e}")
        return False

# Callback when mouse is clicked
def on_click(x, y, button, pressed):
    if button == mouse.Button.left and pressed:
        try:
            sock.sendto(b"click\n", (host, port))
        except Exception as e:
            print(f"[!] Error sending click: {e}")

print(f"[+] Sending mouse events to {host}:{port}")

# Start mouse listener
with mouse.Listener(on_move=on_move, on_click=on_click) as listener:
    listener.join()
