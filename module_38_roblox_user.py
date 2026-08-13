#!/usr/bin/env python3
# Roblox User Info Module - Working Version

import requests, json, time, sys

def run():
    print("\n" + "="*60)
    print("ROBLOX USER INFO")
    print("="*60)
    
    username = input("Enter Roblox username: ").strip()
    
    if not username:
        print("No username entered")
        input("\nPress Enter to continue...")
        return
    
    print(f"\n[+] Looking up: {username}")
    print("[+] Searching Roblox API...")
    
    try:
        # Search for user by username
        url = f"https://users.roblox.com/v1/users/search?keyword={username}&limit=10"
        response = requests.get(url, timeout=10)
        
        if response.status_code == 200:
            data = response.json()
            
            if data.get('data') and len(data['data']) > 0:
                print("\n" + "="*60)
                print("USER FOUND!")
                print("="*60)
                
                # Show all matching users
                for i, user in enumerate(data['data'][:5]):
                    print(f"\n[{i+1}] User Info:")
                    print(f"  ID: {user.get('id', 'Unknown')}")
                    print(f"  Name: {user.get('name', 'Unknown')}")
                    print(f"  Display Name: {user.get('displayName', 'Unknown')}")
                    print(f"  Has Verified Badge: {user.get('hasVerifiedBadge', False)}")
                    
                    # Get more details from user ID
                    user_id = user.get('id')
                    if user_id:
                        try:
                            detail_url = f"https://users.roblox.com/v1/users/{user_id}"
                            detail_response = requests.get(detail_url, timeout=10)
                            if detail_response.status_code == 200:
                                detail_data = detail_response.json()
                                print(f"  Description: {detail_data.get('description', 'None')[:100]}...")
                                print(f"  Created: {detail_data.get('created', 'Unknown')}")
                                print(f"  Is Banned: {detail_data.get('isBanned', False)}")
                        except:
                            pass
                        
                        # Get profile picture
                        try:
                            avatar_url = f"https://thumbnails.roblox.com/v1/users/avatar?userIds={user_id}&size=48x48&format=Png"
                            avatar_response = requests.get(avatar_url, timeout=10)
                            if avatar_response.status_code == 200:
                                avatar_data = avatar_response.json()
                                if avatar_data.get('data'):
                                    print(f"  Avatar: {avatar_data['data'][0].get('imageUrl', 'N/A')}")
                        except:
                            pass
                        
                        # Get Roblox profile link
                        print(f"  Profile: https://www.roblox.com/users/{user_id}/profile")
                
                print("\n" + "="*60)
                print(f"Total users found: {len(data.get('data', []))}")
                print("="*60)
                
            else:
                print("\n[!] No users found with that username")
                print("Try checking the spelling or try a different username")
                
        elif response.status_code == 429:
            print("\n[!] Rate limited. Please wait a moment and try again.")
        else:
            print(f"\n[!] Error: HTTP {response.status_code}")
            
    except requests.exceptions.Timeout:
        print("\n[!] Request timed out. Please try again.")
    except requests.exceptions.ConnectionError:
        print("\n[!] Connection error. Check your internet connection.")
    except Exception as e:
        print(f"\n[!] Error: {e}")
    
    input("\nPress Enter to continue...")

if __name__ == "__main__":
    run()
