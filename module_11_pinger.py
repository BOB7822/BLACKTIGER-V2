#!/usr/bin/env python3
# IP Pinger Module

import subprocess, platform, socket

def run():
    print("\n" + "="*60)
    print("IP PINGER")
    print("="*60)
    
    target = input("IP or domain: ").strip()
    
    try:
        ip = socket.gethostbyname(target)
        print(f"Resolved: {ip}")
    except:
        ip = target
    
    cmd = ['ping', '-c', '4', ip] if platform.system() != "Windows" else ['ping', '-n', '4', ip]
    res = subprocess.run(cmd, capture_output=True, text=True)
    print(res.stdout)

if __name__ == "__main__":
    run()