#!/usr/bin/env python3
# ARP Sniffer Module

import socket, struct, time

def run():
    print("\n" + "="*60)
    print("ARP SNIFFER")
    print("="*60)
    
    count = int(input("ARP packets to capture [10]: ").strip() or "10")
    
    print(f"\nCapturing {count} ARP packets...")
    print("Press Ctrl+C to stop")
    
    try:
        s = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3))
        captured = 0
        while captured < count:
            packet, addr = s.recvfrom(65536)
            if len(packet) >= 42:
                eth_header = packet[:14]
                eth = struct.unpack('!6s6sH', eth_header)
                eth_proto = socket.ntohs(eth[2])
                if eth_proto == 1544:  # ARP
                    captured += 1
                    arp_header = packet[14:42]
                    arp = struct.unpack('!HHBBH6s4s6s4s', arp_header)
                    sender_mac = ':'.join(f'{b:02x}' for b in arp[5])
                    sender_ip = socket.inet_ntoa(arp[6])
                    target_mac = ':'.join(f'{b:02x}' for b in arp[7])
                    target_ip = socket.inet_ntoa(arp[8])
                    print(f"\nARP Packet {captured}:")
                    print(f"  Operation: {arp[4]}")
                    print(f"  Sender MAC: {sender_mac}")
                    print(f"  Sender IP: {sender_ip}")
                    print(f"  Target MAC: {target_mac}")
                    print(f"  Target IP: {target_ip}")
            time.sleep(0.1)
        print("\nCapture complete!")
    except:
        print("Run with sudo for raw socket access")

if __name__ == "__main__":
    run()