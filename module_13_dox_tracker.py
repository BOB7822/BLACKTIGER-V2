#!/usr/bin/env python3
# DOX Tracker Module

import requests, json

def run():
    print("\n" + "="*60)
    print("DOX TRACKER")
    print("="*60)
    
    query = input("Email or username: ").strip()
    results = {}
    
    try:
        r = requests.get(f"https://haveibeenpwned.com/api/v3/breachedaccount/{query}", timeout=10)
        if r.status_code == 200:
            results['HIBP'] = r.json()
            print(f"Found {len(r.json())} breaches")
    except:
        pass
    
    for p in ['github', 'twitter', 'instagram', 'reddit']:
        try:
            r = requests.get(f"https://{p}.com/{query}", timeout=3)
            if r.status_code == 200:
                results[p] = "found"
                print(f"[FOUND] {p}")
        except:
            pass
    
    print(json.dumps(results, indent=2))

if __name__ == "__main__":
    run()