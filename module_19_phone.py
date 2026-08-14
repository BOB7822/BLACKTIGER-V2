#!/usr/bin/env python3
# Phone Lookup Module - 

import re, sys, os, requests, json, subprocess

def run():
    print("\n" + "="*60)
    print("PHONE LOOKUP")
    print("="*60)
    
    print("[!] Enter phone number with country code")
    print("[!] Examples: +14155552671 (US), +447911123456 (UK)")
    print("[!] Or just enter any phone number")
    print("="*60)
    
    phone = input("\nEnter phone number: ").strip()
    
    if not phone:
        print("No phone number entered")
        input("\nPress Enter to continue...")
        return
    
    print(f"\n[+] Looking up: {phone}")
    print("[+] Gathering information...\n")
    
    # Clean the number
    clean_number = re.sub(r'[^0-9+]', '', phone)
    
    # Check format
    if clean_number.startswith('+'):
        print(f"Format: International - {clean_number}")
    elif clean_number.isdigit():
        print(f"Format: Local - {clean_number}")
    else:
        print(f"Format: Unknown")
    
    print("\n" + "="*60)
    print("LOOKUP RESULTS")
    print("="*60)
    
    # 1. Try WHOIS lookup if available
    print("\n[1] WHOIS Lookup:")
    try:
        result = subprocess.run(['whois', clean_number], capture_output=True, text=True, timeout=5)
        if result.stdout:
            lines = result.stdout.split('\n')[:10]
            for line in lines:
                if ':' in line and not line.startswith('%') and not line.startswith('#'):
                    print(f"    {line}")
    except:
        print("    WHOIS not available")
    
    # 2. Try online lookup services (no API keys)
    print("\n[2] Online Lookup:")
    services = [
        "https://www.freecarrierlookup.com/phone/" + clean_number,
        "https://www.verifyemailaddress.org/phone-validator/phone/" + clean_number
    ]
    
    for url in services:
        try:
            response = requests.get(url, timeout=5, headers={'User-Agent': 'Mozilla/5.0'})
            print(f"    {url[:50]}...: HTTP {response.status_code}")
        except:
            print(f"    {url[:50]}...: Timeout")
    
    # 3. Check carrier info for US numbers
    print("\n[3] Carrier/Country Info:")
    
    # US numbers
    if clean_number.startswith('+1') and len(clean_number) >= 10:
        area_code = clean_number[-10:][:3]
        print(f"    Area Code: {area_code}")
        
        # Area code to state mapping (shortened for brevity)
        area_states = {
            '201': 'New Jersey', '202': 'District of Columbia', '203': 'Connecticut',
            '205': 'Alabama', '206': 'Washington', '207': 'Maine',
            '208': 'Idaho', '209': 'California', '210': 'Texas',
            '212': 'New York', '213': 'California', '214': 'Texas',
            '215': 'Pennsylvania', '216': 'Ohio', '217': 'Illinois',
            '218': 'Minnesota', '219': 'Indiana', '220': 'Ohio',
            '224': 'Illinois', '225': 'Louisiana', '228': 'Mississippi',
            '229': 'Georgia', '231': 'Michigan', '234': 'Ohio',
            '239': 'Florida', '240': 'Maryland', '248': 'Michigan',
            '251': 'Alabama', '252': 'North Carolina', '253': 'Washington',
            '254': 'Texas', '256': 'Alabama', '260': 'Indiana',
            '262': 'Wisconsin', '267': 'Pennsylvania', '269': 'Michigan',
            '270': 'Kentucky', '272': 'Pennsylvania', '276': 'Virginia',
            '281': 'Texas', '283': 'Ohio', '301': 'Maryland',
            '302': 'Delaware', '303': 'Colorado', '304': 'West Virginia',
            '305': 'Florida', '307': 'Wyoming', '308': 'Nebraska',
            '309': 'Illinois', '310': 'California', '312': 'Illinois',
            '313': 'Michigan', '314': 'Missouri', '315': 'New York',
            '316': 'Kansas', '317': 'Indiana', '318': 'Louisiana',
            '319': 'Iowa', '320': 'Minnesota', '321': 'Florida',
            '323': 'California', '325': 'Texas'
        }
        
        if area_code in area_states:
            print(f"    State: {area_states[area_code]}")
        else:
            print(f"    State: Unknown")
    
    # International
    elif clean_number.startswith('+44'):
        print("    Country: United Kingdom")
    elif clean_number.startswith('+61'):
        print("    Country: Australia")
    elif clean_number.startswith('+81'):
        print("    Country: Japan")
    elif clean_number.startswith('+86'):
        print("    Country: China")
    elif clean_number.startswith('+91'):
        print("    Country: India")
    elif clean_number.startswith('+33'):
        print("    Country: France")
    elif clean_number.startswith('+49'):
        print("    Country: Germany")
    elif clean_number.startswith('+39'):
        print("    Country: Italy")
    elif clean_number.startswith('+34'):
        print("    Country: Spain")
    elif clean_number.startswith('+55'):
        print("    Country: Brazil")
    elif clean_number.startswith('+7'):
        print("    Country: Russia")
    elif clean_number.startswith('+82'):
        print("    Country: South Korea")
    elif clean_number.startswith('+31'):
        print("    Country: Netherlands")
    elif clean_number.startswith('+46'):
        print("    Country: Sweden")
    elif clean_number.startswith('+47'):
        print("    Country: Norway")
    elif clean_number.startswith('+45'):
        print("    Country: Denmark")
    elif clean_number.startswith('+358'):
        print("    Country: Finland")
    elif clean_number.startswith('+41'):
        print("    Country: Switzerland")
    elif clean_number.startswith('+43'):
        print("    Country: Austria")
    elif clean_number.startswith('+32'):
        print("    Country: Belgium")
    elif clean_number.startswith('+351'):
        print("    Country: Portugal")
    elif clean_number.startswith('+30'):
        print("    Country: Greece")
    elif clean_number.startswith('+90'):
        print("    Country: Turkey")
    elif clean_number.startswith('+60'):
        print("    Country: Malaysia")
    elif clean_number.startswith('+65'):
        print("    Country: Singapore")
    elif clean_number.startswith('+66'):
        print("    Country: Thailand")
    elif clean_number.startswith('+84'):
        print("    Country: Vietnam")
    elif clean_number.startswith('+63'):
        print("    Country: Philippines")
    elif clean_number.startswith('+62'):
        print("    Country: Indonesia")
    elif clean_number.startswith('+56'):
        print("    Country: Chile")
    elif clean_number.startswith('+54'):
        print("    Country: Argentina")
    elif clean_number.startswith('+52'):
        print("    Country: Mexico")
    elif clean_number.startswith('+27'):
        print("    Country: South Africa")
    elif clean_number.startswith('+971'):
        print("    Country: UAE")
    elif clean_number.startswith('+966'):
        print("    Country: Saudi Arabia")
    elif clean_number.startswith('+1'):
        print("    Country: US/Canada")
    else:
        print("    Country: Unknown")
    
    # 4. Try to get location from IP
    print("\n[4] Location Info:")
    try:
        response = requests.get("http://ip-api.com/json/", timeout=5)
        if response.status_code == 200:
            data = response.json()
            if data.get('status') == 'success':
                print(f"    City: {data.get('city', 'Unknown')}")
                print(f"    Region: {data.get('regionName', 'Unknown')}")
                print(f"    Country: {data.get('country', 'Unknown')}")
                print(f"    ISP: {data.get('isp', 'Unknown')}")
            else:
                print("    Could not get location")
        else:
            print("    Could not get location")
    except:
        print("    Could not get location")
    
    # 5. Check if number is likely mobile or landline
    print("\n[5] Number Type:")
    if clean_number.startswith('+1') and len(clean_number) >= 10:
        mobile_prefixes = ['201', '202', '203', '205', '206', '207', '208', '209', '210',
                          '212', '213', '214', '215', '216', '217', '218', '219', '224',
                          '225', '228', '229', '231', '234', '239', '240', '248', '251',
                          '252', '253', '254', '256', '260', '262', '267', '269', '270',
                          '272', '276', '281', '283', '301', '302', '303', '304', '305',
                          '307', '308', '309', '310', '312', '313', '314', '315', '316',
                          '317', '318', '319', '320', '321', '323', '325']
        area = clean_number[-10:][:3] if len(clean_number) >= 10 else ''
        if area in mobile_prefixes:
            print("    Likely: Mobile")
        else:
            print("    Unknown")
    elif clean_number.startswith('+44') and len(clean_number) >= 11:
        if clean_number[3] == '7':
            print("    Likely: Mobile")
        elif clean_number[3] in ['2', '3']:
            print("    Likely: Landline")
        else:
            print("    Unknown")
    else:
        print("    Unknown")
    
    # 6. Number validity
    print("\n[6] Number Validity:")
    if len(clean_number) >= 10:
        print("    Format: Valid")
    else:
        print("    Format: Invalid (too short)")
    
    # Summary
    print("\n" + "="*60)
    print("SUMMARY")
    print("="*60)
    print(f"Number: {clean_number}")
    print("="*60)
    
    # Direct links for manual lookup
    print("\n[+] Manual lookup links:")
    print(f"    Whitepages: https://www.whitepages.com/phone/{clean_number}")
    print(f"    Spytox: https://www.spytox.com/phone-number-lookup/{clean_number}")
    print(f"    Numverify (API): https://www.numverify.com/")
    print(f"    Twilio Lookup: https://www.twilio.com/lookup")
    
    input("\nPress Enter to continue...")

if __name__ == "__main__":
    run()
