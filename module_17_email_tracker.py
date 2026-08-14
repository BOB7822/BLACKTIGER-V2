#!/usr/bin/env python3
# Email Tracker Module

import re, requests, json, dns.resolver, socket, time, sys

def run():
    print("\n" + "="*60)
    print("EMAIL TRACKER")
    print("="*60)
    
    print("[!] Enter an email address to track")
    print("[!] This will check the email across multiple services")
    print("="*60)
    
    email = input("\nEnter email address: ").strip()
    
    if not email:
        print("No email entered")
        input("\nPress Enter to continue...")
        return
    
    if '@' not in email:
        print("[!] Invalid email format - missing @")
        input("\nPress Enter to continue...")
        return
    
    username = email.split('@')[0]
    domain = email.split('@')[1]
    
    print(f"\n[+] Tracking: {email}")
    print(f"[+] Username: {username}")
    print(f"[+] Domain: {domain}")
    print("\n" + "="*60)
    
    results = {}
    
    # 1. Validate email format
    print("\n[1] Validating email format...")
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.match(email_pattern, email):
        print("    Valid email format")
        results['format'] = 'Valid'
    else:
        print("    Invalid email format")
        results['format'] = 'Invalid'
    
    # 2. Check domain MX records
    print("\n[2] Checking MX records...")
    try:
        mx_records = dns.resolver.resolve(domain, 'MX')
        print(f"    MX records found: {len(mx_records)}")
        for mx in mx_records:
            print(f"    - {mx.exchange} (Priority: {mx.preference})")
        results['mx_records'] = True
    except:
        print("    No MX records found")
        results['mx_records'] = False
    
    # 3. Check if email provider is known
    print("\n[3] Identifying provider...")
    known_providers = {
        'gmail.com': {'name': 'Google (Gmail)', 'check': 'https://mail.google.com'},
        'googlemail.com': {'name': 'Google (Gmail)', 'check': 'https://mail.google.com'},
        'outlook.com': {'name': 'Microsoft (Outlook)', 'check': 'https://outlook.live.com'},
        'hotmail.com': {'name': 'Microsoft (Hotmail)', 'check': 'https://outlook.live.com'},
        'live.com': {'name': 'Microsoft (Live)', 'check': 'https://outlook.live.com'},
        'msn.com': {'name': 'Microsoft (MSN)', 'check': 'https://outlook.live.com'},
        'yahoo.com': {'name': 'Yahoo', 'check': 'https://mail.yahoo.com'},
        'yahoo.co.uk': {'name': 'Yahoo UK', 'check': 'https://mail.yahoo.com'},
        'protonmail.com': {'name': 'ProtonMail', 'check': 'https://protonmail.com'},
        'protonmail.ch': {'name': 'ProtonMail', 'check': 'https://protonmail.com'},
        'pm.me': {'name': 'ProtonMail', 'check': 'https://protonmail.com'},
        'icloud.com': {'name': 'Apple (iCloud)', 'check': 'https://icloud.com'},
        'me.com': {'name': 'Apple (iCloud)', 'check': 'https://icloud.com'},
        'mac.com': {'name': 'Apple (iCloud)', 'check': 'https://icloud.com'},
        'aol.com': {'name': 'AOL', 'check': 'https://mail.aol.com'},
        'mail.com': {'name': 'Mail.com', 'check': 'https://www.mail.com'},
        'yandex.com': {'name': 'Yandex', 'check': 'https://mail.yandex.com'},
        'yandex.ru': {'name': 'Yandex', 'check': 'https://mail.yandex.ru'},
        'tutanota.com': {'name': 'Tutanota', 'check': 'https://tutanota.com'},
        'tuta.io': {'name': 'Tutanota', 'check': 'https://tutanota.com'},
        'zoho.com': {'name': 'Zoho', 'check': 'https://mail.zoho.com'},
        'gmx.com': {'name': 'GMX', 'check': 'https://www.gmx.com'},
        'web.de': {'name': 'Web.de', 'check': 'https://web.de'},
        'fastmail.com': {'name': 'FastMail', 'check': 'https://www.fastmail.com'}
    }
    
    if domain in known_providers:
        print(f"    Provider: {known_providers[domain]['name']}")
        print(f"    Login URL: {known_providers[domain]['check']}")
        results['provider'] = known_providers[domain]['name']
    else:
        print(f"    Provider: Custom/Domain email")
        results['provider'] = 'Custom'
    
    # 4. Check if email exists (using gravatar)
    print("\n[4] Checking Gravatar...")
    try:
        import hashlib
        email_hash = hashlib.md5(email.lower().encode()).hexdigest()
        gravatar_url = f"https://www.gravatar.com/avatar/{email_hash}?d=404"
        response = requests.get(gravatar_url, timeout=5)
        if response.status_code == 200:
            print("    Gravatar found!")
            results['gravatar'] = True
        else:
            print("    No Gravatar found")
            results['gravatar'] = False
    except:
        print("    Could not check Gravatar")
    
    # 5. Check Have I Been Pwned
    print("\n[5] Checking Have I Been Pwned...")
    try:
        response = requests.get(
            f"https://haveibeenpwned.com/api/v3/breachedaccount/{email}",
            headers={'hibp-api-key': ''},
            timeout=10
        )
        if response.status_code == 200:
            breaches = response.json()
            print(f"    Breaches found: {len(breaches)}")
            for breach in breaches[:3]:
                print(f"    - {breach.get('Name', 'Unknown')} ({breach.get('BreachDate', 'Unknown')})")
            if len(breaches) > 3:
                print(f"    ... and {len(breaches) - 3} more")
            results['breaches'] = len(breaches)
        elif response.status_code == 404:
            print("    No breaches found")
            results['breaches'] = 0
        else:
            print(f"    Error: {response.status_code}")
    except:
        print("    Could not check breaches")
    
    # 6. Check email reputation
    print("\n[6] Checking email reputation...")
    try:
        response = requests.get(f"https://emailrep.io/{email}", timeout=10)
        if response.status_code == 200:
            data = response.json()
            rep = data.get('reputation', 'Unknown')
            suspicious = data.get('suspicious', False)
            print(f"    Reputation: {rep}")
            print(f"    Suspicious: {suspicious}")
            results['reputation'] = rep
        else:
            print("    Could not get reputation")
    except:
        print("    Could not get reputation")
    
    # 7. Search for username across platforms
    print("\n[7] Searching for username across platforms...")
    platforms = {
        'GitHub': f'https://github.com/{username}',
        'Twitter': f'https://twitter.com/{username}',
        'Instagram': f'https://instagram.com/{username}',
        'Reddit': f'https://reddit.com/user/{username}',
        'YouTube': f'https://youtube.com/@{username}',
        'Facebook': f'https://facebook.com/{username}',
        'LinkedIn': f'https://linkedin.com/in/{username}',
        'Pinterest': f'https://pinterest.com/{username}',
        'Tumblr': f'https://{username}.tumblr.com',
        'GitLab': f'https://gitlab.com/{username}',
        'Keybase': f'https://keybase.io/{username}',
        'Medium': f'https://medium.com/@{username}',
        'Spotify': f'https://open.spotify.com/user/{username}',
        'Steam': f'https://steamcommunity.com/id/{username}'
    }
    
    found_platforms = []
    for platform, url in platforms.items():
        try:
            response = requests.get(url, timeout=3, headers={'User-Agent': 'Mozilla/5.0'})
            if response.status_code == 200:
                print(f"    - Found on {platform}")
                found_platforms.append(platform)
        except:
            pass
    
    if found_platforms:
        print(f"    Found on {len(found_platforms)} platforms")
        results['platforms'] = found_platforms
    else:
        print("    No platforms found")
    
    # 8. Generate email variations
    print("\n[8] Email variations:")
    variations = [
        email,
        f"{username}@{domain}",
        f"{username.lower()}@{domain}",
        f"{username.upper()}@{domain}",
        f"{username}.{domain.split('.')[0]}@{domain}" if '.' in domain else None,
    ]
    for var in variations:
        if var:
            print(f"    - {var}")
    
    # 9. Generate Google dorks
    print("\n[9] Google dorks for this email:")
    dorks = [
        f'"{email}"',
        f'"{username}" "{domain}"',
        f'site:github.com "{email}"',
        f'site:linkedin.com "{email}"',
        f'"{email}" filetype:pdf'
    ]
    for dork in dorks:
        search_url = f"https://www.google.com/search?q={dork.replace(' ', '+')}"
        print(f"    {search_url[:80]}...")
    
    # 10. Try to find social media links
    print("\n[10] Checking for social media links...")
    social_urls = [
        f"https://www.facebook.com/search/top/?q={email}",
        f"https://www.linkedin.com/search/results/all/?keywords={email}",
        f"https://twitter.com/search?q={email}",
        f"https://www.instagram.com/web/search/top/?q={email}",
        f"https://github.com/search?q={email}"
    ]
    for url in social_urls:
        print(f"    {url[:80]}...")
    
    # Summary
    print("\n" + "="*60)
    print("TRACKING SUMMARY")
    print("="*60)
    print(f"Email: {email}")
    print(f"Username: {username}")
    print(f"Domain: {domain}")
    print(f"Provider: {results.get('provider', 'Unknown')}")
    print(f"Format: {results.get('format', 'Unknown')}")
    print(f"MX Records: {'Yes' if results.get('mx_records', False) else 'No'}")
    print(f"Breaches: {results.get('breaches', 'Unknown')}")
    print(f"Gravatar: {'Yes' if results.get('gravatar', False) else 'No'}")
    if results.get('platforms'):
        print(f"Platforms Found: {', '.join(results['platforms'][:5])}")
    print("="*60)
    
    input("\nPress Enter to continue...")

if __name__ == "__main__":
    run()
