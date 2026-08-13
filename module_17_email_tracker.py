#!/usr/bin/env python3
# Email Tracker Module

import re

def run():
    print("\n" + "="*60)
    print("EMAIL TRACKER")
    print("="*60)
    
    email = input("Email: ").strip()
    
    if re.match(r'[^@]+@[^@]+\.[^@]+', email):
        print("Valid email")
        print(f"Username: {email.split('@')[0]}")
        print(f"Domain: {email.split('@')[1]}")
    else:
        print("Invalid email")

if __name__ == "__main__":
    run()