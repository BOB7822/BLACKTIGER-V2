#!/usr/bin/env python3
# USB Sniffer Module

import os, sys, time, subprocess

def run():
    print("\n" + "="*60)
    print("USB SNIFFER")
    print("="*60)
    
    print("\nStarting USB sniffing...")
    print("Press Ctrl+C to stop")
    
    try:
        cmd = "lsusb"
        result = subprocess.run(cmd.split(), capture_output=True, text=True)
        print("USB Devices:")
        print(result.stdout)
        
        print("\nUSB Events (dmesg):")
        cmd = "dmesg | grep -i usb | tail -10"
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        print(result.stdout)
        
        print("\nTo monitor USB traffic:")
        print("  - Use usbmon module")
        print("  - Run: sudo modprobe usbmon")
        print("  - Use Wireshark with USB capture")
        print("  - Use usbhid-dump for HID devices")
    except:
        print("Error reading USB devices")

if __name__ == "__main__":
    run()