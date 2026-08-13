#!/usr/bin/env python3
# Bluetooth Sniffer Module

import os, sys, time, subprocess

def run():
    print("\n" + "="*60)
    print("BLUETOOTH SNIFFER")
    print("="*60)
    
    print("\nStarting Bluetooth scanning...")
    print("Press Ctrl+C to stop")
    
    try:
        cmd = "hcitool scan"
        print(f"Running: {cmd}")
        result = subprocess.run(cmd.split(), capture_output=True, text=True)
        print(result.stdout)
        
        cmd = "hcitool inq"
        result = subprocess.run(cmd.split(), capture_output=True, text=True)
        print(result.stdout)
        
        print("\nFor deeper sniffing, use tools like:")
        print("  - btmon")
        print("  - hcidump")
        print("  - Wireshark with bluetooth")
    except:
        print("No Bluetooth tools found")
        print("Install: bluez, bluez-utils")
        print("Run: sudo apt install bluez bluez-utils")

if __name__ == "__main__":
    run()