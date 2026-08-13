#!/usr/bin/env python3
# Censys Search Module

import requests

def run():
    print("\n" + "="*60)
    print("CENSYS SEARCH")
    print("="*60)
    
    query = input("Search query: ").strip()
    
    try:
        url = f"https://search.censys.io/api/v2/index?q={query}"
        r = requests.get(url, timeout=15)
        if r.status_code == 200:
            data = r.json()
            print(f"Found results (limited)")
            for host in data.get('result', {}).get('hits', [])[:5]:
                print(f"  {host.get('ip', 'Unknown')}")
        else:
            print(f"Error: {r.status_code}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    run()