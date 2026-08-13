#!/usr/bin/env python3
# Roblox Cookie Info Module

import base64

def run():
    print("\n" + "="*60)
    print("ROBLOX COOKIE INFO")
    print("="*60)
    
    cookie = input(".ROBLOSECURITY: ").strip()
    parts = cookie.split('.')
    
    if len(parts) > 1:
        try:
            payload = base64.b64decode(parts[1] + '==')
            print(f"User ID: {payload[:8]}")
        except:
            print("Could not decode")

if __name__ == "__main__":
    run()