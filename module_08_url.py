#!/usr/bin/env python3
# URL Scanner Module

import socket

def run():
    print("\n" + "="*60)
    print("URL SCANNER")
    print("="*60)
    
    domain = input("Domain: ").strip()
    subs = ['www','mail','ftp','admin','dev','test','api','blog','shop','forum']
    found = []
    
    for s in subs:
        try:
            ip = socket.gethostbyname(f"{s}.{domain}")
            found.append(f"{s}.{domain} -> {ip}")
            print(f"[FOUND] {s}.{domain}")
        except:
            pass
    
    print(f"Found {len(found)}")

if __name__ == "__main__":
    run()