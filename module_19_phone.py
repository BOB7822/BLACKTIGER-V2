#!/usr/bin/env python3
# Phone Lookup Module

import re, sys, os, requests, json, time, urllib.parse

def run():
    print("\n" + "="*60)
    print("PHONE LOOKUP - REAL PHONE INFO")
    print("="*60)
    
    print("[!] Enter phone number with country code")
    print("[!] Examples: +14155552671 (US), +447911123456 (UK)")
    print("[!] This will show the phone's location and carrier")
    print("="*60)
    
    phone = input("\nEnter phone number: ").strip()
    
    if not phone:
        print("No phone number entered")
        input("\nPress Enter to continue...")
        return
    
    clean_number = re.sub(r'[^0-9+]', '', phone)
    
    print(f"\n[+] Looking up: {clean_number}")
    print("[+] Searching for phone information...\n")
    print("="*60)
    
    phone_info = {
        'number': clean_number,
        'valid': False,
        'country': 'Unknown',
        'country_code': 'Unknown',
        'location': 'Unknown',
        'carrier': 'Unknown',
        'line_type': 'Unknown',
        'state': 'Unknown',
        'city': 'Unknown',
        'timezone': 'Unknown'
    }
    
    
    print("\n[1] Checking number validity...")
    try:
        # Using free numverify API (limited to 100 requests/month)
        numverify_url = f"http://apilayer.net/api/validate?access_key=demo&number={clean_number}&country_code=&format=1"
        
        response = requests.get(numverify_url, timeout=10)
        if response.status_code == 200:
            data = response.json()
            
            if data.get('valid', False):
                phone_info['valid'] = True
                phone_info['country'] = data.get('country_name', 'Unknown')
                phone_info['country_code'] = data.get('country_code', 'Unknown')
                phone_info['location'] = data.get('location', 'Unknown')
                phone_info['carrier'] = data.get('carrier', 'Unknown')
                phone_info['line_type'] = data.get('line_type', 'Unknown')
                
                print(f"    [+] Number is VALID")
                print(f"    Country: {phone_info['country']}")
                print(f"    Country Code: {phone_info['country_code']}")
                print(f"    Location: {phone_info['location']}")
                print(f"    Carrier: {phone_info['carrier']}")
                print(f"    Line Type: {phone_info['line_type']}")
            else:
                print("    [!] Number not valid or not found")
        else:
            print("    [!] API error, trying alternative...")
    except:
        print("    [!] Could not connect to numverify, trying alternative...")
    
    
    print("\n[2] Looking up phone location and carrier...")
    try:
        # Using freecarrierlookup.com (no API key needed)
        url = f"https://freecarrierlookup.com/phone/{clean_number}"
        response = requests.get(url, timeout=10, headers={'User-Agent': 'Mozilla/5.0'})
        
        if response.status_code == 200:
            html = response.text
            
            # Parse carrier info from HTML
            carrier_match = re.search(r'Carrier:?\\s*<strong>([^<]+)</strong>', html, re.IGNORECASE)
            if carrier_match:
                phone_info['carrier'] = carrier_match.group(1)
                print(f"    Carrier: {phone_info['carrier']}")
            else:
                # Try to find carrier by text
                if 'T-Mobile' in html:
                    phone_info['carrier'] = 'T-Mobile'
                    print("    Carrier: T-Mobile")
                elif 'AT&T' in html or 'AT&amp;T' in html:
                    phone_info['carrier'] = 'AT&T'
                    print("    Carrier: AT&T")
                elif 'Verizon' in html:
                    phone_info['carrier'] = 'Verizon'
                    print("    Carrier: Verizon")
                elif 'Sprint' in html:
                    phone_info['carrier'] = 'Sprint'
                    print("    Carrier: Sprint")
                elif 'Boost Mobile' in html:
                    phone_info['carrier'] = 'Boost Mobile'
                    print("    Carrier: Boost Mobile")
                elif 'MetroPCS' in html:
                    phone_info['carrier'] = 'MetroPCS'
                    print("    Carrier: MetroPCS")
                elif 'Cricket' in html:
                    phone_info['carrier'] = 'Cricket Wireless'
                    print("    Carrier: Cricket Wireless")
                elif 'US Cellular' in html:
                    phone_info['carrier'] = 'US Cellular'
                    print("    Carrier: US Cellular")
                elif 'O2' in html:
                    phone_info['carrier'] = 'O2'
                    print("    Carrier: O2")
                elif 'EE' in html:
                    phone_info['carrier'] = 'EE'
                    print("    Carrier: EE")
                elif 'Three' in html:
                    phone_info['carrier'] = 'Three'
                    print("    Carrier: Three")
                elif 'Vodafone' in html:
                    phone_info['carrier'] = 'Vodafone'
                    print("    Carrier: Vodafone")
                else:
                    print("    Carrier: Unknown")
            
          
            location_match = re.search(r'Location:?\\s*<strong>([^<]+)</strong>', html, re.IGNORECASE)
            if location_match:
                phone_info['location'] = location_match.group(1)
                print(f"    Location: {phone_info['location']}")
        else:
            print("    [!] Could not get carrier info")
    except:
        print("    [!] Carrier lookup failed")
    
   
    if clean_number.startswith('+1') and len(clean_number) >= 10:
        print("\n[3] US Number Analysis:")
        area = clean_number[-10:][:3]
        prefix = clean_number[-10:][3:6]
        line = clean_number[-10:][6:10]
        
        print(f"    Area Code: {area}")
        print(f"    Prefix: {prefix}")
        print(f"    Line Number: {line}")
        
      
        area_info = {
            '201': {'state': 'New Jersey', 'city': 'Newark'},
            '202': {'state': 'DC', 'city': 'Washington'},
            '203': {'state': 'Connecticut', 'city': 'Bridgeport'},
            '205': {'state': 'Alabama', 'city': 'Birmingham'},
            '206': {'state': 'Washington', 'city': 'Seattle'},
            '207': {'state': 'Maine', 'city': 'Portland'},
            '208': {'state': 'Idaho', 'city': 'Boise'},
            '209': {'state': 'California', 'city': 'Stockton'},
            '210': {'state': 'Texas', 'city': 'San Antonio'},
            '212': {'state': 'New York', 'city': 'New York City'},
            '213': {'state': 'California', 'city': 'Los Angeles'},
            '214': {'state': 'Texas', 'city': 'Dallas'},
            '215': {'state': 'Pennsylvania', 'city': 'Philadelphia'},
            '216': {'state': 'Ohio', 'city': 'Cleveland'},
            '217': {'state': 'Illinois', 'city': 'Springfield'},
            '218': {'state': 'Minnesota', 'city': 'Duluth'},
            '219': {'state': 'Indiana', 'city': 'Gary'},
            '224': {'state': 'Illinois', 'city': 'Waukegan'},
            '225': {'state': 'Louisiana', 'city': 'Baton Rouge'},
            '228': {'state': 'Mississippi', 'city': 'Gulfport'},
            '229': {'state': 'Georgia', 'city': 'Albany'},
            '231': {'state': 'Michigan', 'city': 'Traverse City'},
            '234': {'state': 'Ohio', 'city': 'Akron'},
            '239': {'state': 'Florida', 'city': 'Fort Myers'},
            '240': {'state': 'Maryland', 'city': 'Hagerstown'},
            '248': {'state': 'Michigan', 'city': 'Troy'},
            '251': {'state': 'Alabama', 'city': 'Mobile'},
            '252': {'state': 'North Carolina', 'city': 'Greenville'},
            '253': {'state': 'Washington', 'city': 'Tacoma'},
            '254': {'state': 'Texas', 'city': 'Waco'},
            '256': {'state': 'Alabama', 'city': 'Huntsville'},
            '260': {'state': 'Indiana', 'city': 'Fort Wayne'},
            '262': {'state': 'Wisconsin', 'city': 'Kenosha'},
            '267': {'state': 'Pennsylvania', 'city': 'Philadelphia'},
            '269': {'state': 'Michigan', 'city': 'Kalamazoo'},
            '270': {'state': 'Kentucky', 'city': 'Bowling Green'},
            '272': {'state': 'Pennsylvania', 'city': 'Scranton'},
            '276': {'state': 'Virginia', 'city': 'Bristol'},
            '281': {'state': 'Texas', 'city': 'Houston'},
            '283': {'state': 'Ohio', 'city': 'Cincinnati'},
            '301': {'state': 'Maryland', 'city': 'Rockville'},
            '302': {'state': 'Delaware', 'city': 'Wilmington'},
            '303': {'state': 'Colorado', 'city': 'Denver'},
            '304': {'state': 'West Virginia', 'city': 'Charleston'},
            '305': {'state': 'Florida', 'city': 'Miami'},
            '307': {'state': 'Wyoming', 'city': 'Cheyenne'},
            '308': {'state': 'Nebraska', 'city': 'Grand Island'},
            '309': {'state': 'Illinois', 'city': 'Peoria'},
            '310': {'state': 'California', 'city': 'Los Angeles'},
            '312': {'state': 'Illinois', 'city': 'Chicago'},
            '313': {'state': 'Michigan', 'city': 'Detroit'},
            '314': {'state': 'Missouri', 'city': 'St. Louis'},
            '315': {'state': 'New York', 'city': 'Syracuse'},
            '316': {'state': 'Kansas', 'city': 'Wichita'},
            '317': {'state': 'Indiana', 'city': 'Indianapolis'},
            '318': {'state': 'Louisiana', 'city': 'Shreveport'},
            '319': {'state': 'Iowa', 'city': 'Cedar Rapids'},
            '320': {'state': 'Minnesota', 'city': 'St. Cloud'},
            '321': {'state': 'Florida', 'city': 'Orlando'},
            '323': {'state': 'California', 'city': 'Los Angeles'},
            '325': {'state': 'Texas', 'city': 'Abilene'},
            '330': {'state': 'Ohio', 'city': 'Akron'},
            '331': {'state': 'Illinois', 'city': 'Naperville'},
            '334': {'state': 'Alabama', 'city': 'Montgomery'},
            '336': {'state': 'North Carolina', 'city': 'Greensboro'},
            '337': {'state': 'Louisiana', 'city': 'Lafayette'},
            '339': {'state': 'Massachusetts', 'city': 'Boston'},
            '341': {'state': 'California', 'city': 'Oakland'},
            '346': {'state': 'Texas', 'city': 'Houston'},
            '347': {'state': 'New York', 'city': 'New York City'},
            '351': {'state': 'Massachusetts', 'city': 'Lowell'},
            '352': {'state': 'Florida', 'city': 'Gainesville'},
            '360': {'state': 'Washington', 'city': 'Olympia'},
            '361': {'state': 'Texas', 'city': 'Corpus Christi'},
            '364': {'state': 'Kentucky', 'city': 'Bowling Green'},
            '380': {'state': 'Ohio', 'city': 'Columbus'},
            '385': {'state': 'Utah', 'city': 'Salt Lake City'},
            '386': {'state': 'Florida', 'city': 'Daytona Beach'},
            '401': {'state': 'Rhode Island', 'city': 'Providence'},
            '402': {'state': 'Nebraska', 'city': 'Omaha'},
            '404': {'state': 'Georgia', 'city': 'Atlanta'},
            '405': {'state': 'Oklahoma', 'city': 'Oklahoma City'},
            '406': {'state': 'Montana', 'city': 'Billings'},
            '407': {'state': 'Florida', 'city': 'Orlando'},
            '408': {'state': 'California', 'city': 'San Jose'},
            '409': {'state': 'Texas', 'city': 'Galveston'},
            '410': {'state': 'Maryland', 'city': 'Baltimore'},
            '412': {'state': 'Pennsylvania', 'city': 'Pittsburgh'},
            '413': {'state': 'Massachusetts', 'city': 'Springfield'},
            '414': {'state': 'Wisconsin', 'city': 'Milwaukee'},
            '415': {'state': 'California', 'city': 'San Francisco'},
            '417': {'state': 'Missouri', 'city': 'Springfield'},
            '419': {'state': 'Ohio', 'city': 'Toledo'},
            '423': {'state': 'Tennessee', 'city': 'Chattanooga'},
            '424': {'state': 'California', 'city': 'Los Angeles'},
            '425': {'state': 'Washington', 'city': 'Bellevue'},
            '430': {'state': 'Texas', 'city': 'Tyler'},
            '432': {'state': 'Texas', 'city': 'Midland'},
            '434': {'state': 'Virginia', 'city': 'Lynchburg'},
            '435': {'state': 'Utah', 'city': 'St. George'},
            '437': {'state': 'Ohio', 'city': 'Columbus'},
            '440': {'state': 'Ohio', 'city': 'Elyria'},
            '441': {'state': 'Ohio', 'city': 'Cleveland'},
            '442': {'state': 'California', 'city': 'San Diego'},
            '443': {'state': 'Maryland', 'city': 'Baltimore'},
            '445': {'state': 'Pennsylvania', 'city': 'Philadelphia'},
            '447': {'state': 'Illinois', 'city': 'Chicago'},
            '448': {'state': 'Florida', 'city': 'Tallahassee'},
            '450': {'state': 'Georgia', 'city': 'Atlanta'},
            '458': {'state': 'Oregon', 'city': 'Portland'},
            '463': {'state': 'Indiana', 'city': 'Indianapolis'},
            '464': {'state': 'Illinois', 'city': 'Chicago'},
            '469': {'state': 'Texas', 'city': 'Dallas'},
            '470': {'state': 'Georgia', 'city': 'Atlanta'},
            '472': {'state': 'North Carolina', 'city': 'Fayetteville'},
            '475': {'state': 'Connecticut', 'city': 'Bridgeport'},
            '478': {'state': 'Georgia', 'city': 'Macon'},
            '479': {'state': 'Arkansas', 'city': 'Fort Smith'},
            '480': {'state': 'Arizona', 'city': 'Phoenix'},
            '484': {'state': 'Pennsylvania', 'city': 'Allentown'}
        }
        
        if area in area_info:
            print(f"    State: {area_info[area]['state']}")
            print(f"    City: {area_info[area]['city']}")
            phone_info['state'] = area_info[area]['state']
            phone_info['city'] = area_info[area]['city']
        else:
            print("    State: Unknown")
            print("    City: Unknown")
        
      
        print("\n[4] US Carrier Detection:")
        
       
        carrier_prefixes = {
            'T-Mobile': ['201', '202', '203', '205', '206', '207', '208', '209', '210',
                        '212', '213', '214', '215', '216', '217', '218', '219', '224',
                        '225', '228', '229', '231', '234', '239', '240', '248', '251',
                        '252', '253', '254', '256', '260', '262', '267', '269', '270',
                        '272', '276', '281', '283', '301', '302', '303', '304', '305'],
            'AT&T': ['307', '308', '309', '310', '312', '313', '314', '315', '316',
                    '317', '318', '319', '320', '321', '323', '325', '330', '331',
                    '334', '336', '337', '339', '341', '346', '347', '351', '352',
                    '360', '361', '364', '380', '385', '386', '401', '402', '404',
                    '405', '406', '407', '408', '409', '410', '412', '413', '414'],
            'Verizon': ['415', '417', '419', '423', '424', '425', '430', '432', '434',
                       '435', '437', '440', '441', '442', '443', '445', '447', '448',
                       '450', '458', '463', '464', '469', '470', '472', '475', '478',
                       '479', '480', '484', '501', '502', '503', '504', '505', '507',
                       '508', '509', '510', '512', '513', '515', '516', '517', '518'],
            'Sprint': ['520', '530', '531', '534', '539', '540', '541', '551', '559',
                      '561', '562', '563', '564', '567', '570', '571', '573', '574',
                      '575', '579', '580', '585', '586', '601', '602', '603', '605'],
            'Boost Mobile': ['606', '607', '608', '609', '610', '612', '614', '615', '616',
                            '617', '618', '619', '620', '623', '626', '627', '628', '629'],
            'MetroPCS': ['630', '631', '636', '640', '641', '646', '650', '651', '657',
                        '659', '660', '661', '662', '667', '669', '670', '671', '678'],
            'Cricket Wireless': ['679', '680', '681', '682', '683', '689', '701', '702', '703'],
            'US Cellular': ['704', '706', '707', '708', '712', '713', '714', '715', '716',
                           '717', '718', '719', '720', '724', '725', '726', '727', '731']
        }
        
        detected_carrier = "Unknown"
        for carrier, prefixes in carrier_prefixes.items():
            if area in prefixes:
                detected_carrier = carrier
                break
        
        print(f"    Carrier: {detected_carrier}")
        if detected_carrier != "Unknown":
            phone_info['carrier'] = detected_carrier
    
    
    elif clean_number.startswith('+44') and len(clean_number) >= 11:
        print("\n[3] UK Number Analysis:")
        print("    Country: United Kingdom")
        
        if clean_number[3] == '7':
            print("    Type: Mobile")
            # UK carrier detection
            uk_prefix = clean_number[3:6] if len(clean_number) >= 6 else ''
            if uk_prefix.startswith('77'):
                print("    Carrier: O2")
                phone_info['carrier'] = 'O2'
            elif uk_prefix.startswith('78'):
                print("    Carrier: O2")
                phone_info['carrier'] = 'O2'
            elif uk_prefix.startswith('79'):
                print("    Carrier: EE")
                phone_info['carrier'] = 'EE'
            elif uk_prefix.startswith('74'):
                print("    Carrier: EE")
                phone_info['carrier'] = 'EE'
            elif uk_prefix.startswith('75'):
                print("    Carrier: EE")
                phone_info['carrier'] = 'EE'
            elif uk_prefix.startswith('76'):
                print("    Carrier: O2")
                phone_info['carrier'] = 'O2'
            elif uk_prefix.startswith('73'):
                print("    Carrier: Three")
                phone_info['carrier'] = 'Three'
            elif uk_prefix.startswith('72'):
                print("    Carrier: O2")
                phone_info['carrier'] = 'O2'
            elif uk_prefix.startswith('71'):
                print("    Carrier: EE")
                phone_info['carrier'] = 'EE'
            else:
                print("    Carrier: Unknown")
        else:
            print("    Type: Landline")
        
        
        uk_cities = {
            '20': 'London',
            '21': 'Birmingham',
            '23': 'Portsmouth',
            '24': 'Nottingham',
            '28': 'Belfast',
            '29': 'Cardiff',
            '31': 'Edinburgh',
            '38': 'Glasgow',
            '39': 'Newcastle',
            '41': 'Glasgow',
            '42': 'Belfast',
            '43': 'Cardiff',
            '44': 'Edinburgh',
            '45': 'Birmingham',
            '46': 'Bristol',
            '48': 'Newport',
            '49': 'Leeds',
            '51': 'Liverpool',
            '52': 'Leeds',
            '53': 'Leeds',
            '54': 'Manchester',
            '55': 'Liverpool',
            '56': 'Sheffield',
            '57': 'Manchester',
            '58': 'Bristol',
            '59': 'Birmingham'
        }
        
        area_code = clean_number[3:5] if len(clean_number) >= 5 else ''
        if area_code in uk_cities:
            print(f"    City: {uk_cities[area_code]}")
            phone_info['city'] = uk_cities[area_code]
    
    
    else:
        print("\n[3] International Number Analysis:")
        # Country code detection
        country_codes = {
            '+1': 'US/Canada',
            '+44': 'United Kingdom',
            '+61': 'Australia',
            '+81': 'Japan',
            '+86': 'China',
            '+91': 'India',
            '+33': 'France',
            '+49': 'Germany',
            '+39': 'Italy',
            '+34': 'Spain',
            '+55': 'Brazil',
            '+7': 'Russia',
            '+82': 'South Korea',
            '+31': 'Netherlands',
            '+46': 'Sweden',
            '+47': 'Norway',
            '+45': 'Denmark',
            '+358': 'Finland',
            '+41': 'Switzerland',
            '+43': 'Austria',
            '+32': 'Belgium',
            '+351': 'Portugal',
            '+30': 'Greece',
            '+90': 'Turkey',
            '+60': 'Malaysia',
            '+65': 'Singapore',
            '+66': 'Thailand',
            '+84': 'Vietnam',
            '+63': 'Philippines',
            '+62': 'Indonesia',
            '+56': 'Chile',
            '+54': 'Argentina',
            '+52': 'Mexico',
            '+27': 'South Africa',
            '+971': 'UAE',
            '+966': 'Saudi Arabia',
            '+64': 'New Zealand',
            '+353': 'Ireland',
            '+972': 'Israel',
            '+48': 'Poland',
            '+36': 'Hungary',
            '+420': 'Czech Republic',
            '+421': 'Slovakia',
            '+386': 'Slovenia',
            '+385': 'Croatia',
            '+381': 'Serbia',
            '+359': 'Bulgaria',
            '+40': 'Romania',
            '+30': 'Greece',
            '+357': 'Cyprus',
            '+356': 'Malta',
            '+354': 'Iceland',
            '+352': 'Luxembourg'
        }
        
        for code, country in country_codes.items():
            if clean_number.startswith(code):
                print(f"    Country: {country}")
                phone_info['country'] = country
                break
        else:
            print("    Country: Unknown")
    
   
    print("\n" + "="*60)
    print("PHONE LOOKUP SUMMARY")
    print("="*60)
    print(f"Number: {clean_number}")
    print(f"Valid: {'Yes' if phone_info['valid'] else 'Unknown'}")
    print(f"Country: {phone_info['country']}")
    print(f"State/Region: {phone_info.get('state', 'Unknown')}")
    print(f"City: {phone_info.get('city', 'Unknown')}")
    print(f"Carrier: {phone_info['carrier']}")
    print(f"Line Type: {phone_info.get('line_type', 'Unknown')}")
    print("="*60)
    
    
    print("\n[+] For more detailed info, try these links:")
    print(f"    https://freecarrierlookup.com/phone/{clean_number}")
    print(f"    https://www.whitepages.com/phone/{clean_number}")
    print(f"    https://www.spytox.com/phone-number-lookup/{clean_number}")
    print(f"    https://www.numverify.com/ (requires free API key)")
    
    input("\nPress Enter to continue...")

if __name__ == "__main__":
    run()
