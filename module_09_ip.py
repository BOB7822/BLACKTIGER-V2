#!/usr/bin/env python3
# IP Scanner Module

import subprocess, platform, ipaddress

def run():
    print("\n" + "="*60)
    print("IP SCANNER")
    print("="*60)
    
    net = input("CIDR (e.g., 192.168.1.0/24): ").strip()
    alive = []
    
    for ip in ipaddress.IPv4Network(net, strict=False):
        ip = str(ip)
        cmd = ['ping', '-c', '1', '-W', '1', ip] if platform.system() != "Windows" else ['ping', '-n', '1', '-w', '1000', ip]
        res = subprocess.run(cmd, capture_output=True)
        if res.returncode == 0:
            alive.append(ip)
            print(f"[ALIVE] {ip}")
    
    print(f"Found {len(alive)}")

if __name__ == "__main__":
    run()