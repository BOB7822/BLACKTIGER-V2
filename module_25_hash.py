#!/usr/bin/env python3
# Hash Generator Module

import hashlib, base64

def run():
    print("\n" + "="*60)
    print("HASH GENERATOR")
    print("="*60)
    
    text = input("Enter text to hash: ").strip()
    
    print(f"\nMD5: {hashlib.md5(text.encode()).hexdigest()}")
    print(f"SHA1: {hashlib.sha1(text.encode()).hexdigest()}")
    print(f"SHA256: {hashlib.sha256(text.encode()).hexdigest()}")
    print(f"SHA512: {hashlib.sha512(text.encode()).hexdigest()}")
    print(f"Base64: {base64.b64encode(text.encode()).decode()}")

if __name__ == "__main__":
    run()