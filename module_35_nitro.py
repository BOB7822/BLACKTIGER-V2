#!/usr/bin/env python3
# Discord Nitro Generator Module

import random, string

def run():
    print("\n" + "="*60)
    print("DISCORD NITRO GENERATOR")
    print("="*60)
    
    count = int(input("Number of codes [10]: ").strip() or "10")
    
    print("\nGenerated Nitro codes:")
    print("Note: These are random codes, not guaranteed to work")
    
    for i in range(count):
        code = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
        print(f"  [{i+1}] https://discord.gift/{code}")

if __name__ == "__main__":
    run()