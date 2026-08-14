#!/usr/bin/env python3
# Discord Webhook Spammer Module - Fixed

import requests, time, random, sys, os, json

def run():
    print("\n" + "="*60)
    print("DISCORD WEBHOOK SPAMMER")
    print("="*60)
    
    print("[!] Webhook URL format: https://discord.com/api/webhooks/ID/TOKEN")
    print("[!] Get it from: Server Settings > Integrations > Webhooks")
    print("="*60)
    
    webhook_url = input("\nWebhook URL: ").strip()
    
    # Validate webhook URL
    if not webhook_url.startswith('https://discord.com/api/webhooks/'):
        print("\n[!] Invalid webhook URL!")
        print("[!] Correct format: https://discord.com/api/webhooks/123456789/abcDEFghiJKL")
        input("\nPress Enter to continue...")
        return
    
    # Test the webhook first
    print("\n[+] Testing webhook connection...")
    try:
        test_payload = {"content": "Testing connection..."}
        test_response = requests.post(webhook_url, json=test_payload, timeout=10)
        
        if test_response.status_code in [200, 204]:
            print("[+] Webhook is working!")
        else:
            print(f"[!] Webhook test failed: {test_response.status_code}")
            print("[!] Make sure the webhook is valid and not deleted")
            input("\nPress Enter to continue...")
            return
    except Exception as e:
        print(f"[!] Could not connect: {e}")
        input("\nPress Enter to continue...")
        return
    
    # Get spam settings
    print("\n" + "="*60)
    print("SPAM SETTINGS")
    print("="*60)
    
    message = input("Message (leave blank for random): ").strip()
    count = int(input("Number of messages [10]: ").strip() or "10")
    delay = float(input("Delay between messages [0.5]: ").strip() or "0.5")
    
    # Random messages
    random_messages = [
        "BlackTiger Pro",
        "Webhook Spammer",
        "Discord Tools",
        "Hacked by BlackTiger",
        "This is a test message",
        "BlackTiger V2.0",
        "Discord Webhook Spammer",
        "https://github.com/BOB7822/BLACKTIGER-V2",
        "Join Discord.gg/nvbQsxFJgz",
        "BlackTiger was here",
        "Hello from BlackTiger!",
        "Webhook testing...",
        "Discord API is fun!",
        "BlackTiger Ultimate Edition"
    ]
    
    print("\n" + "="*60)
    print("SENDING MESSAGES...")
    print("="*60)
    print(f"Target: {webhook_url[:50]}...")
    print(f"Messages: {count}")
    print(f"Delay: {delay}s")
    print("Press Ctrl+C to stop")
    print("="*60)
    
    success_count = 0
    fail_count = 0
    
    for i in range(count):
        try:
            # Choose message
            if message:
                msg = message
            else:
                msg = random.choice(random_messages)
            
            # Build payload
            payload = {
                "content": f"{msg} [{i+1}/{count}]",
                "username": "BlackTiger",
                "avatar_url": "https://i.imgur.com/blacktiger.png"
            }
            
            # Send the message
            response = requests.post(webhook_url, json=payload, timeout=10)
            
            # Handle response
            if response.status_code in [200, 204]:
                success_count += 1
                print(f"[OK] Message {i+1}/{count} sent")
                
            elif response.status_code == 429:
                # Rate limited
                try:
                    retry_after = response.json().get('retry_after', 5)
                except:
                    retry_after = 5
                print(f"[!] Rate limited, waiting {retry_after}s...")
                time.sleep(retry_after)
                
                # Retry
                retry_response = requests.post(webhook_url, json=payload, timeout=10)
                if retry_response.status_code in [200, 204]:
                    success_count += 1
                    print(f"[OK] Message {i+1}/{count} sent (retry)")
                else:
                    fail_count += 1
                    print(f"[FAIL] Message {i+1}/{count} failed: {retry_response.status_code}")
                    
            elif response.status_code == 404:
                fail_count += 1
                print(f"[FAIL] Webhook not found or deleted (404)")
                break
                
            elif response.status_code == 401:
                fail_count += 1
                print(f"[FAIL] Invalid webhook token (401)")
                break
                
            else:
                fail_count += 1
                print(f"[FAIL] Message {i+1}/{count} failed: {response.status_code}")
            
            time.sleep(delay)
            
        except KeyboardInterrupt:
            print("\n[!] Stopped by user")
            break
            
        except requests.exceptions.Timeout:
            fail_count += 1
            print(f"[FAIL] Message {i+1}/{count} timed out")
            
        except requests.exceptions.ConnectionError:
            fail_count += 1
            print(f"[FAIL] Connection error - check your internet")
            break
            
        except Exception as e:
            fail_count += 1
            print(f"[FAIL] Error: {e}")
    
    # Results
    print("\n" + "="*60)
    print("RESULTS")
    print("="*60)
    print(f"Successful: {success_count}")
    print(f"Failed: {fail_count}")
    print(f"Total: {success_count + fail_count}")
    print("="*60)
    
    if fail_count > 0:
        print("\n[!] Troubleshooting:")
        print("1. Make sure the webhook URL is correct")
        print("2. The webhook must be from the same server you're in")
        print("3. Check that the webhook hasn't been deleted")
        print("4. You might be rate limited - wait a few seconds")
    
    input("\nPress Enter to continue...")

if __name__ == "__main__":
    run()
