#!/usr/bin/env python3
# Advanced Port Scanner Module

import socket, threading, time

def run():
    print("\n" + "="*60)
    print("ADVANCED PORT SCANNER")
    print("="*60)
    
    ip = input("IP: ").strip()
    start_port = int(input("Start port [1]: ").strip() or "1")
    end_port = int(input("End port [1024]: ").strip() or "1024")
    threads = int(input("Threads [100]: ").strip() or "100")
    
    open_ports = []
    lock = threading.Lock()
    
    def scan_port(port):
        try:
            s = socket.socket()
            s.settimeout(0.5)
            if s.connect_ex((ip, port)) == 0:
                with lock:
                    open_ports.append(port)
                    print(f"[OPEN] {port}")
            s.close()
        except:
            pass
    
    print(f"\nScanning {ip} ports {start_port}-{end_port}...")
    start_time = time.time()
    
    for port in range(start_port, end_port + 1):
        scan_port(port)
    
    print(f"\nFound {len(open_ports)} open ports")
    print(f"Time: {time.time() - start_time:.2f}s")
    print(f"Open ports: {sorted(open_ports)}")

if __name__ == "__main__":
    run()