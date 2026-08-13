#!/usr/bin/env python3
# Discord Nitro Generator Module - Live Display

import random, string, time, os, sys

def run():
    print("\n" + "="*60)
    print("DISCORD NITRO GENERATOR")
    print("="*60)
    
    print("Generating Discord Nitro codes...")
    
    count = input("Number of codes to generate [10]: ").strip()
    if not count:
        count = 10
    else:
        try:
            count = int(count)
        except:
            count = 10
    
    print("\n" + "="*60)
    print(f"Generating {count} Nitro codes:")
    print("="*60)
    print("Note: These are random codes, NOT guaranteed to work")
    print("="*60 + "\n")
    
    codes = []
    for i in range(count):
        # Generate random 16-character code
        code = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
        codes.append(code)
        
        # Show live generation with number
        print(f"  [{i+1:02d}] Generating... ", end="", flush=True)
        time.sleep(0.05)
        print(f"https://discord.gift/{code}")
    
    print("\n" + "="*60)
    print(f"Total codes generated: {len(codes)}")
    print("="*60)
    
    # Save to file
    try:
        out_dir = os.path.expanduser("~/Downloads/BlackTiger_Output")
        os.makedirs(out_dir, exist_ok=True)
        path = os.path.join(out_dir, "nitro_codes.txt")
        with open(path, 'w') as f:
            for code in codes:
                f.write(f"https://discord.gift/{code}\n")
        print(f"\n[+] Codes saved to: {path}")
    except:
        pass
    
    input("\nPress Enter to continue...")

if __name__ == "__main__":
    run()
