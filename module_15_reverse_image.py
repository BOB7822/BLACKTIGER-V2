#!/usr/bin/env python3
# Reverse Image Search Module

import requests, base64

def run():
    print("\n" + "="*60)
    print("REVERSE IMAGE SEARCH")
    print("="*60)
    
    image_input = input("Image URL or file path: ").strip()
    
    if not image_input.startswith('http'):
        try:
            with open(image_input, 'rb') as f:
                image_data = base64.b64encode(f.read()).decode()
            print("File loaded")
        except:
            print("Could not load file")
            return
    else:
        try:
            response = requests.get(image_input, timeout=10)
            image_data = base64.b64encode(response.content).decode()
            print("URL loaded")
        except:
            print("Could not load URL")
            return
    
    print("Search URL: https://www.google.com/searchbyimage?image_url=" + image_input)
    print("TinEye: https://tineye.com/search?url=" + image_input)

if __name__ == "__main__":
    run()