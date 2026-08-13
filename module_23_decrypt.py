#!/usr/bin/env python3
# Password Decrypt Module

import hashlib

def run():
    print("\n" + "="*60)
    print("PASSWORD DECRYPT")
    print("="*60)
    
    h = input("Hash: ").strip()
    ht = input("Type (md5, sha1, sha256, sha512): ").strip().lower()
    
    wordlist = ['password', '123456', 'admin', 'letmein', 'qwerty', 'abc123']
    found = None
    
    for pw in wordlist:
        if ht == 'md5':
            comp = hashlib.md5(pw.encode()).hexdigest()
        elif ht == 'sha1':
            comp = hashlib.sha1(pw.encode()).hexdigest()
        elif ht == 'sha256':
            comp = hashlib.sha256(pw.encode()).hexdigest()
        elif ht == 'sha512':
            comp = hashlib.sha512(pw.encode()).hexdigest()
        else:
            print("Unsupported")
            return
        if comp == h:
            found = pw
            break
    
    if found:
        print(f"Password: {found}")
    else:
        print("Not found")

if __name__ == "__main__":
    run()