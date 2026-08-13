#!/usr/bin/env python3
# HTTP Sniffer Module

import socket, struct, time, re

def run():
    print("\n" + "="*60)
    print("HTTP SNIFFER")
    print("="*60)
    
    count = int(input("HTTP packets to capture [10]: ").strip() or "10")
    port = int(input("Port [80]: ").strip() or "80")
    
    print(f"\nCapturing {count} HTTP packets on port {port}...")
    print("Press Ctrl+C to stop")
    
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)
        s.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
        captured = 0
        while captured < count:
            packet, addr = s.recvfrom(65536)
            if len(packet) > 40:
                ip_header = packet[0:20]
                iph = struct.unpack('!BBHHHBBH4s4s', ip_header)
                proto = iph[6]
                if proto == 6:
                    tcp_header = packet[20:40]
                    tcph = struct.unpack('!HHLLBBHHH', tcp_header)
                    src_port = tcph[0]
                    dst_port = tcph[1]
                    if src_port == port or dst_port == port:
                        captured += 1
                        data = packet[40:]
                        try:
                            decoded = data.decode('utf-8', errors='ignore')
                            lines = decoded.split('\n')[:5]
                            print(f"\nHTTP Packet {captured}:")
                            for line in lines:
                                if line.strip():
                                    print(f"  {line[:100]}")
                            if 'password' in decoded.lower() or 'passwd' in decoded.lower():
                                print("  [ALERT] Possible password in traffic!")
                        except:
                            print(f"HTTP Packet {captured}: {len(data)} bytes")
            time.sleep(0.1)
        print("\nCapture complete!")
    except:
        print("Run with sudo for raw socket access")

if __name__ == "__main__":
    run()