#!/usr/bin/env python3
# Website Info Scanner Module

import requests

def run():
    print("\n" + "="*60)
    print("WEBSITE INFO SCANNER")
    print("="*60)
    
    url = input("URL: ").strip()
    
    try:
        r = requests.get(url, timeout=10)
        print(f"Status: {r.status_code}")
        print(f"Server: {r.headers.get('Server', 'Unknown')}")
        if '/wp-admin' in r.text:
            print("CMS: WordPress")
        elif '/administrator' in r.text:
            print("CMS: Joomla")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    run()