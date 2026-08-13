#!/usr/bin/env python3
# Email Reputation Checker Module

import requests

def run():
    print("\n" + "="*60)
    print("EMAIL REPUTATION CHECKER")
    print("="*60)
    
    email = input("Email: ").strip()
    
    if '@' not in email:
        print("Invalid email")
        return
    
    print(f"\nChecking reputation for: {email}")
    
    try:
        r = requests.get(f"https://emailrep.io/{email}", timeout=10)
        if r.status_code == 200:
            data = r.json()
            print(f"Email: {data.get('email')}")
            print(f"Reputation: {data.get('reputation', 'Unknown')}")
            print(f"Suspicious: {data.get('suspicious', False)}")
            
            if 'details' in data:
                details = data['details']
                print(f"First seen: {details.get('first_seen', 'Unknown')}")
                print(f"Last seen: {details.get('last_seen', 'Unknown')}")
                print(f"Domain: {details.get('domain', 'Unknown')}")
                print(f"Free provider: {details.get('is_free_provider', False)}")
                print(f"Disposable: {details.get('is_disposable', False)}")
            
            if 'breaches' in data:
                print(f"Breaches: {data['breaches']}")
        else:
            print("Could not get reputation (rate limited)")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    run()