#!/usr/bin/env python3
# 10 Minute Email Generator Module - Working Version

import requests, time, json, os, sys

def run():
    print("\n" + "="*60)
    print("10 MINUTE EMAIL GENERATOR")
    print("="*60)
    
    print("Generating temporary email...")
    
    try:
        # Generate email using 1secmail API
        response = requests.get("https://www.1secmail.com/api/v1/?action=genRandomMailbox&count=1")
        if response.status_code == 200:
            email = response.json()[0]
            print(f"\n[+] Email generated: {email}")
            
            parts = email.split('@')
            username = parts[0]
            domain = parts[1]
            
            print("\n" + "="*60)
            print("WAITING FOR EMAILS...")
            print("Press Ctrl+C to stop")
            print("="*60)
            print(f"Email: {email}")
            print("="*60)
            
            # Show inbox every 5 seconds
            while True:
                try:
                    # Check for new messages
                    check = requests.get(f"https://www.1secmail.com/api/v1/?action=getMessages&login={username}&domain={domain}")
                    if check.status_code == 200:
                        messages = check.json()
                        if messages:
                            print(f"\n[{time.strftime('%H:%M:%S')}] New email received!")
                            for msg in messages:
                                print(f"  From: {msg.get('from', 'Unknown')}")
                                print(f"  Subject: {msg.get('subject', 'No subject')}")
                                print(f"  Date: {msg.get('date', 'Unknown')}")
                                
                                # Get full message body
                                msg_id = msg.get('id')
                                if msg_id:
                                    full = requests.get(f"https://www.1secmail.com/api/v1/?action=readMessage&login={username}&domain={domain}&id={msg_id}")
                                    if full.status_code == 200:
                                        data = full.json()
                                        body = data.get('body', 'No content')
                                        print(f"  Body: {body[:500]}...")
                                        print("-"*40)
                            print("="*60)
                        else:
                            print(f"[{time.strftime('%H:%M:%S')}] Waiting for emails...")
                except:
                    pass
                time.sleep(5)
        else:
            print("Failed to generate email")
            
    except KeyboardInterrupt:
        print("\n\n[!] Stopped by user")
        print(f"[+] Your temporary email was: {email if 'email' in locals() else 'Unknown'}")
        print("Check it at: https://www.1secmail.com/login")
        input("\nPress Enter to continue...")
    except Exception as e:
        print(f"Error: {e}")
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    run()
