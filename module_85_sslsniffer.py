#!/usr/bin/env python3
# SSL Sniffer Module

import socket, ssl, struct, time

def run():
    print("\n" + "="*60)
    print("SSL SNIFFER")
    print("="*60)
    
    target = input("Target IP or domain: ").strip()
    port = int(input("Port [443]: ").strip() or "443")
    
    print(f"\nAttempting SSL connection to {target}:{port}")
    
    try:
        ctx = ssl.create_default_context()
        with ctx.wrap_socket(socket.socket(), server_hostname=target) as s:
            s.connect((target, port))
            cert = s.getpeercert()
            print(f"SSL connection established!")
            print(f"Certificate subject: {cert.get('subject', 'Unknown')}")
            print(f"Issuer: {cert.get('issuer', 'Unknown')}")
            print(f"Valid until: {cert.get('notAfter', 'Unknown')}")
            print(f"SSL Version: {s.version()}")
            print(f"Cipher: {s.cipher()}")
            
            print("\nTo sniff SSL traffic, use mitmproxy or burpsuite")
            print("Install: pip install mitmproxy")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    run()