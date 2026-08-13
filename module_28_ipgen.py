#!/usr/bin/env python3
# IP Generator Module

import random, ipaddress

def run():
    print("\n" + "="*60)
    print("IP GENERATOR")
    print("="*60)
    
    count = int(input("Number of IPs [20]: ").strip() or "20")
    cidr = input("CIDR range (e.g., 192.168.0.0/24) [random]: ").strip()
    
    print("\nGenerated IPs:")
    
    if cidr:
        try:
            network = ipaddress.IPv4Network(cidr, strict=False)
            for i, ip in enumerate(list(network.hosts())[:count]):
                print(f"  {ip}")
            return
        except:
            print("Invalid CIDR, generating random IPs")
    
    for _ in range(count):
        ip = f"{random.randint(1,255)}.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(0,255)}"
        print(f"  {ip}")

if __name__ == "__main__":
    run()