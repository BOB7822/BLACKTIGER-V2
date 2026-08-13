#!/usr/bin/env python3
# Wayback Machine Module

import requests

def run():
    print("\n" + "="*60)
    print("WAYBACK MACHINE")
    print("="*60)
    
    url = input("URL (e.g., example.com): ").strip()
    
    if not url.startswith('http'):
        url = f"http://{url}"
    
    print(f"\nChecking archives for: {url}")
    
    try:
        r = requests.get(f"https://archive.org/wayback/available?url={url}", timeout=10)
        if r.status_code == 200:
            data = r.json()
            if data.get('archived_snapshots'):
                snapshots = data['archived_snapshots']
                if 'closest' in snapshots:
                    closest = snapshots['closest']
                    print(f"Closest snapshot: {closest.get('timestamp')}")
                    print(f"URL: {closest.get('url')}")
            else:
                print("No archives found")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    run()