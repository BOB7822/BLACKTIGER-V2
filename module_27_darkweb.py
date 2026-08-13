#!/usr/bin/env python3
# Dark Web Links Module

def run():
    print("\n" + "="*60)
    print("DARK WEB LINKS")
    print("="*60)
    
    links = [
        ("Dread", "http://dread.onion"),
        ("Torch", "http://torch.onion"),
        ("Ahmia", "http://ahmia.onion"),
        ("DarkNetLive", "http://darknetlive.onion"),
        ("HiddenWiki", "http://hiddenwiki.onion")
    ]
    
    for name, url in links:
        print(f"  {name}: {url}")
    
    print("\nUse Tor Browser to access these links")

if __name__ == "__main__":
    run()