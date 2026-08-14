
import re, sys, os, requests, json

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
    
    d)
    try:
        # Clean the number - remove spaces and special chars except +
        clean_number = re.sub(r'[^0-9+]', '', phone)
        
        print("[1] Checking number format...")
        
        
        if clean_number.startswith('+'):
            print(f"    International format: {clean_number}")
        elif clean_number.isdigit():
            print(f"    Local format: {clean_number}")
            print("    [i] Try adding country code for better results")
        else:
            print("    [i] Number contains invalid characters")
        
        # Method 2: Try using free API (ip-api.com for location)
        print("\n[2] Checking location...")
        try:
            # Try to get location from IP if number is US
            if clean_number.startswith('+1') or len(clean_number) == 10:
                # For US numbers, try to get area code info
                area_code = clean_number[-10:][:3] if len(clean_number) >= 10 else "Unknown"
                if area_code != "Unknown":
                    print(f"    Area Code: {area_code}")
                    
                    
                    response = requests.get(f"http://ip-api.com/json/", timeout=5)
                    if response.status_code == 200:
                        data = response.json()
                        print(f"    Region: {data.get('regionName', 'Unknown')}")
                        print(f"    City: {data.get('city', 'Unknown')}")
                        print(f"    Country: {data.get('country', 'Unknown')}")
            else:
                print("    Location lookup only available for US numbers")
        except:
            pass
        
        # Method 3: Check carrier info
        print("\n[3] Checking carrier info...")
        try:
            # Try to get carrier info using free API
            if clean_number.startswith('+1'):
                # US numbers - try to identify carrier
                prefixes = {
                    '201': 'AT&T',
                    '202': 'Verizon',
                    '203': 'AT&T',
                    '205': 'AT&T',
                    '206': 'AT&T',
                    '207': 'Verizon',
                    '208': 'AT&T',
                    '209': 'AT&T',
                    '210': 'AT&T',
                    '212': 'Verizon',
                    '213': 'AT&T',
                    '214': 'AT&T',
                    '215': 'Verizon',
                    '216': 'AT&T',
                    '217': 'AT&T',
                    '218': 'AT&T',
                    '219': 'AT&T',
                    '220': 'AT&T',
                    '224': 'AT&T',
                    '225': 'AT&T',
                    '228': 'AT&T',
                    '229': 'AT&T',
                    '231': 'AT&T',
                    '234': 'AT&T',
                    '239': 'AT&T',
                    '240': 'Verizon',
                    '248': 'AT&T',
                    '251': 'AT&T',
                    '252': 'AT&T',
                    '253': 'AT&T',
                    '254': 'AT&T',
                    '256': 'AT&T',
                    '260': 'AT&T',
                    '262': 'AT&T',
                    '267': 'Verizon',
                    '269': 'AT&T',
                    '270': 'AT&T',
                    '272': 'AT&T',
                    '276': 'AT&T',
                    '281': 'AT&T',
                    '283': 'AT&T',
                    '301': 'Verizon',
                    '302': 'Verizon',
                    '303': 'Verizon',
                    '304': 'Verizon',
                    '305': 'AT&T',
                    '307': 'Verizon',
                    '308': 'Verizon',
                    '309': 'Verizon',
                    '310': 'AT&T',
                    '312': 'AT&T',
                    '313': 'AT&T',
                    '314': 'AT&T',
                    '315': 'Verizon',
                    '316': 'AT&T',
                    '317': 'AT&T',
                    '318': 'AT&T',
                    '319': 'Verizon',
                    '320': 'Verizon',
                    '321': 'AT&T',
                    '323': 'AT&T',
                    '325': 'AT&T',
                    '327': 'AT&T',
                    '330': 'AT&T',
                    '331': 'AT&T',
                    '334': 'AT&T',
                    '336': 'AT&T',
                    '337': 'AT&T',
                    '339': 'AT&T',
                    '341': 'AT&T',
                    '346': 'AT&T',
                    '347': 'Verizon',
                    '351': 'AT&T',
                    '352': 'AT&T',
                    '360': 'Verizon',
                    '361': 'AT&T',
                    '364': 'AT&T',
                    '380': 'AT&T',
                    '385': 'AT&T',
                    '386': 'AT&T',
                    '401': 'Verizon',
                    '402': 'Verizon',
                    '404': 'AT&T',
                    '405': 'AT&T',
                    '406': 'AT&T',
                    '407': 'AT&T',
                    '408': 'AT&T',
                    '409': 'AT&T',
                    '410': 'Verizon',
                    '412': 'Verizon',
                    '413': 'Verizon',
                    '414': 'Verizon',
                    '415': 'AT&T',
                    '417': 'AT&T',
                    '419': 'AT&T',
                    '423': 'AT&T',
                    '424': 'AT&T',
                    '425': 'AT&T',
                    '430': 'AT&T',
                    '432': 'AT&T',
                    '434': 'AT&T',
                    '435': 'AT&T',
                    '437': 'AT&T',
                    '440': 'AT&T',
                    '441': 'AT&T',
                    '442': 'AT&T',
                    '443': 'Verizon',
                    '445': 'AT&T',
                    '447': 'AT&T',
                    '448': 'AT&T',
                    '450': 'AT&T',
                    '458': 'AT&T',
                    '463': 'AT&T',
                    '464': 'AT&T',
                    '469': 'AT&T',
                    '470': 'AT&T',
                    '472': 'AT&T',
                    '475': 'AT&T',
                    '478': 'AT&T',
                    '479': 'AT&T',
                    '480': 'AT&T',
                    '484': 'Verizon',
                    '501': 'AT&T',
                    '502': 'AT&T',
                    '503': 'Verizon',
                    '504': 'AT&T',
                    '505': 'AT&T',
                    '507': 'AT&T',
                    '508': 'Verizon',
                    '509': 'AT&T',
                    '510': 'AT&T',
                    '512': 'AT&T',
                    '513': 'AT&T',
                    '515': 'Verizon',
                    '516': 'Verizon',
                    '517': 'AT&T',
                    '518': 'Verizon',
                    '520': 'AT&T',
                    '530': 'AT&T',
                    '531': 'AT&T',
                    '534': 'AT&T',
                    '539': 'AT&T',
                    '540': 'AT&T',
                    '541': 'AT&T',
                    '551': 'Verizon',
                    '559': 'AT&T',
                    '561': 'AT&T',
                    '562': 'AT&T',
                    '563': 'Verizon',
                    '564': 'AT&T',
                    '567': 'AT&T',
                    '570': 'Verizon',
                    '571': 'Verizon',
                    '573': 'AT&T',
                    '574': 'AT&T',
                    '575': 'AT&T',
                    '579': 'AT&T',
                    '580': 'AT&T',
                    '585': 'AT&T',
                    '586': 'AT&T',
                    '601': 'AT&T',
                    '602': 'AT&T',
                    '603': 'Verizon',
                    '605': 'AT&T',
                    '606': 'AT&T',
                    '607': 'Verizon',
                    '608': 'AT&T',
                    '609': 'Verizon',
                    '610': 'Verizon',
                    '612': 'AT&T',
                    '614': 'AT&T',
                    '615': 'AT&T',
                    '616': 'AT&T',
                    '617': 'Verizon',
                    '618': 'AT&T',
                    '619': 'AT&T',
                    '620': 'AT&T',
                    '623': 'AT&T',
                    '626': 'AT&T',
                    '627': 'AT&T',
                    '628': 'AT&T',
                    '629': 'AT&T',
                    '630': 'AT&T',
                    '631': 'Verizon',
                    '636': 'AT&T',
                    '640': 'AT&T',
                    '641': 'AT&T',
                    '646': 'Verizon',
                    '650': 'AT&T',
                    '651': 'Verizon',
                    '657': 'AT&T',
                    '659': 'AT&T',
                    '660': 'AT&T',
                    '661': 'AT&T',
                    '662': 'AT&T',
                    '667': 'AT&T',
                    '669': 'AT&T',
                    '670': 'Verizon',
                    '671': 'Verizon',
                    '678': 'AT&T',
                    '679': 'AT&T',
                    '680': 'AT&T',
                    '681': 'Verizon',
                    '682': 'AT&T',
                    '683': 'AT&T',
                    '689': 'AT&T',
                    '701': 'AT&T',
                    '702': 'AT&T',
                    '703': 'Verizon',
                    '704': 'AT&T',
                    '706': 'AT&T',
                    '707': 'AT&T',
                    '708': 'AT&T',
                    '712': 'Verizon',
                    '713': 'AT&T',
                    '714': 'AT&T',
                    '715': 'AT&T',
                    '716': 'Verizon',
                    '717': 'Verizon',
                    '718': 'Verizon',
                    '719': 'AT&T',
                    '720': 'Verizon',
                    '724': 'Verizon',
                    '725': 'AT&T',
                    '726': 'AT&T',
                    '727': 'AT&T',
                    '731': 'AT&T',
                    '732': 'Verizon',
                    '734': 'AT&T',
                    '737': 'AT&T',
                    '740': 'AT&T',
                    '743': 'AT&T',
                    '747': 'AT&T',
                    '752': 'AT&T',
                    '754': 'AT&T',
                    '757': 'Verizon',
                    '760': 'AT&T',
                    '762': 'AT&T',
                    '763': 'AT&T',
                    '764': 'AT&T',
                    '765': 'AT&T',
                    '769': 'AT&T',
                    '770': 'AT&T',
                    '772': 'AT&T',
                    '773': 'AT&T',
                    '774': 'AT&T',
                    '775': 'AT&T',
                    '779': 'AT&T',
                    '781': 'Verizon',
                    '785': 'AT&T',
                    '786': 'AT&T',
                    '787': 'AT&T',
                    '801': 'Verizon',
                    '802': 'Verizon',
                    '803': 'AT&T',
                    '804': 'Verizon',
                    '805': 'AT&T',
                    '806': 'AT&T',
                    '808': 'AT&T',
                    '810': 'AT&T',
                    '812': 'AT&T',
                    '813': 'AT&T',
                    '814': 'Verizon',
                    '815': 'AT&T',
                    '816': 'AT&T',
                    '817': 'AT&T',
                    '818': 'AT&T',
                    '820': 'AT&T',
                    '825': 'AT&T',
                    '826': 'AT&T',
                    '828': 'AT&T',
                    '830': 'AT&T',
                    '831': 'AT&T',
                    '832': 'AT&T',
                    '833': 'AT&T',
                    '834': 'AT&T',
                    '835': 'AT&T',
                    '836': 'AT&T',
                    '838': 'Verizon',
                    '840': 'AT&T',
                    '843': 'AT&T',
                    '845': 'Verizon',
                    '847': 'AT&T',
                    '848': 'Verizon',
                    '850': 'AT&T',
                    '854': 'AT&T',
                    '856': 'Verizon',
                    '857': 'Verizon',
                    '858': 'AT&T',
                    '859': 'AT&T',
                    '860': 'Verizon',
                    '862': 'Verizon',
                    '863': 'AT&T',
                    '864': 'AT&T',
                    '865': 'AT&T',
                    '870': 'AT&T',
                    '872': 'AT&T',
                    '873': 'AT&T',
                    '878': 'Verizon',
                    '901': 'AT&T',
                    '902': 'AT&T',
                    '903': 'AT&T',
                    '904': 'AT&T',
                    '906': 'AT&T',
                    '907': 'AT&T',
                    '908': 'Verizon',
                    '909': 'AT&T',
                    '910': 'AT&T',
                    '912': 'AT&T',
                    '913': 'AT&T',
                    '914': 'Verizon',
                    '915': 'AT&T',
                    '916': 'AT&T',
                    '917': 'Verizon',
                    '918': 'AT&T',
                    '919': 'AT&T',
                    '920': 'AT&T',
                    '925': 'AT&T',
                    '928': 'AT&T',
                    '929': 'Verizon',
                    '930': 'AT&T',
                    '931': 'AT&T',
                    '934': 'AT&T',
                    '935': 'AT&T',
                    '936': 'AT&T',
                    '937': 'AT&T',
                    '938': 'AT&T',
                    '939': 'AT&T',
                    '940': 'AT&T',
                    '941': 'AT&T',
                    '945': 'AT&T',
                    '947': 'AT&T',
                    '948': 'AT&T',
                    '949': 'AT&T',
                    '951': 'AT&T',
                    '952': 'Verizon',
                    '954': 'AT&T',
                    '956': 'AT&T',
                    '959': 'AT&T',
                    '970': 'AT&T',
                    '971': 'Verizon',
                    '972': 'AT&T',
                    '973': 'Verizon',
                    '975': 'AT&T',
                    '978': 'Verizon',
                    '979': 'AT&T',
                    '980': 'AT&T',
                    '984': 'AT&T',
                    '985': 'AT&T',
                    '986': 'AT&T',
                    '989': 'AT&T'
                }
                
                # Get first 3 digits of number (area code)
                if len(clean_number) >= 10:
                    area = clean_number[-10:][:3]
                    if area in prefixes:
                        print(f"    Carrier: {prefixes[area]}")
                    else:
                        print("    Carrier: Unknown")
            else:
                # International numbers - try to identify country
                country_codes = {
                    '+1': 'US/Canada',
                    '+44': 'UK',
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
                    '+966': 'Saudi Arabia'
                }
                
                for code, country in country_codes.items():
                    if clean_number.startswith(code):
                        print(f"    Country: {country}")
                        break
                else:
                    print("    Country: Unknown")
        except:
            pass
        
        
        print("\n[4] Checking number type...")
        if clean_number.startswith('+') and len(clean_number) >= 10:
            # Check if it's a mobile number (rough guess)
            if clean_number.startswith('+1'):
                # US numbers - check if it's a mobile prefix
                mobile_prefixes = ['201', '202', '203', '206', '212', '213', '214', '215', '216', '217', '218', '219']
                area = clean_number[-10:][:3] if len(clean_number) >= 10 else ''
                if area in mobile_prefixes:
                    print("    Type: Likely Mobile")
                else:
                    print("    Type: Unknown")
            elif clean_number.startswith('+44'):
                # UK numbers - check if it starts with 7 (mobile)
                if len(clean_number) >= 11:
                    if clean_number[3] == '7':
                        print("    Type: Likely Mobile")
                    elif clean_number[3] == '2' or clean_number[3] == '3':
                        print("    Type: Likely Landline")
                    else:
                        print("    Type: Unknown")
            else:
                print("    Type: Unknown")
        else:
            print("    Type: Unknown")
        
        print("\n" + "="*60)
        print("SUMMARY")
        print("="*60)
        print(f"Number: {clean_number}")
        
        
        try:
            location_response = requests.get(f"http://ip-api.com/json/", timeout=5)
            if location_response.status_code == 200:
                loc_data = location_response.json()
                print(f"Location: {loc_data.get('city', 'Unknown')}, {loc_data.get('regionName', 'Unknown')}, {loc_data.get('country', 'Unknown')}")
        except:
            pass
        
        print("="*60)
        
    except Exception as e:
        print(f"[!] Error during lookup: {e}")
        print("\n[!] For more detailed phone lookups, try:")
        print("  - https://www.whitepages.com/phone/" + phone)
        print("  - https://www.spytox.com/phone-number-lookup")
        print("  - https://www.numverify.com/ (requires API key)")
    
    input("\nPress Enter to continue...")

if __name__ == "__main__":
    run()
