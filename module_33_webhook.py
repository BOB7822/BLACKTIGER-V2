#!/usr/bin/env python3
# Discord Webhook Spammer Module

import requests, time, random

def run():
    print("\n" + "="*60)
    print("DISCORD WEBHOOK SPAMMER")
    print("="*60)
    
    webhook_url = input("Webhook URL: ").strip()
    message = input("Message (leave blank for random): ").strip()
    count = int(input("Number of messages [10]: ").strip() or "10")
    delay = float(input("Delay between messages [0.5]: ").strip() or "0.5")
    
    if not message:
        messages = ["BlackTiger Pro", "Webhook Spammer", "Discord Tools", "Hacked by BlackTiger"]
    
    print(f"Sending {count} messages...")
    
    for i in range(count):
        try:
            msg = message if message else random.choice(messages)
            payload = {"content": msg + f" [{i+1}/{count}]", "username": "BlackTiger"}
            response = requests.post(webhook_url, json=payload)
            if response.status_code == 204:
                print(f"[OK] Message {i+1} sent")
            else:
                print(f"[FAIL] Message {i+1} failed: {response.status_code}")
            time.sleep(delay)
        except Exception as e:
            print(f"Error: {e}")
    
    print("Spam complete!")

if __name__ == "__main__":
    run()