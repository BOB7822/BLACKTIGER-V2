#!/usr/bin/env python3
# Port Knocking Module

import socket, time, sys

def run():
    print("\n" + "="*60)
    print("PORT KNOCKING")
    print("="*60)
    
    target_ip = input("Target IP: ").strip()
    ports = input("Port sequence (comma separated, e.g., 7000,7001,7002): ").strip()
    ports = [int(p.strip()) for p in ports.split(',')]
    delay = float(input("Delay between knocks [0.5]: ").strip() or "0.5")
    
    print(f"\nKnocking on {target_ip}")
    print(f"Port sequence: {ports}")
    print(f"Delay: {delay}s")
    
    for port in ports:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(1)
            s.connect((target_ip, port))
            s.close()
            print(f"Knocked: {port}")
        except:
            print(f"Knocked: {port} (timeout)")
        time.sleep(delay)
    
    print("\nKnock sequence complete!")
    print("If configured, port should now be open")

if __name__ == "__main__":
    run()