# server.py (UDP version)
import socket
import pyautogui

# Disable PyAutoGUI fail-safe (use with caution)
pyautogui.FAILSAFE = False

# Get screen dimensions
screen_width, screen_height = pyautogui.size()
edge_margin = 2  # Number of pixels to avoid at the edges

HOST = '0.0.0.0'
PORT = 12345

# Create and bind UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((HOST, PORT))

print(f"[+] UDP Server listening on {HOST}:{PORT}")

while True:
    data, addr = sock.recvfrom(1024)
    message = data.decode().strip()
    
    # Handle multiple lines if received together
    for line in message.split('\n'):
        parts = line.strip().split()

        if not parts:
            continue

        if parts[0] == "move" and len(parts) == 3:
            try:
                x, y = int(parts[1]), int(parts[2])

                # Ignore positions too close to the screen edges
                if (x <= edge_margin or x >= screen_width - edge_margin or
                    y <= edge_margin or y >= screen_height - edge_margin):
                    continue

                pyautogui.moveTo(x, y)
            except ValueError:
                print("[!] Invalid coordinates received.")

        elif parts[0] == "click":
            pyautogui.click()
