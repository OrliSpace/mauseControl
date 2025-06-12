# server.py
import socket
import pyautogui

HOST = '0.0.0.0'
PORT = 5001

# Create basic TCP server socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((HOST, PORT))
sock.listen(5)

print(f"[+] Server listening on {HOST}:{PORT}")

conn, addr = sock.accept()
print(f"[+] Connected by {addr}")

while True:
    data = conn.recv(1024).decode()
    if not data:
        break

    # Handle multiple lines if received in one packet
    for line in data.strip().split('\n'):
        parts = line.strip().split()
        if parts[0] == "move" and len(parts) == 3:
            try:
                x, y = int(parts[1]), int(parts[2])
                pyautogui.moveTo(x, y)
            except ValueError:
                print("[!] Invalid coordinates received.")
