#!/usr/bin/env python3
# Email Lookup Module

import socket

def run():
    print("\n" + "="*60)
    print("EMAIL LOOKUP")
    print("="*60)
    
    email = input("Email: ").strip()
    domain = email.split('@')[1] if '@' in email else email
    
    try:
        mx_records = socket.getaddrinfo(domain, 25, socket.AF_INET, socket.SOCK_STREAM)
        print(f"MX records for {domain}:")
        for record in mx_records[:5]:
            print(f"  {record[4][0]}")
    except:
        print(f"No MX records found for {domain}")

if __name__ == "__main__":
    run()