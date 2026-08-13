#!/usr/bin/env python3
# Python Obfuscator Module

import os, sys, re, base64

def run():
    print("\n" + "="*60)
    print("PYTHON OBFUSCATOR")
    print("="*60)
    
    path = input("Path to Python file: ").strip()
    if not os.path.exists(path):
        print("File not found")
        return
    
    with open(path, 'r') as f:
        code = f.read()
    
    print("[1] String Encryption")
    print("[2] Variable Renaming")
    print("[3] All (Recommended)")
    choice = input("> ").strip()
    
    obf_code = code
    if choice in ['1', '3']:
        lines = code.split('\n')
        obf = []
        for line in lines:
            def repl(m):
                s = m.group(0)
                enc = base64.b64encode(s.encode()).decode()
                return f"__import__('base64').b64decode('{enc}').decode()"
            line = re.sub(r'"[^"]*"', repl, line)
            line = re.sub(r"'[^']*'", repl, line)
            obf.append(line)
        obf_code = "\n".join(obf)
    
    out_dir = os.path.expanduser("~/Downloads/BlackTiger_Output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "obfuscated.py")
    with open(path, 'w') as f:
        f.write(obf_code)
    
    print(f"Saved: {path}")

if __name__ == "__main__":
    run()