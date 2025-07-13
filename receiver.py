import socket

HOST = '0.0.0.0'
PORT = 4444

print(f"[*] Listening on {HOST}:{PORT}...")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(5)

    while True:
        conn, addr = s.accept()
        with conn:
            print(f"[+] Connection from {addr}")
            try:
                data = conn.recv(1024)
                if data:
                    decoded = data.decode(errors='ignore').strip()
                    if decoded:
                        print(f"[+] Logged: {decoded}")
            except Exception as e:
                print(f"[!] Error: {e}")
