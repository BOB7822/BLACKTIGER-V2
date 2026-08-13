

import requests, time, random, sys, os

def run():
    print("\n" + "="*60)
    print("DISCORD WEBHOOK SPAMMER")
    print("="*60)
    
    
    
    webhook_url = input("\nPaste your Webhook URL: ").strip()
    
    # Validate webhook URL
    if not webhook_url.startswith('https://discord.com/api/webhooks/'):
        print("\n[!] INVALID WEBHOOK URL!")
        print("[!] Correct format: https://discord.com/api/webhooks/123456789/abcDEFghiJKL")
        print("[!] You entered: " + webhook_url[:50] + "...")
        print("\n[!] Make sure you copied the Webhook URL, not a channel URL")
        print("[!] Channel URLs look like: https://discord.com/channels/...")
        print("\nPress Enter to continue...")
        input()
        return
    
    print("\n[+] Webhook URL looks valid!")
    print("[+] Testing connection...")
    
    # Test the webhook
    try:
        test_response = requests.post(webhook_url, json={"content": "Testing connection..."})
        if test_response.status_code in [200, 204]:
            print("[+] Webhook is working!")
        else:
            print(f"[!] Webhook test failed: {test_response.status_code}")
            print("[!] Make sure the webhook is valid and not deleted")
            input("\nPress Enter to continue...")
            return
    except:
        print("[!] Could not connect to webhook")
        input("\nPress Enter to continue...")
        return
    
    print("\n" + "="*60)
    print("SPAM SETTINGS")
    print("="*60)
    
    message = input("Message (leave blank for random): ").strip()
    count = int(input("Number of messages [10]: ").strip() or "10")
    delay = float(input("Delay between messages [0.5]: ").strip() or "0.5")
    
                 if none provided
    if not message:
        messages = [
            "BlackTiger ",
            "Webhook Spammer",
            "Discord Tools",
            "Hacked by BlackTiger",
            "This is a test message",
            "BlackTiger V2.0",
            "Discord Webhook Spammer",
            "https://github.com/BOB7822/BLACKTIGER-V2",
            "Join Discord.gg/nvbQsxFJgz",
            "BlackTiger was here"
        ]
    
    print("\n" + "="*60)
    print("SPAMMING...")
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
                msg = random.choice(messages)
            
            # Build payload
            payload = {
                "content": f"{msg} [{i+1}/{count}]",
                "username": "BlackTiger",
                "avatar_url": "https://i.imgur.com/blacktiger.png"
            }
            
            # Send the message
            response = requests.post(webhook_url, json=payload, timeout=10)
            
            # Handle response
            if response.status_code == 204:
                success_count += 1
                print(f"[OK] Message {i+1}/{count} sent")
                
            elif response.status_code == 200:
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
                print("[!] Create a new webhook")
                break
                
            elif response.status_code == 401:
                fail_count += 1
                print(f"[FAIL] Invalid webhook token (401)")
                print("[!] Check if the webhook URL is correct")
                break
                
            else:
                fail_count += 1
                print(f"[FAIL] Message {i+1}/{count} failed: {response.status_code}")
                if response.status_code == 400:
                    print("[!] Bad request - message might be too long")
            
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
    
    if fail_count > 0 and success_count == 0:
        print("\n[!] All messages failed!")
        print("\nTROUBLESHOOTING:")
        print("1. Check that your webhook URL is correct")
        print("2. Make sure the webhook hasn't been deleted")
        print("3. Check your internet connection")
        print("4. Try using a different webhook")
        print("\nWebhook URL format:")
        print("https://discord.com/api/webhooks/ID/TOKEN")
    
    input("\nPress Enter to continue...")

if __name__ == "__main__":
    run()
