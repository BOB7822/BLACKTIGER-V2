#!/usr/bin/env python3
# Subdomain Scanner Module

import socket

def run():
    print("\n" + "="*60)
    print("SUBDOMAIN SCANNER")
    print("="*60)
    
    domain = input("Domain: ").strip()
    
    subdomains = ['www', 'mail', 'ftp', 'admin', 'dev', 'test', 'api', 'blog', 'shop', 'forum',
                  'support', 'help', 'docs', 'wiki', 'media', 'static', 'cdn', 'images', 'video',
                  'download', 'upload', 'login', 'signup', 'register', 'auth', 'secure', 'ssl']
    
    found = []
    for sub in subdomains:
        try:
            ip = socket.gethostbyname(f"{sub}.{domain}")
            found.append(f"{sub}.{domain} -> {ip}")
            print(f"[FOUND] {sub}.{domain}")
        except:
            pass
    
    print(f"\nFound {len(found)} subdomains")

if __name__ == "__main__":
    run()