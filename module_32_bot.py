#!/usr/bin/env python3
# Discord Bot Checker Module

import requests

def run():
    print("\n" + "="*60)
    print("DISCORD BOT CHECKER")
    print("="*60)
    
    token = input("Bot token: ").strip()
    
    try:
        r = requests.get('https://discord.com/api/v9/users/@me', headers={'Authorization': f'Bot {token}'})
        if r.status_code == 200:
            data = r.json()
            print(f"Name: {data.get('username')}")
            print(f"ID: {data.get('id')}")
        else:
            print("Invalid token")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    run()