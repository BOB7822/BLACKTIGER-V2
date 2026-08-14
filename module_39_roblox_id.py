#!/usr/bin/env python3
# Roblox ID Info 

import requests, json, sys, os

def run():
    print("\n" + "="*60)
    print("ROBLOX ID INFO")
    print("="*60)
    
    print("[!] Enter a Roblox User ID to lookup")
    print("[!] Example: 123456789")
    print("="*60)
    
    uid = input("\nEnter Roblox User ID: ").strip()
    
    if not uid:
        print("No ID entered")
        input("\nPress Enter to continue...")
        return
    
    print(f"\n[+] Looking up User ID: {uid}")
    print("[+] Searching Roblox API...\n")
    
    try:
        # Get user info
        url = f"https://users.roblox.com/v1/users/{uid}"
        response = requests.get(url, timeout=10)
        
        if response.status_code == 200:
            data = response.json()
            
            print("="*60)
            print("USER INFORMATION")
            print("="*60)
            print(f"ID: {data.get('id', 'Unknown')}")
            print(f"Username: {data.get('name', 'Unknown')}")
            print(f"Display Name: {data.get('displayName', 'Unknown')}")
            print(f"Description: {data.get('description', 'None')[:200]}")
            print(f"Created: {data.get('created', 'Unknown')}")
            print(f"Is Banned: {data.get('isBanned', False)}")
            
            # Get profile picture
            print("\n" + "="*60)
            print("PROFILE PICTURE")
            print("="*60)
            try:
                avatar_url = f"https://thumbnails.roblox.com/v1/users/avatar?userIds={uid}&size=48x48&format=Png"
                avatar_response = requests.get(avatar_url, timeout=10)
                if avatar_response.status_code == 200:
                    avatar_data = avatar_response.json()
                    if avatar_data.get('data'):
                        print(f"Avatar URL: {avatar_data['data'][0].get('imageUrl', 'N/A')}")
                    else:
                        print("No avatar found")
            except:
                print("Could not get avatar")
            
            # Get profile link
            print("\n" + "="*60)
            print("PROFILE LINK")
            print("="*60)
            print(f"https://www.roblox.com/users/{uid}/profile")
            
            # Get groups
            print("\n" + "="*60)
            print("GROUPS")
            print("="*60)
            try:
                groups_url = f"https://groups.roblox.com/v2/users/{uid}/groups/roles"
                groups_response = requests.get(groups_url, timeout=10)
                if groups_response.status_code == 200:
                    groups_data = groups_response.json()
                    groups = groups_data.get('data', [])
                    if groups:
                        for group in groups[:5]:
                            group_obj = group.get('group', {})
                            print(f"  - {group_obj.get('name', 'Unknown')} (ID: {group_obj.get('id', 'Unknown')})")
                        if len(groups) > 5:
                            print(f"  ... and {len(groups)-5} more groups")
                    else:
                        print("  No groups found")
                else:
                    print("  Could not get groups")
            except:
                print("  Could not get groups")
            
            # Get friends count
            print("\n" + "="*60)
            print("FRIENDS")
            print("="*60)
            try:
                friends_url = f"https://friends.roblox.com/v1/users/{uid}/friends/count"
                friends_response = requests.get(friends_url, timeout=10)
                if friends_response.status_code == 200:
                    friends_data = friends_response.json()
                    print(f"Friends Count: {friends_data.get('count', 0)}")
                else:
                    print("  Could not get friends count")
            except:
                print("  Could not get friends count")
            
            # Get followers count
            print("\n" + "="*60)
            print("FOLLOWERS")
            print("="*60)
            try:
                followers_url = f"https://friends.roblox.com/v1/users/{uid}/followers/count"
                followers_response = requests.get(followers_url, timeout=10)
                if followers_response.status_code == 200:
                    followers_data = followers_response.json()
                    print(f"Followers Count: {followers_data.get('count', 0)}")
                else:
                    print("  Could not get followers count")
            except:
                print("  Could not get followers count")
            
        elif response.status_code == 404:
            print("[!] User not found")
            print("The ID you entered does not exist")
        else:
            print(f"[!] Error: HTTP {response.status_code}")
            
    except requests.exceptions.Timeout:
        print("[!] Request timed out. Please try again.")
    except requests.exceptions.ConnectionError:
        print("[!] Connection error. Check your internet connection.")
    except Exception as e:
        print(f"[!] Error: {e}")
    
    input("\nPress Enter to continue...")

if __name__ == "__main__":
    run()
