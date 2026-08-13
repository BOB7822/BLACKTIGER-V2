#!/usr/bin/env python3
# Network Sniffer Module

import socket, struct, time

def run():
    print("\n" + "="*60)
    print("NETWORK SNIFFER")
    print("="*60)
    
    interface = input("Network interface [eth0]: ").strip() or "eth0"
    count = int(input("Packets to capture [50]: ").strip() or "50")
    
    print(f"\nStarting network sniffer on {interface}")
    print(f"Capturing {count} packets...")
    print("Press Ctrl+C to stop")
    
    try:
        import pcapy
        cap = pcapy.open_live(interface, 65536, 1, 0)
        count = 0
        while count < 50:
            (header, packet) = cap.next()
            if header is not None:
                count += 1
                eth_header = packet[:14]
                eth = struct.unpack('!6s6sH', eth_header)
                eth_proto = socket.ntohs(eth[2])
                if eth_proto == 8:
                    print(f"Packet {count}: IP packet")
                    try:
                        ip_header = packet[14:34]
                        iph = struct.unpack('!BBHHHBBH4s4s', ip_header)
                        src_ip = socket.inet_ntoa(iph[8])
                        dst_ip = socket.inet_ntoa(iph[9])
                        print(f"  Source: {src_ip} -> Destination: {dst_ip}")
                    except:
                        pass
        print("Capture complete!")
    except ImportError:
        print("pcapy not installed")
        print("Install: pip install pcapy")
        print("\nAlternative using python socket:")
        try:
            s = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3))
            for i in range(count):
                packet, addr = s.recvfrom(65536)
                print(f"Packet {i+1}: {len(packet)} bytes from {addr}")
        except:
            print("Run with sudo for raw socket access")
    except Exception as e:
        print(f"Error: {e}")
        print("Run with sudo for packet capture")

if __name__ == "__main__":
    run()