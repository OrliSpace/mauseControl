import socket
import os
from dotenv import load_dotenv  # For loading environment variables from .env file


# Load environment variables from .env file (HOST and PORT)
load_dotenv()
host = os.getenv("HOST")               # Server IP from .env
port = int(os.getenv("PORT"))          # Server port from .env

def on_move(x, y):# client.py
import socket
import os
from dotenv import load_dotenv
from pynput import mouse

# Load IP and port from .env file
load_dotenv()
host = os.getenv("HOST")
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
    """
    Callback for mouse movement.
    Sends the current mouse coordinates to the server.
    """
    try:
        msg = f"move {x} {y}\n"        # Format the message
        conn.sendall(msg.encode())     # Send encoded message over secure connection
    except:
        return False                   # Stop the listener on failure

# Establish a secure socket connection to the server
with socket.create_connection((host, port)) as sock:
    with context.wrap_socket(sock, server_hostname=host) as conn:
        print("[+] Connected to server, tracking mouse...")

        # Start listening for mouse movement and trigger on_move callback
        from pynput import mouse
        with mouse.Listener(on_move=on_move) as listener:
            listener.join()           # Keep the listener running
