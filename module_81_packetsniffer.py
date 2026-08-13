#!/usr/bin/env python3
# Packet Sniffer Module

import socket, struct, time

def run():
    print("\n" + "="*60)
    print("PACKET SNIFFER")
    print("="*60)
    
    count = int(input("Packets to capture [20]: ").strip() or "20")
    
    print(f"\nCapturing {count} packets...")
    print("Press Ctrl+C to stop")
    
    try:
        s = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3))
        captured = 0
        while captured < count:
            packet, addr = s.recvfrom(65536)
            captured += 1
            print(f"\nPacket {captured}:")
            print(f"  Source: {addr}")
            print(f"  Length: {len(packet)} bytes")
            
            if len(packet) >= 14:
                eth_header = packet[:14]
                eth = struct.unpack('!6s6sH', eth_header)
                eth_proto = socket.ntohs(eth[2])
                print(f"  Protocol: {eth_proto}")
                if eth_proto == 8:
                    print("  Type: IP")
                elif eth_proto == 1544:
                    print("  Type: ARP")
            time.sleep(0.1)
        print("\nCapture complete!")
    except:
        print("Run with sudo for raw socket access")

if __name__ == "__main__":
    run()