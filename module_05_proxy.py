#!/usr/bin/env python3
# Proxy Scraper Module

import requests, os

def run():
    print("\n" + "="*60)
    print("PROXY SCRAPER")
    print("="*60)
    
    working = []
    sources = [
        "https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all",
        "https://free-proxy-list.net/"
    ]
    
    for src in sources:
        try:
            print(f"Scraping {src}...")
            r = requests.get(src, timeout=10)
            for line in r.text.split('\n'):
                if ':' in line:
                    proxy = line.strip()
                    try:
                        test = requests.get('http://httpbin.org/ip', proxies={'http': proxy}, timeout=3)
                        if test.status_code == 200:
                            working.append(proxy)
                            print(f"Found: {proxy}")
                    except:
                        pass
        except:
            pass
    
    out_dir = os.path.expanduser("~/Downloads/BlackTiger_Output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "proxies.txt")
    with open(path, 'w') as f:
        f.write('\n'.join(working))
    
    print(f"Found {len(working)} proxies: {path}")

if __name__ == "__main__":
    run()