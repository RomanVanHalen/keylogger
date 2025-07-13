# 🛡️ Stealth Keylogger – Cybersecurity Awareness Demo

This project simulates how attackers can use fake installers (like a Notepad setup) to deliver stealth keyloggers that capture and exfiltrate keystrokes to a remote attacker. It’s designed for **educational purposes only** to raise awareness about endpoint threats and red team tactics.

---

## ⚠️ Disclaimer

> This tool is provided **strictly for ethical, educational, and awareness purposes**. It was developed and tested in a **controlled lab environment** (e.g., VMs).  
>
> ❌ **Never deploy this code outside of a lab or on machines you do not own or have explicit permission to use.** Unauthorized use is illegal and unethical.  
>
> The author is not responsible for any misuse of this code.

---

## 🎯 Why This Demo Matters

Attackers often disguise malware as harmless applications. This lab demo helps:
- Understand how keystroke data can be silently harvested
- Explore red team tactics and defensive implications
- Raise awareness about software trust and endpoint security

---

## 🛠️ Setup Instructions

### 🔸 Requirements (Windows VM)

- Python 3.x
- `keyboard` module
- `pyinstaller` for packaging

### 🔹 Requirements (Kali VM / Attacker)

- Python 3.x


### 🔹 1. On the **Windows VM (Victim Simulation)**

#### ✅ Install requirements:
```bash
pip install keyboard pyinstaller
