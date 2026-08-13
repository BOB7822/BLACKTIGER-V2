#!/usr/bin/env python3
# Roblox User Info Module

import requests

def run():
    print("\n" + "="*60)
    print("ROBLOX USER INFO")
    print("="*60)
    
    user = input("Username: ").strip()
    
    try:
        r = requests.get(f'https://users.roblox.com/v1/users/search?keyword={user}')
        if r.status_code == 200:
            data = r.json()
            if data.get('data'):
                u = data['data'][0]
                print(f"ID: {u.get('id')}")
                print(f"Name: {u.get('name')}")
            else:
                print("Not found")
        else:
            print("Error")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    run()