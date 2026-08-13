#!/usr/bin/env python3
# Shodan Search Module

import requests

def run():
    print("\n" + "="*60)
    print("SHODAN SEARCH")
    print("="*60)
    
    print("Using public Shodan search (limited results)")
    query = input("Search query (e.g., 'apache'): ").strip()
    
    try:
        url = f"https://api.shodan.io/shodan/host/search?query={query}"
        r = requests.get(url, timeout=15)
        if r.status_code == 200:
            data = r.json()
            print(f"Found {data.get('total', 0)} results (limited)")
            for host in data.get('matches', [])[:10]:
                ip = host.get('ip_str', 'Unknown')
                ports = host.get('ports', [])
                org = host.get('org', 'Unknown')
                print(f"  {ip}:{ports[:3]} - {org}")
        else:
            print(f"Error: {r.status_code}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    run()