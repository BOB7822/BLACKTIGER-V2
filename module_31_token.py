#!/usr/bin/env python3
# Discord Token Checker Module

import requests

def run():
    print("\n" + "="*60)
    print("DISCORD TOKEN CHECKER")
    print("="*60)
    
    token = input("Token: ").strip()
    
    try:
        r = requests.get('https://discord.com/api/v9/users/@me', headers={'Authorization': token})
        if r.status_code == 200:
            data = r.json()
            print(f"Username: {data.get('username')}#{data.get('discriminator')}")
            print(f"ID: {data.get('id')}")
            print(f"Email: {data.get('email')}")
        else:
            print("Invalid token")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    run()