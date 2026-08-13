#!/usr/bin/env python3
# IP Geolocation Module

import requests, json

def run():
    print("\n" + "="*60)
    print("IP GEOLOCATION")
    print("="*60)
    
    ip = input("IP address (or 'me' for your IP): ").strip()
    
    if ip.lower() == 'me':
        try:
            r = requests.get('https://api.ipify.org?format=json', timeout=5)
            ip = r.json()['ip']
            print(f"Your IP: {ip}")
        except:
            print("Could not get your IP")
            return
    
    print(f"\nLooking up: {ip}")
    
    try:
        r = requests.get(f"http://ip-api.com/json/{ip}?fields=status,country,regionName,city,zip,lat,lon,timezone,isp,org,as,query", timeout=8)
        if r.status_code == 200:
            data = r.json()
            if data.get('status') != 'fail':
                print(f"IP: {data.get('query', ip)}")
                print(f"Country: {data.get('country', 'Unknown')}")
                print(f"Region: {data.get('regionName', 'Unknown')}")
                print(f"City: {data.get('city', 'Unknown')}")
                print(f"Postal: {data.get('zip', 'Unknown')}")
                print(f"Latitude: {data.get('lat', 'Unknown')}")
                print(f"Longitude: {data.get('lon', 'Unknown')}")
                print(f"Timezone: {data.get('timezone', 'Unknown')}")
                print(f"ISP: {data.get('isp', 'Unknown')}")
                print(f"Organization: {data.get('org', 'Unknown')}")
                if data.get('lat') and data.get('lon'):
                    print(f"Google Maps: https://maps.google.com/maps?q={data['lat']},{data['lon']}")
            else:
                print("Geolocation failed")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    run()