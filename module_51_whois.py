#!/usr/bin/env python3
# WHOIS Lookup Module

import subprocess, socket

def run():
    print("\n" + "="*60)
    print("WHOIS LOOKUP")
    print("="*60)
    
    domain = input("Domain: ").strip()
    
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(("whois.verisign-grs.com", 43))
        s.send(f"{domain}\r\n".encode())
        response = s.recv(4096).decode()
        s.close()
        print(response[:2000])
        if len(response) > 2000:
            print("\n... (truncated)")
    except:
        try:
            result = subprocess.run(['whois', domain], capture_output=True, text=True)
            print(result.stdout[:2000])
        except:
            print("WHOIS lookup failed")

if __name__ == "__main__":
    run()