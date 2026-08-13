#!/usr/bin/env python3
# Discord Server Info Module

import requests

def run():
    print("\n" + "="*60)
    print("DISCORD SERVER INFO")
    print("="*60)
    
    gid = input("Guild ID: ").strip()
    token = input("Token: ").strip()
    
    try:
        r = requests.get(f'https://discord.com/api/v9/guilds/{gid}', headers={'Authorization': token})
        if r.status_code == 200:
            data = r.json()
            print(f"Name: {data.get('name')}")
            print(f"Members: {data.get('approximate_member_count', 'Unknown')}")
        else:
            print("Error")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    run()