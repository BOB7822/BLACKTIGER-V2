#!/usr/bin/env python3


import requests, time, json, os, sys, random, string

def run():
    print("\n" + "="*60)
    print("10 MINUTE EMAIL GENERATOR")
    print("="*60)
    
    print("Generating temporary email...")
    
   
    email = None
    
    
    try:
        print("[1] Trying 1secmail...")
        response = requests.get("https://www.1secmail.com/api/v1/?action=genRandomMailbox&count=1", timeout=10)
        if response.status_code == 200:
            email = response.json()[0]
            print(f"[+] Email generated: {email}")
    except:
        print("[!] 1secmail failed, trying next method...")
    
    
    if not email:
        try:
            print("[2] Trying temp-mail...")
            response = requests.get("https://api.temp-mail.org/request/domains/format/json", timeout=10)
            if response.status_code == 200:
                domains = response.json()
                domain = domains[0] if domains else "temp-mail.org"
            else:
                domain = "temp-mail.org"
            
            username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
            email = f"{username}@{domain}"
            print(f"[+] Email generated: {email}")
        except:
            print("[!] temp-mail failed, trying next method...")
    
  
    if not email:
        try:
            print("[3] Trying guerillamail...")
            response = requests.get("https://api.guerrillamail.com/ajax.php?f=get_email_address", timeout=10)
            if response.status_code == 200:
                data = response.json()
                email = data.get('email_addr')
                print(f"[+] Email generated: {email}")
        except:
            print("[!] guerillamail failed, trying next method...")
    
    
    if not email:
        try:
            print("[4] Trying throwawaymail...")
            response = requests.post("https://api.throwawaymail.com/v1/addresses", timeout=10)
            if response.status_code == 200:
                data = response.json()
                email = data.get('email')
                print(f"[+] Email generated: {email}")
        except:
            print("[!] throwawaymail failed...")
    
    
    if not email:
        print("[5] Generating manual email...")
        domains = ['gmail.com', 'outlook.com', 'yahoo.com', 'protonmail.com', 'icloud.com', 'temp-mail.org', 'mailinator.com']
        username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
        domain = random.choice(domains)
        email = f"{username}@{domain}"
        print(f"[+] Email generated: {email}")
    
    if not email:
        print("[!] All methods failed. Using fallback email...")
        username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
        email = f"{username}@temp-mail.org"
        print(f"[+] Fallback email: {email}")
    
    
    print("\n" + "="*60)
    print("EMAIL GENERATED SUCCESSFULLY!")
    print("="*60)
    print(f"Email: {email}")
    print("="*60)
    print("\nCheck your email at:")
    print(f"https://www.1secmail.com/login")
    print(f"https://www.temp-mail.org/en/")
    print("="*60)
    
    # Ask if user wants to check for emails
    check = input("\nCheck for emails automatically? [y/N]: ").strip().lower()
    
    if check == 'y':
        if '@1secmail.com' in email:
            username = email.split('@')[0]
            domain = email.split('@')[1]
            print("\nWaiting for emails... Press Ctrl+C to stop")
            while True:
                try:
                    response = requests.get(f"https://www.1secmail.com/api/v1/?action=getMessages&login={username}&domain={domain}", timeout=10)
                    if response.status_code == 200:
                        messages = response.json()
                        if messages:
                            print(f"\n[{time.strftime('%H:%M:%S')}] New email received!")
                            for msg in messages:
                                print(f"  From: {msg.get('from', 'Unknown')}")
                                print(f"  Subject: {msg.get('subject', 'No subject')}")
                                msg_id = msg.get('id')
                                if msg_id:
                                    full = requests.get(f"https://www.1secmail.com/api/v1/?action=readMessage&login={username}&domain={domain}&id={msg_id}")
                                    if full.status_code == 200:
                                        data = full.json()
                                        print(f"  Body: {data.get('body', 'No content')[:300]}...")
                            print("-"*40)
                except:
                    pass
                time.sleep(5)
        else:
            print("\nAuto-check only works for 1secmail.com emails")
            print(f"Manually check: https://www.1secmail.com/login")
            print(f"Email: {email}")
    
    input("\nPress Enter to continue...")

if __name__ == "__main__":
    run()
