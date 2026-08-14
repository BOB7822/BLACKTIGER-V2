#!/usr/bin/env python3
# Social Media OSINT n

import requests, time, re, json, sys

def run():
    print("\n" + "="*60)
    print("SOCIAL MEDIA OSINT")
    print("="*60)
    
    username = input("Enter username to search: ").strip()
    
    if not username:
        print("No username entered")
        input("\nPress Enter to continue...")
        return
    
    print(f"\n[+] Searching for: {username}")
    print("[+] Checking social media platforms...\n")
    print("="*60)
    
    found = []
    not_found = []
    errors = []
    
    # Platform configurations with proper URLs and detection methods
    platforms = {
        'Instagram': {
            'url': f'https://www.instagram.com/{username}/',
            'detect': '200',
            'method': 'status'
        },
        'Twitter': {
            'url': f'https://twitter.com/{username}',
            'detect': '200',
            'method': 'status'
        },
        'Facebook': {
            'url': f'https://www.facebook.com/{username}',
            'detect': '200',
            'method': 'status'
        },
        'YouTube': {
            'url': f'https://www.youtube.com/@{username}',
            'detect': '200',
            'method': 'status'
        },
        'TikTok': {
            'url': f'https://www.tiktok.com/@{username}',
            'detect': '200',
            'method': 'status'
        },
        'Reddit': {
            'url': f'https://www.reddit.com/user/{username}',
            'detect': '200',
            'method': 'status'
        },
        'GitHub': {
            'url': f'https://github.com/{username}',
            'detect': '200',
            'method': 'status'
        },
        'Twitch': {
            'url': f'https://www.twitch.tv/{username}',
            'detect': '200',
            'method': 'status'
        },
        'Snapchat': {
            'url': f'https://www.snapchat.com/add/{username}',
            'detect': '200',
            'method': 'status'
        },
        'Telegram': {
            'url': f'https://t.me/{username}',
            'detect': '200',
            'method': 'status'
        },
        'LinkedIn': {
            'url': f'https://www.linkedin.com/in/{username}',
            'detect': '200',
            'method': 'status'
        },
        'Pinterest': {
            'url': f'https://www.pinterest.com/{username}/',
            'detect': '200',
            'method': 'status'
        },
        'Tumblr': {
            'url': f'https://{username}.tumblr.com',
            'detect': '200',
            'method': 'status'
        },
        'Spotify': {
            'url': f'https://open.spotify.com/user/{username}',
            'detect': '200',
            'method': 'status'
        },
        'Steam': {
            'url': f'https://steamcommunity.com/id/{username}',
            'detect': '200',
            'method': 'status'
        },
        'Vimeo': {
            'url': f'https://vimeo.com/{username}',
            'detect': '200',
            'method': 'status'
        },
        'SoundCloud': {
            'url': f'https://soundcloud.com/{username}',
            'detect': '200',
            'method': 'status'
        },
        'Dribbble': {
            'url': f'https://dribbble.com/{username}',
            'detect': '200',
            'method': 'status'
        },
        'Behance': {
            'url': f'https://www.behance.net/{username}',
            'detect': '200',
            'method': 'status'
        },
        'Patreon': {
            'url': f'https://www.patreon.com/{username}',
            'detect': '200',
            'method': 'status'
        },
        'Medium': {
            'url': f'https://medium.com/@{username}',
            'detect': '200',
            'method': 'status'
        },
        'GitLab': {
            'url': f'https://gitlab.com/{username}',
            'detect': '200',
            'method': 'status'
        },
        'Keybase': {
            'url': f'https://keybase.io/{username}',
            'detect': '200',
            'method': 'status'
        },
        'Flickr': {
            'url': f'https://www.flickr.com/people/{username}/',
            'detect': '200',
            'method': 'status'
        },
        'DeviantArt': {
            'url': f'https://www.deviantart.com/{username}',
            'detect': '200',
            'method': 'status'
        },
        'Etsy': {
            'url': f'https://www.etsy.com/shop/{username}',
            'detect': '200',
            'method': 'status'
        },
        'WordPress': {
            'url': f'https://{username}.wordpress.com',
            'detect': '200',
            'method': 'status'
        },
        'VK': {
            'url': f'https://vk.com/{username}',
            'detect': '200',
            'method': 'status'
        },
        'Imgur': {
            'url': f'https://imgur.com/user/{username}',
            'detect': '200',
            'method': 'status'
        },
        'Poshmark': {
            'url': f'https://poshmark.com/closet/{username}',
            'detect': '200',
            'method': 'status'
        },
        'ReverbNation': {
            'url': f'https://www.reverbnation.com/{username}',
            'detect': '200',
            'method': 'status'
        },
        'Bandcamp': {
            'url': f'https://bandcamp.com/{username}',
            'detect': '200',
            'method': 'status'
        },
        'Mixcloud': {
            'url': f'https://www.mixcloud.com/{username}/',
            'detect': '200',
            'method': 'status'
        },
        'AskFM': {
            'url': f'https://ask.fm/{username}',
            'detect': '200',
            'method': 'status'
        },
        'Vine': {
            'url': f'https://vine.co/u/{username}',
            'detect': '200',
            'method': 'status'
        },
        'Periscope': {
            'url': f'https://www.periscope.tv/{username}',
            'detect': '200',
            'method': 'status'
        }
    }
    
    # Check each platform
    for platform, config in platforms.items():
        try:
            # Send request with proper headers
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                'Accept-Language': 'en-US,en;q=0.5',
                'Accept-Encoding': 'gzip, deflate, br',
                'Connection': 'keep-alive',
                'Upgrade-Insecure-Requests': '1'
            }
            
            response = requests.get(config['url'], timeout=8, headers=headers, allow_redirects=True)
            
            # Check if found
            if response.status_code == 200:
                # Additional check for some platforms that return 200 even when not found
                found_platform = True
                
                # Special checks for specific platforms
                if platform == 'Instagram':
                    if 'Page Not Found' in response.text or 'Sorry, this page isn\'t available' in response.text:
                        found_platform = False
                
                if platform == 'Twitter':
                    if 'This account doesn’t exist' in response.text or 'Page not found' in response.text:
                        found_platform = False
                
                if platform == 'TikTok':
                    if 'Couldn\'t find this account' in response.text or 'User not found' in response.text:
                        found_platform = False
                
                if platform == 'YouTube':
                    if 'This channel does not exist' in response.text or '404' in response.text:
                        found_platform = False
                
                if platform == 'Reddit':
                    if 'page not found' in response.text.lower() or 'there doesn\'t seem to be anything here' in response.text:
                        found_platform = False
                
                if platform == 'GitHub':
                    if 'Page not found' in response.text or 'There is no account' in response.text:
                        found_platform = False
                
                if platform == 'LinkedIn':
                    if 'This profile does not exist' in response.text or 'Page not found' in response.text:
                        found_platform = False
                
                if platform == 'Twitch':
                    if 'Sorry. Unless you’ve got a time machine' in response.text or 'Channel not found' in response.text:
                        found_platform = False
                
                if found_platform:
                    print(f"  [FOUND] {platform}: {config['url']}")
                    found.append(platform)
                else:
                    print(f"  [NOT FOUND] {platform}")
                    not_found.append(platform)
                    
            elif response.status_code == 404:
                print(f"  [NOT FOUND] {platform}")
                not_found.append(platform)
            else:
                # Some platforms return 302 redirects for valid profiles
                if response.status_code in [301, 302]:
                    print(f"  [FOUND] {platform}: {config['url']}")
                    found.append(platform)
                else:
                    print(f"  [ERROR] {platform}: HTTP {response.status_code}")
                    errors.append(platform)
                    
        except requests.exceptions.Timeout:
            print(f"  [TIMEOUT] {platform}")
            errors.append(platform)
        except requests.exceptions.ConnectionError:
            print(f"  [CONNECTION ERROR] {platform}")
            errors.append(platform)
        except Exception as e:
            print(f"  [ERROR] {platform}: {str(e)[:50]}")
            errors.append(platform)
        
        # Small delay to avoid rate limiting
        time.sleep(0.1)
    
    # Summary
    print("\n" + "="*60)
    print("SUMMARY")
    print("="*60)
    print(f"Found on: {len(found)} platforms")
    if found:
        print("\nPlatforms found:")
        for platform in found[:10]:
            print(f"  - {platform}")
        if len(found) > 10:
            print(f"  ... and {len(found)-10} more")
    
    print(f"\nNot found: {len(not_found)} platforms")
    print(f"Errors: {len(errors)} platforms")
    
    # Save results
    try:
        out_dir = os.path.expanduser("~/Downloads/BlackTiger_Output")
        os.makedirs(out_dir, exist_ok=True)
        path = os.path.join(out_dir, f"social_{username}.txt")
        with open(path, 'w') as f:
            f.write(f"Social Media OSINT Results for: {username}\n")
            f.write("="*50 + "\n\n")
            f.write(f"Found on {len(found)} platforms:\n")
            for platform in found:
                # Get the URL for this platform
                for p, config in platforms.items():
                    if p == platform:
                        f.write(f"  {platform}: {config['url']}\n")
                        break
    except:
        pass
    
    print(f"\n[+] Results saved to: ~/Downloads/BlackTiger_Output/social_{username}.txt")
    
    print("\n" + "="*60)
    input("Press Enter to continue...")

if __name__ == "__main__":
    run()
