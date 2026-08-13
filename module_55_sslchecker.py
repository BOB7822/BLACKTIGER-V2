#!/usr/bin/env python3
# SSL Certificate Checker Module

import ssl, socket, datetime

def run():
    print("\n" + "="*60)
    print("SSL CERTIFICATE CHECKER")
    print("="*60)
    
    domain = input("Domain: ").strip()
    
    try:
        ctx = ssl.create_default_context()
        with ctx.wrap_socket(socket.socket(), server_hostname=domain) as s:
            s.connect((domain, 443))
            cert = s.getpeercert()
            
        print(f"Certificate for: {domain}")
        print(f"Subject: {cert.get('subject', 'Unknown')}")
        print(f"Issuer: {cert.get('issuer', 'Unknown')}")
        print(f"Valid from: {cert.get('notBefore', 'Unknown')}")
        print(f"Valid until: {cert.get('notAfter', 'Unknown')}")
        print(f"Serial: {cert.get('serialNumber', 'Unknown')}")
        
        if 'notAfter' in cert:
            expiry = datetime.datetime.strptime(cert['notAfter'], '%b %d %H:%M:%S %Y %Z')
            now = datetime.datetime.now()
            days_left = (expiry - now).days
            if days_left < 0:
                print("EXPIRED!")
            else:
                print(f"Days left: {days_left}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    run()