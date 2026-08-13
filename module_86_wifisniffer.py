#!/usr/bin/env python3
# WiFi Sniffer Module

import os, sys, time, subprocess

def run():
    print("\n" + "="*60)
    print("WIFI SNIFFER")
    print("="*60)
    
    interface = input("WiFi interface [wlan0mon]: ").strip() or "wlan0mon"
    count = int(input("Packets to capture [20]: ").strip() or "20")
    
    print(f"\nStarting WiFi sniffing on {interface}")
    print("Press Ctrl+C to stop")
    
    try:
        cmd = f"tcpdump -i {interface} -c {count} -e"
        print(f"Running: {cmd}")
        subprocess.run(cmd.split())
        print("\nCapture complete!")
    except:
        try:
            cmd = f"airodump-ng {interface} --output-format csv --write /tmp/wifi_scan"
            print(f"Running: {cmd}")
            proc = subprocess.Popen(cmd.split(), stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            time.sleep(10)
            proc.terminate()
            print("Scan complete!")
        except:
            print("No WiFi sniffing tools found")
            print("Install: tcpdump, aircrack-ng")
            print("Run: sudo apt install tcpdump aircrack-ng")

if __name__ == "__main__":
    run()