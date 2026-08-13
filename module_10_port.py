#!/usr/bin/env python3
# Port Scanner Module

import socket

def run():
    print("\n" + "="*60)
    print("PORT SCANNER")
    print("="*60)
    
    ip = input("IP: ").strip()
    ports = [21,22,23,25,80,443,445,3389,8080,8443]
    open_ports = []
    
    for p in ports:
        s = socket.socket()
        s.settimeout(0.5)
        if s.connect_ex((ip, p)) == 0:
            open_ports.append(p)
            print(f"[OPEN] {p}")
        s.close()
    
    print(f"Found {len(open_ports)}")

if __name__ == "__main__":
    run()