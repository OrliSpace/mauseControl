# server.py (TCP version)
import socket
import pyautogui

# Disable PyAutoGUI fail-safe (use with caution)
pyautogui.FAILSAFE = False

# Get screen dimensions
screen_width, screen_height = pyautogui.size()
edge_margin = 2  # Number of pixels to avoid at the edges

HOST = '0.0.0.0'
PORT = 12345

# Create and bind TCP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((HOST, PORT))
sock.listen(1)

print(f"[+] TCP Server listening on {HOST}:{PORT}")
conn, addr = sock.accept()
print(f"[+] Connected by {addr}")

buffer = ""

while True:
    try:
        data = conn.recv(1024)
        if not data:
            break

        buffer += data.decode()
        while '\n' in buffer:
            line, buffer = buffer.split('\n', 1)
            parts = line.strip().split()

            if not parts:
                continue

            if parts[0] == "move" and len(parts) == 3:
                try:
                    x, y = int(parts[1]), int(parts[2])
                    if (x <= edge_margin or x >= screen_width - edge_margin or
                        y <= edge_margin or y >= screen_height - edge_margin):
                        continue
                    pyautogui.moveTo(x, y)
                except ValueError:
                    print("[!] Invalid coordinates.")

            elif parts[0] == "click":
                pyautogui.click()

    except Exception as e:
        print(f"[!] Error: {e}")
        break

conn.close()
