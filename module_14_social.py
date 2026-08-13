#!/usr/bin/env python3
# Social Media OSINT Module

import requests, time

def run():
    print("\n" + "="*60)
    print("SOCIAL MEDIA OSINT")
    print("="*60)
    
    username = input("Username: ").strip()
    
    platforms = {
        'Instagram': f'https://www.instagram.com/{username}/',
        'Twitter': f'https://twitter.com/{username}',
        'Facebook': f'https://facebook.com/{username}',
        'YouTube': f'https://youtube.com/@{username}',
        'TikTok': f'https://tiktok.com/@{username}',
        'Reddit': f'https://reddit.com/user/{username}',
        'GitHub': f'https://github.com/{username}',
        'Twitch': f'https://twitch.tv/{username}',
        'Snapchat': f'https://snapchat.com/add/{username}',
        'Telegram': f'https://t.me/{username}',
        'LinkedIn': f'https://linkedin.com/in/{username}'
    }
    
    print(f"\nSearching for {username}...\n")
    found = []
    
    for platform, url in platforms.items():
        try:
            response = requests.get(url, timeout=5)
            if response.status_code == 200:
                print(f"[FOUND] {platform}: {url}")
                found.append(platform)
            elif response.status_code == 404:
                print(f"[NOT FOUND] {platform}")
            else:
                print(f"[?] {platform}: Status {response.status_code}")
        except:
            print(f"[?] {platform}: Timeout")
        time.sleep(0.3)
    
    print(f"\nFound on {len(found)} platforms")

if __name__ == "__main__":
    run()