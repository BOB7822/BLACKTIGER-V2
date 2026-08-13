#!/usr/bin/env python3
# DOX Creator Module

import os, json, time, requests
from datetime import datetime

def run():
    print("\n" + "="*60)
    print("DOX CREATOR")
    print("="*60)
    
    target = input("Target name or email: ").strip()
    if not target:
        print("No target provided")
        return
    
    data = {"target": target, "timestamp": datetime.now().isoformat()}
    
    if '@' in target:
        username = target.split('@')[0]
        domain = target.split('@')[1]
        data['email'] = target
        data['username'] = username
        data['domain'] = domain
        print(f"Email: {target}")
        print(f"Username: {username}")
        print(f"Domain: {domain}")
    else:
        username = target
        data['username'] = username
        print(f"Username: {username}")
        for d in ['gmail.com', 'outlook.com', 'yahoo.com', 'protonmail.com']:
            print(f"Possible email: {username}@{d}")
    
    print("\nChecking social media...")
    platforms = {
        'GitHub': f'https://github.com/{username}',
        'Twitter': f'https://twitter.com/{username}',
        'Instagram': f'https://instagram.com/{username}',
        'Reddit': f'https://reddit.com/user/{username}',
        'YouTube': f'https://youtube.com/@{username}'
    }
    
    found = []
    for platform, url in platforms.items():
        try:
            r = requests.get(url, timeout=3)
            if r.status_code == 200:
                found.append(platform)
                print(f"[FOUND] {platform}: {url}")
        except:
            pass
    
    data['found_platforms'] = found
    
    out_dir = os.path.expanduser("~/Downloads/BlackTiger_Output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, f"dox_{username}.json")
    with open(path, 'w') as f:
        json.dump(data, f, indent=2)
    
    print(f"\nReport saved: {path}")

if __name__ == "__main__":
    run()