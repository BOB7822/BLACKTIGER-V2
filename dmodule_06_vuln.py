#!/usr/bin/env python3
# Web Vulnerability Scanner Module

import requests

def run():
    print("\n" + "="*60)
    print("WEB VULNERABILITY SCANNER")
    print("="*60)
    
    url = input("URL: ").strip()
    results = {}
    
    # SQL Injection
    for p in ["' OR 1=1--", "' UNION SELECT NULL--"]:
        try:
            r = requests.get(url + "?q=" + p, timeout=5)
            if "SQL" in r.text or "mysql" in r.text.lower():
                results["SQL Injection"] = "Possible"
        except:
            pass
    
    # XSS
    for p in ["<script>alert(1)</script>"]:
        try:
            r = requests.get(url + "?q=" + p, timeout=5)
            if p in r.text:
                results["XSS"] = "Possible"
        except:
            pass
    
    # LFI
    for p in ["../../../../etc/passwd"]:
        try:
            r = requests.get(url + "?file=" + p, timeout=5)
            if "root:" in r.text:
                results["LFI"] = "Possible"
        except:
            pass
    
    print("\nResults:")
    for k, v in results.items():
        print(f"  {k}: {v}")

if __name__ == "__main__":
    run()