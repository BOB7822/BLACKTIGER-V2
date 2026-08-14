

import socket, dns.resolver, requests, json, re, time

def run():
    print("\n" + "="*60)
    print("EMAIL LOOKUP")
    print("="*60)
    
    print("[!] Enter an email address to lookup")
    print("[!] This will check MX records, DNS, and breach data")
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
    
    print(f"\n[+] Email: {email}")
    print(f"[+] Username: {username}")
    print(f"[+] Domain: {domain}")
    print("\n" + "="*60)
    
    # 1. Check MX Records
    print("\n[1] Checking MX Records...")
    try:
        mx_records = dns.resolver.resolve(domain, 'MX')
        print(f"    MX Records found: {len(mx_records)}")
        for mx in mx_records:
            print(f"    - {mx.exchange} (Priority: {mx.preference})")
    except dns.resolver.NoAnswer:
        print("    No MX records found")
    except dns.resolver.NXDOMAIN:
        print("    Domain does not exist")
    except Exception as e:
        print(f"    Error: {e}")
        print("    [i] Try installing dnspython: pip install dnspython")
    
    # 2. Check A Records
    print("\n[2] Checking A Records...")
    try:
        a_records = dns.resolver.resolve(domain, 'A')
        print(f"    A Records found: {len(a_records)}")
        for a in a_records:
            print(f"    - {a.address}")
    except:
        try:
            ip = socket.gethostbyname(domain)
            print(f"    IP Address: {ip}")
        except:
            print("    No A records found")
    
    # 3. Check SPF Records
    print("\n[3] Checking SPF Records...")
    try:
        txt_records = dns.resolver.resolve(domain, 'TXT')
        spf_found = False
        for txt in txt_records:
            txt_str = str(txt)
            if 'v=spf1' in txt_str:
                print(f"    SPF: {txt_str[:100]}...")
                spf_found = True
                break
        if not spf_found:
            print("    No SPF records found")
    except:
        print("    No SPF records found")
    
    # 4. Check if email exists on common services
    print("\n[4] Checking Common Email Services...")
    
    # Check if it's a known provider
    known_providers = {
        'gmail.com': 'Google (Gmail)',
        'googlemail.com': 'Google (Gmail)',
        'outlook.com': 'Microsoft (Outlook)',
        'hotmail.com': 'Microsoft (Hotmail)',
        'live.com': 'Microsoft (Live)',
        'msn.com': 'Microsoft (MSN)',
        'yahoo.com': 'Yahoo',
        'yahoo.co.uk': 'Yahoo UK',
        'protonmail.com': 'ProtonMail',
        'protonmail.ch': 'ProtonMail',
        'pm.me': 'ProtonMail',
        'icloud.com': 'Apple (iCloud)',
        'me.com': 'Apple (iCloud)',
        'mac.com': 'Apple (iCloud)',
        'aol.com': 'AOL',
        'mail.com': 'Mail.com',
        'yandex.com': 'Yandex',
        'yandex.ru': 'Yandex',
        'tutanota.com': 'Tutanota',
        'tuta.io': 'Tutanota',
        'keemail.me': 'Tutanota',
        'zoho.com': 'Zoho',
        'zohomail.com': 'Zoho',
        'gmx.com': 'GMX',
        'gmx.net': 'GMX',
        'web.de': 'Web.de',
        'posteo.de': 'Posteo',
        'mailbox.org': 'Mailbox.org',
        'fastmail.com': 'FastMail',
        'fastmail.fm': 'FastMail'
    }
    
    if domain in known_providers:
        print(f"    Provider: {known_providers[domain]}")
    else:
        print(f"    Provider: Unknown/Custom Domain")
    
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
            for breach in breaches[:5]:
                print(f"    - {breach.get('Name', 'Unknown')} ({breach.get('BreachDate', 'Unknown')})")
            if len(breaches) > 5:
                print(f"    ... and {len(breaches) - 5} more")
        elif response.status_code == 404:
            print("    No breaches found")
        else:
            print(f"    Error: {response.status_code}")
    except requests.exceptions.Timeout:
        print("    Timeout - try again later")
    except Exception as e:
        print(f"    Error: {e}")
    
    # 6. Check Email Reputation (using emailrep.io)
    print("\n[6] Checking Email Reputation...")
    try:
        response = requests.get(f"https://emailrep.io/{email}", timeout=10)
        if response.status_code == 200:
            data = response.json()
            rep = data.get('reputation', 'Unknown')
            suspicious = data.get('suspicious', False)
            print(f"    Reputation: {rep}")
            print(f"    Suspicious: {suspicious}")
            
            if 'details' in data:
                details = data['details']
                if details.get('first_seen'):
                    print(f"    First seen: {details['first_seen']}")
                if details.get('last_seen'):
                    print(f"    Last seen: {details['last_seen']}")
                if details.get('is_free_provider'):
                    print(f"    Free provider: {details['is_free_provider']}")
                if details.get('is_disposable'):
                    print(f"    Disposable: {details['is_disposable']}")
        else:
            print("    Could not get reputation (rate limited)")
    except:
        print("    Could not get reputation")
    
    # 7. Check if domain is valid
    print("\n[7] Checking Domain Validity...")
    try:
        socket.gethostbyname(domain)
        print("    Domain is active")
    except:
        print("    Domain may be inactive")
    
    # 8. Generate Google Dorks
    print("\n[8] Google Dorks for this email:")
    dorks = [
        f'"{email}"',
        f'"{username}" "{domain}"',
        f'site:github.com "{email}"',
        f'site:linkedin.com "{email}"'
    ]
    for dork in dorks:
        print(f"    https://www.google.com/search?q={dork.replace(' ', '+')}")
    
    # Summary
    print("\n" + "="*60)
    print("SUMMARY")
    print("="*60)
    print(f"Email: {email}")
    print(f"Username: {username}")
    print(f"Domain: {domain}")
    print("="*60)
    
    input("\nPress Enter to continue...")

if __name__ == "__main__":
    run()
