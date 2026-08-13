#!/usr/bin/env python3
# DNS Sniffer Module

import socket, struct, time

def run():
    print("\n" + "="*60)
    print("DNS SNIFFER")
    print("="*60)
    
    count = int(input("DNS packets to capture [10]: ").strip() or "10")
    
    print(f"\nCapturing {count} DNS packets...")
    print("Press Ctrl+C to stop")
    
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_UDP)
        s.bind(('0.0.0.0', 53))
        captured = 0
        while captured < count:
            data, addr = s.recvfrom(1024)
            captured += 1
            print(f"\nDNS Packet {captured}:")
            print(f"  From: {addr}")
            print(f"  Size: {len(data)} bytes")
            if len(data) > 12:
                dns_header = data[:12]
                dns = struct.unpack('!HHHHHH', dns_header)
                print(f"  ID: {dns[0]}")
                print(f"  Questions: {dns[1]}")
                print(f"  Answers: {dns[2]}")
                print(f"  Authority: {dns[3]}")
                print(f"  Additional: {dns[4]}")
            time.sleep(0.1)
        print("\nCapture complete!")
    except:
        print("Run with sudo for raw socket access")

if __name__ == "__main__":
    run()