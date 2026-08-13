#!/usr/bin/env python3
# Roblox Cookie Login Module

import requests

def run():
    print("\n" + "="*60)
    print("ROBLOX COOKIE LOGIN")
    print("="*60)
    
    cookie = input(".ROBLOSECURITY: ").strip()
    
    try:
        r = requests.get('https://www.roblox.com/mobileapi/userinfo', 
                        headers={'Cookie': f'.ROBLOSECURITY={cookie}'})
        if r.status_code == 200:
            data = r.json()
            print(f"UserID: {data.get('UserID')}")
            print(f"UserName: {data.get('UserName')}")
            print(f"Robux: {data.get('RobuxBalance')}")
        else:
            print("Invalid cookie")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    run()