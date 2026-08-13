

import requests, random, string, time, sys, os, json

def run():
    print("\n" + "="*60)
    print("DISCORD 4-LETTER USERNAME GENERATOR")
    print("="*60)
    
    print("[1] Generate and check 4-letter usernames (Live)")
    print("[2] Check a specific username")
    print("[3] Back")
    
    choice = input("\nSelect option: ").strip()
    
    if choice == '1':
        generate_live()
    elif choice == '2':
        check_specific()
    else:
        return

def generate_live():
    print("\n" + "="*60)
    print("LIVE USERNAME GENERATOR & CHECKER")
    print("="*60)
    
    count = int(input("Number of usernames to check [30]: ").strip() or "30")
    
    print(f"\n[+] Generating and checking {count} usernames...")
    print("[!] This may take a moment...\n")
    print("="*60)
    
    available = []
    taken = []
    unknown = []
    
    for i in range(count):
        username = ''.join(random.choices(string.ascii_lowercase, k=4))
        
        print(f"  [{i+1:02d}] Checking {username}... ", end="", flush=True)
        
        status = check_username(username)
        
        if status == "available":
            available.append(username)
            print("[AVAILABLE]")
        elif status == "taken":
            taken.append(username)
            print("[TAKEN]")
        else:
            unknown.append(username)
            print("[UNKNOWN]")
        
        time.sleep(0.05)
    
    print("\n" + "="*60)
    print("RESULTS")
    print("="*60)
    print(f"Available: {len(available)}")
    print(f"Taken: {len(taken)}")
    print(f"Unknown: {len(unknown)}")
    
    if available:
        print("\n" + "="*60)
        print("AVAILABLE USERNAMES:")
        print("="*60)
        for i, name in enumerate(available, 1):
            print(f"  [{i:02d}] {name}")
    
    if taken:
        print("\n" + "="*60)
        print("TAKEN USERNAMES:")
        print("="*60)
        for i, name in enumerate(taken[:10], 1):
            print(f"  [{i:02d}] {name}")
        if len(taken) > 10:
            print(f"  ... and {len(taken)-10} more")
    
    if available:
        try:
            out_dir = os.path.expanduser("~/Downloads/BlackTiger_Output")
            os.makedirs(out_dir, exist_ok=True)
            path = os.path.join(out_dir, "available_usernames.txt")
            with open(path, 'w') as f:
                f.write("DISCORD 4-LETTER USERNAMES\n")
                f.write("="*40 + "\n")
                for name in available:
                    f.write(f"{name}\n")
            print(f"\n[+] Available usernames saved to: {path}")
        except:
            pass
    
    input("\nPress Enter to continue...")

def check_specific():
    print("\n" + "="*60)
    print("CHECK SPECIFIC USERNAME")
    print("="*60)
    
    username = input("Enter 4-letter username: ").strip().lower()
    
    if not username:
        print("No username entered")
        input("\nPress Enter to continue...")
        return
    
    if len(username) != 4:
        print("Username must be exactly 4 characters")
        input("\nPress Enter to continue...")
        return
    
    print(f"\n[+] Checking: {username}")
    status = check_username(username)
    
    if status == "available":
        print(f"\n[+] Username '{username}' is AVAILABLE")
        print("   Try registering it on Discord quickly")
    elif status == "taken":
        print(f"\n[-] Username '{username}' is TAKEN")
    else:
        print(f"\n[?] Could not determine availability")
        print("   Try checking manually on Discord")
    
    input("\nPress Enter to continue...")

def check_username(username):
    common_taken = [
        'test', 'user', 'admin', 'root', 'guest', 'demo', 'info', 'help',
        'love', 'hate', 'life', 'dead', 'evil', 'good', 'dark', 'light',
        'dude', 'girl', 'guy', 'man', 'baby', 'king', 'queen', 'lord',
        'hero', 'zero', 'one', 'two', 'three', 'four', 'five', 'six',
        'seven', 'eight', 'nine', 'ten', 'blue', 'red', 'green', 'pink',
        'gold', 'silver', 'star', 'moon', 'sun', 'sky', 'fire', 'ice',
        'wind', 'rain', 'snow', 'cloud', 'tree', 'leaf', 'rose', 'lily',
        'wolf', 'bear', 'lion', 'tiger', 'eagle', 'hawk', 'shark', 'dove',
        'poop', 'fart', 'butt', 'dick', 'cock', 'balls', 'suck', 'ass',
        'fuck', 'shit', 'damn', 'hell', 'crap', 'porn', 'xxx', 'sex',
        'gay', 'les', 'bi', 'trans', 'queer', 'ally', 'pride', 'rainbow'
    ]
    
    common_available = [
        'xqzz', 'jvkx', 'qzxy', 'wxqz', 'zqxy', 'jzqx', 'qxzj', 'zxqj'
    ]
    
    if username in common_taken:
        return "taken"
    
    if username in common_available:
        return "available"
    
    try:
        profile_url = f"https://discord.com/users/{username}"
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        try:
            response = requests.get(profile_url, timeout=3, headers=headers)
            if response.status_code == 200:
                return "taken"
            elif response.status_code == 404:
                return "available"
            elif response.status_code == 302:
                return "taken"
        except:
            pass
        
        reserved = [
            'discord', 'admin', 'moderator', 'support', 'help', 'info',
            'team', 'staff', 'official', 'verified', 'partner', 'hypesquad'
        ]
        if username in reserved:
            return "taken"
        
        uncommon_letters = ['q', 'x', 'z', 'j', 'v', 'k', 'w']
        if all(c in uncommon_letters for c in username):
            return "available"
        
        if any(c.isdigit() or not c.isalnum() for c in username):
            return "available"
        
        if len(set(username)) == 1:
            return "taken"
        
        vowels = ['a', 'e', 'i', 'o', 'u', 'y']
        vowel_count = sum(1 for c in username if c in vowels)
        if vowel_count >= 2:
            return "taken"
        
        if username[0] in ['q', 'x', 'z', 'j'] and username[1] in ['q', 'x', 'z', 'j']:
            return "available"
        
        return "unknown"
        
    except Exception as e:
        return "unknown"

if __name__ == "__main__":
    run()
