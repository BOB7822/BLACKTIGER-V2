#!/usr/bin/env python3
# MAC Address Changer Module

import os, sys, time, subprocess, random

def run():
    print("\n" + "="*60)
    print("MAC ADDRESS CHANGER")
    print("="*60)
    
    interface = input("Network interface [eth0]: ").strip() or "eth0"
    
    print(f"\nCurrent MAC for {interface}:")
    cmd = f"ifconfig {interface} | grep ether"
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    print(result.stdout)
    
    choice = input("\n[1] Random MAC [2] Custom MAC [3] Reset: ").strip()
    
    if choice == '1':
        mac = ':'.join(['{:02x}'.format(random.randint(0, 255)) for _ in range(6)])
        print(f"New MAC: {mac}")
    elif choice == '2':
        mac = input("Enter new MAC (e.g., 00:11:22:33:44:55): ").strip()
    elif choice == '3':
        mac = ""
        print("Resetting MAC...")
    else:
        return
    
    try:
        os.system(f"sudo ip link set {interface} down")
        if mac:
            os.system(f"sudo ip link set {interface} address {mac}")
        os.system(f"sudo ip link set {interface} up")
        print("MAC changed successfully!")
        cmd = f"ifconfig {interface} | grep ether"
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        print(result.stdout)
    except:
        print("Error changing MAC. Run with sudo")
        print("Alternative: sudo macchanger -r " + interface)

if __name__ == "__main__":
    run()