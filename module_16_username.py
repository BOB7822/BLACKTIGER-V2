#!/usr/bin/env python3
# Username Tracker Module

import requests

def run():
    print("\n" + "="*60)
    print("USERNAME TRACKER")
    print("="*60)
    
    user = input("Username: ").strip()
    
    platforms = {
        'github': f'https://github.com/{user}',
        'twitter': f'https://twitter.com/{user}',
        'instagram': f'https://instagram.com/{user}',
        'reddit': f'https://reddit.com/user/{user}',
        'youtube': f'https://youtube.com/@{user}',
        'facebook': f'https://facebook.com/{user}'
    }
    
    found = []
    for name, url in platforms.items():
        try:
            r = requests.get(url, timeout=3)
            if r.status_code == 200:
                found.append(name)
                print(f"[FOUND] {name}")
        except:
            pass
    
    print(f"Found on {len(found)} platforms")

if __name__ == "__main__":
    run()