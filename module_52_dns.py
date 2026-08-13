#!/usr/bin/env python3
# DNS Lookup Module

import socket

def run():
    print("\n" + "="*60)
    print("DNS LOOKUP")
    print("="*60)
    
    domain = input("Domain: ").strip()
    
    try:
        print(f"A records for {domain}:")
        for ip in socket.gethostbyname_ex(domain)[2]:
            print(f"  {ip}")
    except:
        try:
            print(f"IP: {socket.gethostbyname(domain)}")
        except:
            print("DNS lookup failed")

if __name__ == "__main__":
    run()