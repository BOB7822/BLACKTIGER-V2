#!/usr/bin/env python3
# Roblox ID Info Module

import requests

def run():
    print("\n" + "="*60)
    print("ROBLOX ID INFO")
    print("="*60)
    
    uid = input("User ID: ").strip()
    
    try:
        r = requests.get(f'https://users.roblox.com/v1/users/{uid}')
        if r.status_code == 200:
            data = r.json()
            print(f"ID: {data.get('id')}")
            print(f"Name: {data.get('name')}")
        else:
            print("Not found")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    run()