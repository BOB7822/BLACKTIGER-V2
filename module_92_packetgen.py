#!/usr/bin/env python3
# Packet Generator Module

import socket, random, time, struct

def run():
    print("\n" + "="*60)
    print("PACKET GENERATOR")
    print("="*60)
    
    target_ip = input("Target IP: ").strip()
    target_port = int(input("Target Port [80]: ").strip() or "80")
    packet_type = input("Packet type [TCP/UDP/ICMP]: ").strip().upper()
    count = int(input("Number of packets [10]: ").strip() or "10")
    
    print(f"\nGenerating {count} {packet_type} packets to {target_ip}:{target_port}")
    
    try:
        for i in range(count):
            if packet_type == "UDP":
                s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                data = random._urandom(random.randint(64, 1024))
                s.sendto(data, (target_ip, target_port))
                print(f"UDP packet {i+1}: {len(data)} bytes")
            elif packet_type == "TCP":
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(1)
                try:
                    s.connect((target_ip, target_port))
                    s.send(b"GET / HTTP/1.0\r\n\r\n")
                    print(f"TCP packet {i+1}: sent")
                except:
                    print(f"TCP packet {i+1}: failed")
                s.close()
            elif packet_type == "ICMP":
                s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
                packet = struct.pack('!BBHHH', 8, 0, 0, 0, 0) + random._urandom(56)
                checksum = 0
                packet = packet[:2] + struct.pack('!H', checksum) + packet[4:]
                s.sendto(packet, (target_ip, 0))
                print(f"ICMP packet {i+1}: sent")
            time.sleep(0.5)
    except:
        print("Run with sudo for raw socket access")

if __name__ == "__main__":
    run()