#!/usr/bin/env python3
# Password Encrypt Module

from cryptography.fernet import Fernet
import os

def run():
    print("\n" + "="*60)
    print("PASSWORD ENCRYPT")
    print("="*60)
    
    pw = input("Password: ").strip()
    
    try:
        key = Fernet.generate_key()
        f = Fernet(key)
        enc = f.encrypt(pw.encode())
        
        out_dir = os.path.expanduser("~/Downloads/BlackTiger_Output")
        os.makedirs(out_dir, exist_ok=True)
        path = os.path.join(out_dir, "encrypted_pass.txt")
        with open(path, 'w') as f:
            f.write(f"Key: {key.decode()}\nEncrypted: {enc.decode()}")
        
        print(f"Saved: {path}")
    except:
        print("cryptography not installed. Run: pip install cryptography")

if __name__ == "__main__":
    run()