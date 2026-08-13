#!/usr/bin/env python3
# Instagram Info Module

import requests, json

def run():
    print("\n" + "="*60)
    print("INSTAGRAM INFO")
    print("="*60)
    
    user = input("Username: ").strip()
    
    try:
        r = requests.get(f"https://www.instagram.com/{user}/?__a=1", timeout=10)
        if r.status_code == 200:
            data = r.json()
            u = data.get('graphql', {}).get('user', {})
            profile = {
                'Username': u.get('username'),
                'Posts': u.get('edge_owner_to_timeline_media', {}).get('count'),
                'Followers': u.get('edge_followed_by', {}).get('count'),
                'Following': u.get('edge_follow', {}).get('count'),
                'Bio': u.get('biography', ''),
                'Full Name': u.get('full_name', '')
            }
            print(json.dumps(profile, indent=2))
        else:
            print("Not found")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    run()