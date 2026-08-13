#!/usr/bin/env python3
# 10 Minute Email Generator Module

import requests, time

def run():
    print("\n" + "="*60)
    print("10 MINUTE EMAIL GENERATOR")
    print("="*60)
    
    print("Generating temporary email...")
    
    try:
        response = requests.get("https://www.1secmail.com/api/v1/?action=genRandomMailbox&count=1")
        if response.status_code == 200:
            email = response.json()[0]
            print(f"\nEmail generated: {email}")
            
            parts = email.split('@')
            username = parts[0]
            domain = parts[1]
            
            print("\nWaiting for emails... Press Ctrl+C to stop")
            print(f"Email: {email}")
            
            while True:
                try:
                    check = requests.get(f"https://www.1secmail.com/api/v1/?action=getMessages&login={username}&domain={domain}")
                    if check.status_code == 200:
                        messages = check.json()
                        if messages:
                            for msg in messages:
                                print(f"\nNew email from: {msg.get('from', 'Unknown')}")
                                print(f"Subject: {msg.get('subject', 'No subject')}")
                                msg_id = msg.get('id')
                                if msg_id:
                                    full = requests.get(f"https://www.1secmail.com/api/v1/?action=readMessage&login={username}&domain={domain}&id={msg_id}")
                                    if full.status_code == 200:
                                        data = full.json()
                                        print(f"Body: {data.get('body', 'No content')[:500]}")
                                        print("-"*40)
                except:
                    pass
                time.sleep(5)
        else:
            print("Failed to generate email")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    run()