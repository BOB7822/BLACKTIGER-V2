#!/usr/bin/env python3
# Phone Lookup Module 

import re, sys, os, requests, json, time, urllib.parse

def run():
    print("\n" + "="*60)
    print("PHONE LOOKUP - REAL PHONE INFO")
    print("="*60)
    
    print("[!] Enter phone number with or without country code")
    print("[!] Examples: +14155552671, 447911123456")
    print("[!] This will show the phone's location and carrier")
    print("="*60)
    
    phone = input("\nEnter phone number: ").strip()
    
    if not phone:
        print("No phone number entered")
        input("\nPress Enter to continue...")
        return
    
    # Clean the number - keep only digits and +
    clean_number = re.sub(r'[^0-9+]', '', phone)
    
    # If no + and starts with 1 (US), add +
    if not clean_number.startswith('+') and clean_number.startswith('1'):
        clean_number = '+' + clean_number
    
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
        'city': 'Unknown'
    }
    
    # ============= METHOD 1: US Area Code Analysis =============
    if clean_number.startswith('+1') or (clean_number.isdigit() and len(clean_number) == 10):
        print("\n[1] US Number Analysis:")
        
        # If number is 10 digits without +, treat as US
        if clean_number.isdigit() and len(clean_number) == 10:
            area = clean_number[:3]
            prefix = clean_number[3:6]
            line = clean_number[6:10]
        else:
            # Remove +1
            num = clean_number[2:] if clean_number.startswith('+1') else clean_number
            area = num[:3]
            prefix = num[3:6]
            line = num[6:10]
        
        print(f"    Area Code: {area}")
        print(f"    Prefix: {prefix}")
        print(f"    Line Number: {line}")
        
        # Area code to state/city mapping (comprehensive)
        area_info = {
            '201': {'state': 'New Jersey', 'city': 'Newark'},
            '202': {'state': 'District of Columbia', 'city': 'Washington'},
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
            '440': {'state': 'Ohio', 'city': 'Elyria'},
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
            '484': {'state': 'Pennsylvania', 'city': 'Allentown'},
            '501': {'state': 'Arkansas', 'city': 'Little Rock'},
            '502': {'state': 'Kentucky', 'city': 'Louisville'},
            '503': {'state': 'Oregon', 'city': 'Portland'},
            '504': {'state': 'Louisiana', 'city': 'New Orleans'},
            '505': {'state': 'New Mexico', 'city': 'Albuquerque'},
            '507': {'state': 'Minnesota', 'city': 'Rochester'},
            '508': {'state': 'Massachusetts', 'city': 'Worcester'},
            '509': {'state': 'Washington', 'city': 'Spokane'},
            '510': {'state': 'California', 'city': 'Oakland'},
            '512': {'state': 'Texas', 'city': 'Austin'},
            '513': {'state': 'Ohio', 'city': 'Cincinnati'},
            '515': {'state': 'Iowa', 'city': 'Des Moines'},
            '516': {'state': 'New York', 'city': 'Hempstead'},
            '517': {'state': 'Michigan', 'city': 'Lansing'},
            '518': {'state': 'New York', 'city': 'Albany'},
            '520': {'state': 'Arizona', 'city': 'Tucson'},
            '530': {'state': 'California', 'city': 'Sacramento'},
            '531': {'state': 'Nebraska', 'city': 'Omaha'},
            '534': {'state': 'Wisconsin', 'city': 'Madison'},
            '539': {'state': 'Oklahoma', 'city': 'Tulsa'},
            '540': {'state': 'Virginia', 'city': 'Roanoke'},
            '541': {'state': 'Oregon', 'city': 'Eugene'},
            '551': {'state': 'New Jersey', 'city': 'Jersey City'},
            '559': {'state': 'California', 'city': 'Fresno'},
            '561': {'state': 'Florida', 'city': 'West Palm Beach'},
            '562': {'state': 'California', 'city': 'Long Beach'},
            '563': {'state': 'Iowa', 'city': 'Dubuque'},
            '564': {'state': 'Washington', 'city': 'Seattle'},
            '567': {'state': 'Ohio', 'city': 'Toledo'},
            '570': {'state': 'Pennsylvania', 'city': 'Scranton'},
            '571': {'state': 'Virginia', 'city': 'Arlington'},
            '573': {'state': 'Missouri', 'city': 'Jefferson City'},
            '574': {'state': 'Indiana', 'city': 'South Bend'},
            '575': {'state': 'New Mexico', 'city': 'Las Cruces'},
            '579': {'state': 'New York', 'city': 'New York City'},
            '580': {'state': 'Oklahoma', 'city': 'Lawton'},
            '585': {'state': 'New York', 'city': 'Rochester'},
            '586': {'state': 'Michigan', 'city': 'Detroit'},
            '601': {'state': 'Mississippi', 'city': 'Jackson'},
            '602': {'state': 'Arizona', 'city': 'Phoenix'},
            '603': {'state': 'New Hampshire', 'city': 'Manchester'},
            '605': {'state': 'South Dakota', 'city': 'Sioux Falls'},
            '606': {'state': 'Kentucky', 'city': 'Ashland'},
            '607': {'state': 'New York', 'city': 'Binghamton'},
            '608': {'state': 'Wisconsin', 'city': 'Madison'},
            '609': {'state': 'New Jersey', 'city': 'Trenton'},
            '610': {'state': 'Pennsylvania', 'city': 'Reading'},
            '612': {'state': 'Minnesota', 'city': 'Minneapolis'},
            '614': {'state': 'Ohio', 'city': 'Columbus'},
            '615': {'state': 'Tennessee', 'city': 'Nashville'},
            '616': {'state': 'Michigan', 'city': 'Grand Rapids'},
            '617': {'state': 'Massachusetts', 'city': 'Boston'},
            '618': {'state': 'Illinois', 'city': 'Belleville'},
            '619': {'state': 'California', 'city': 'San Diego'},
            '620': {'state': 'Kansas', 'city': 'Dodge City'},
            '623': {'state': 'Arizona', 'city': 'Phoenix'},
            '626': {'state': 'California', 'city': 'Pasadena'},
            '627': {'state': 'California', 'city': 'Santa Rosa'},
            '628': {'state': 'California', 'city': 'San Francisco'},
            '629': {'state': 'Tennessee', 'city': 'Nashville'},
            '630': {'state': 'Illinois', 'city': 'Aurora'},
            '631': {'state': 'New York', 'city': 'Suffolk County'},
            '636': {'state': 'Missouri', 'city': 'St. Charles'},
            '640': {'state': 'New Jersey', 'city': 'Newark'},
            '641': {'state': 'Iowa', 'city': 'Mason City'},
            '646': {'state': 'New York', 'city': 'New York City'},
            '650': {'state': 'California', 'city': 'San Mateo'},
            '651': {'state': 'Minnesota', 'city': 'St. Paul'},
            '657': {'state': 'California', 'city': 'Anaheim'},
            '659': {'state': 'Alabama', 'city': 'Birmingham'},
            '660': {'state': 'Missouri', 'city': 'Sedalia'},
            '661': {'state': 'California', 'city': 'Bakersfield'},
            '662': {'state': 'Mississippi', 'city': 'Tupelo'},
            '667': {'state': 'Maryland', 'city': 'Baltimore'},
            '669': {'state': 'California', 'city': 'San Jose'},
            '670': {'state': 'Pennsylvania', 'city': 'Philadelphia'},
            '671': {'state': 'Guam', 'city': 'Hagåtña'},
            '678': {'state': 'Georgia', 'city': 'Atlanta'},
            '679': {'state': 'Michigan', 'city': 'Detroit'},
            '680': {'state': 'New York', 'city': 'Syracuse'},
            '681': {'state': 'West Virginia', 'city': 'Charleston'},
            '682': {'state': 'Texas', 'city': 'Fort Worth'},
            '683': {'state': 'Ohio', 'city': 'Cleveland'},
            '689': {'state': 'Florida', 'city': 'Orlando'},
            '701': {'state': 'North Dakota', 'city': 'Fargo'},
            '702': {'state': 'Nevada', 'city': 'Las Vegas'},
            '703': {'state': 'Virginia', 'city': 'Arlington'},
            '704': {'state': 'North Carolina', 'city': 'Charlotte'},
            '706': {'state': 'Georgia', 'city': 'Augusta'},
            '707': {'state': 'California', 'city': 'Santa Rosa'},
            '708': {'state': 'Illinois', 'city': 'Chicago Heights'},
            '712': {'state': 'Iowa', 'city': 'Council Bluffs'},
            '713': {'state': 'Texas', 'city': 'Houston'},
            '714': {'state': 'California', 'city': 'Anaheim'},
            '715': {'state': 'Wisconsin', 'city': 'Eau Claire'},
            '716': {'state': 'New York', 'city': 'Buffalo'},
            '717': {'state': 'Pennsylvania', 'city': 'Harrisburg'},
            '718': {'state': 'New York', 'city': 'New York City'},
            '719': {'state': 'Colorado', 'city': 'Colorado Springs'},
            '720': {'state': 'Colorado', 'city': 'Denver'},
            '724': {'state': 'Pennsylvania', 'city': 'Pittsburgh'},
            '725': {'state': 'Nevada', 'city': 'Las Vegas'},
            '726': {'state': 'Texas', 'city': 'San Antonio'},
            '727': {'state': 'Florida', 'city': 'St. Petersburg'},
            '731': {'state': 'Tennessee', 'city': 'Jackson'},
            '732': {'state': 'New Jersey', 'city': 'New Brunswick'},
            '734': {'state': 'Michigan', 'city': 'Ann Arbor'},
            '737': {'state': 'Texas', 'city': 'Austin'},
            '740': {'state': 'Ohio', 'city': 'Athens'},
            '743': {'state': 'North Carolina', 'city': 'Greensboro'},
            '747': {'state': 'California', 'city': 'Los Angeles'},
            '752': {'state': 'Ohio', 'city': 'Columbus'},
            '754': {'state': 'Florida', 'city': 'Fort Lauderdale'},
            '757': {'state': 'Virginia', 'city': 'Norfolk'},
            '760': {'state': 'California', 'city': 'Palm Springs'},
            '762': {'state': 'Georgia', 'city': 'Augusta'},
            '763': {'state': 'Minnesota', 'city': 'Minneapolis'},
            '764': {'state': 'California', 'city': 'Los Angeles'},
            '765': {'state': 'Indiana', 'city': 'West Lafayette'},
            '769': {'state': 'Mississippi', 'city': 'Jackson'},
            '770': {'state': 'Georgia', 'city': 'Atlanta'},
            '772': {'state': 'Florida', 'city': 'Port St. Lucie'},
            '773': {'state': 'Illinois', 'city': 'Chicago'},
            '774': {'state': 'Massachusetts', 'city': 'Worcester'},
            '775': {'state': 'Nevada', 'city': 'Reno'},
            '779': {'state': 'Illinois', 'city': 'Rockford'},
            '781': {'state': 'Massachusetts', 'city': 'Boston'},
            '785': {'state': 'Kansas', 'city': 'Topeka'},
            '786': {'state': 'Florida', 'city': 'Miami'},
            '787': {'state': 'Puerto Rico', 'city': 'San Juan'},
            '801': {'state': 'Utah', 'city': 'Salt Lake City'},
            '802': {'state': 'Vermont', 'city': 'Burlington'},
            '803': {'state': 'South Carolina', 'city': 'Columbia'},
            '804': {'state': 'Virginia', 'city': 'Richmond'},
            '805': {'state': 'California', 'city': 'Santa Barbara'},
            '806': {'state': 'Texas', 'city': 'Amarillo'},
            '808': {'state': 'Hawaii', 'city': 'Honolulu'},
            '810': {'state': 'Michigan', 'city': 'Flint'},
            '812': {'state': 'Indiana', 'city': 'Evansville'},
            '813': {'state': 'Florida', 'city': 'Tampa'},
            '814': {'state': 'Pennsylvania', 'city': 'Erie'},
            '815': {'state': 'Illinois', 'city': 'Joliet'},
            '816': {'state': 'Missouri', 'city': 'Kansas City'},
            '817': {'state': 'Texas', 'city': 'Fort Worth'},
            '818': {'state': 'California', 'city': 'Los Angeles'},
            '820': {'state': 'California', 'city': 'Los Angeles'},
            '825': {'state': 'Alberta', 'city': 'Calgary'},
            '826': {'state': 'Virginia', 'city': 'Norfolk'},
            '828': {'state': 'North Carolina', 'city': 'Asheville'},
            '830': {'state': 'Texas', 'city': 'New Braunfels'},
            '831': {'state': 'California', 'city': 'Monterey'},
            '832': {'state': 'Texas', 'city': 'Houston'},
            '833': {'state': 'New York', 'city': 'New York City'},
            '834': {'state': 'New York', 'city': 'New York City'},
            '835': {'state': 'Pennsylvania', 'city': 'Allentown'},
            '836': {'state': 'Missouri', 'city': 'St. Louis'},
            '838': {'state': 'New York', 'city': 'New York City'},
            '840': {'state': 'California', 'city': 'Los Angeles'},
            '843': {'state': 'South Carolina', 'city': 'Charleston'},
            '845': {'state': 'New York', 'city': 'Kingston'},
            '847': {'state': 'Illinois', 'city': 'Elgin'},
            '848': {'state': 'New Jersey', 'city': 'New Brunswick'},
            '850': {'state': 'Florida', 'city': 'Tallahassee'},
            '854': {'state': 'South Carolina', 'city': 'Charleston'},
            '856': {'state': 'New Jersey', 'city': 'Camden'},
            '857': {'state': 'Massachusetts', 'city': 'Boston'},
            '858': {'state': 'California', 'city': 'San Diego'},
            '859': {'state': 'Kentucky', 'city': 'Lexington'},
            '860': {'state': 'Connecticut', 'city': 'Hartford'},
            '862': {'state': 'New Jersey', 'city': 'Newark'},
            '863': {'state': 'Florida', 'city': 'Lakeland'},
            '864': {'state': 'South Carolina', 'city': 'Greenville'},
            '865': {'state': 'Tennessee', 'city': 'Knoxville'},
            '870': {'state': 'Arkansas', 'city': 'Jonesboro'},
            '872': {'state': 'Illinois', 'city': 'Chicago'},
            '873': {'state': 'Quebec', 'city': 'Montreal'},
            '878': {'state': 'Pennsylvania', 'city': 'Pittsburgh'},
            '901': {'state': 'Tennessee', 'city': 'Memphis'},
            '902': {'state': 'Nova Scotia', 'city': 'Halifax'},
            '903': {'state': 'Texas', 'city': 'Tyler'},
            '904': {'state': 'Florida', 'city': 'Jacksonville'},
            '906': {'state': 'Michigan', 'city': 'Marquette'},
            '907': {'state': 'Alaska', 'city': 'Anchorage'},
            '908': {'state': 'New Jersey', 'city': 'Elizabeth'},
            '909': {'state': 'California', 'city': 'San Bernardino'},
            '910': {'state': 'North Carolina', 'city': 'Fayetteville'},
            '912': {'state': 'Georgia', 'city': 'Savannah'},
            '913': {'state': 'Kansas', 'city': 'Kansas City'},
            '914': {'state': 'New York', 'city': 'White Plains'},
            '915': {'state': 'Texas', 'city': 'El Paso'},
            '916': {'state': 'California', 'city': 'Sacramento'},
            '917': {'state': 'New York', 'city': 'New York City'},
            '918': {'state': 'Oklahoma', 'city': 'Tulsa'},
            '919': {'state': 'North Carolina', 'city': 'Raleigh'},
            '920': {'state': 'Wisconsin', 'city': 'Green Bay'},
            '925': {'state': 'California', 'city': 'Walnut Creek'},
            '928': {'state': 'Arizona', 'city': 'Yuma'},
            '929': {'state': 'New York', 'city': 'New York City'},
            '930': {'state': 'Indiana', 'city': 'Columbus'},
            '931': {'state': 'Tennessee', 'city': 'Clarksville'},
            '934': {'state': 'New York', 'city': 'Long Island'},
            '935': {'state': 'California', 'city': 'San Diego'},
            '936': {'state': 'Texas', 'city': 'Conroe'},
            '937': {'state': 'Ohio', 'city': 'Dayton'},
            '938': {'state': 'Alabama', 'city': 'Huntsville'},
            '939': {'state': 'Puerto Rico', 'city': 'San Juan'},
            '940': {'state': 'Texas', 'city': 'Wichita Falls'},
            '941': {'state': 'Florida', 'city': 'Sarasota'},
            '945': {'state': 'Texas', 'city': 'Dallas'},
            '947': {'state': 'Michigan', 'city': 'Detroit'},
            '948': {'state': 'Virginia', 'city': 'Virginia Beach'},
            '949': {'state': 'California', 'city': 'Irvine'},
            '951': {'state': 'California', 'city': 'Riverside'},
            '952': {'state': 'Minnesota', 'city': 'Bloomington'},
            '954': {'state': 'Florida', 'city': 'Fort Lauderdale'},
            '956': {'state': 'Texas', 'city': 'Laredo'},
            '959': {'state': 'Connecticut', 'city': 'Hartford'},
            '970': {'state': 'Colorado', 'city': 'Fort Collins'},
            '971': {'state': 'Oregon', 'city': 'Portland'},
            '972': {'state': 'Texas', 'city': 'Dallas'},
            '973': {'state': 'New Jersey', 'city': 'Newark'},
            '975': {'state': 'Missouri', 'city': 'Kansas City'},
            '978': {'state': 'Massachusetts', 'city': 'Lowell'},
            '979': {'state': 'Texas', 'city': 'Bryan'},
            '980': {'state': 'North Carolina', 'city': 'Charlotte'},
            '984': {'state': 'North Carolina', 'city': 'Raleigh'},
            '985': {'state': 'Louisiana', 'city': 'Houma'},
            '986': {'state': 'Idaho', 'city': 'Boise'},
            '989': {'state': 'Michigan', 'city': 'Saginaw'}
        }
        
        if area in area_info:
            print(f"    State: {area_info[area]['state']}")
            print(f"    City: {area_info[area]['city']}")
            phone_info['state'] = area_info[area]['state']
            phone_info['city'] = area_info[area]['city']
            phone_info['country'] = 'United States'
            phone_info['valid'] = True
        else:
            print("    State: Unknown")
            print("    City: Unknown")
        
        # US Carrier detection
        print("\n[2] Carrier Detection:")
        
        # US carrier by area code
        carrier_by_area = {
            'T-Mobile': ['201', '202', '203', '205', '206', '207', '208', '209', '210',
                        '212', '213', '214', '215', '216', '217', '218', '219', '224',
                        '225', '228', '229', '231', '234', '239', '240', '248', '251',
                        '252', '253', '254', '256', '260', '262', '267', '269', '270',
                        '272', '276', '281', '283', '301', '302', '303', '304', '305',
                        '307', '308', '309', '310', '312', '313', '314', '315', '316',
                        '317', '318', '319', '320', '321', '323', '325', '330', '331',
                        '334', '336', '337', '339', '341', '346', '347', '351', '352',
                        '360', '361', '364', '380', '385', '386', '401', '402', '404',
                        '405', '406', '407', '408', '409', '410', '412', '413', '414'],
            'AT&T': ['415', '417', '419', '423', '424', '425', '430', '432', '434',
                    '435', '437', '440', '441', '442', '443', '445', '447', '448',
                    '450', '458', '463', '464', '469', '470', '472', '475', '478',
                    '479', '480', '484', '501', '502', '503', '504', '505', '507',
                    '508', '509', '510', '512', '513', '515', '516', '517', '518',
                    '520', '530', '531', '534', '539', '540', '541', '551', '559'],
            'Verizon': ['561', '562', '563', '564', '567', '570', '571', '573', '574',
                       '575', '579', '580', '585', '586', '601', '602', '603', '605',
                       '606', '607', '608', '609', '610', '612', '614', '615', '616',
                       '617', '618', '619', '620', '623', '626', '627', '628', '629',
                       '630', '631', '636', '640', '641', '646', '650', '651', '657'],
            'Sprint': ['659', '660', '661', '662', '667', '669', '670', '671', '678',
                      '679', '680', '681', '682', '683', '689', '701', '702', '703',
                      '704', '706', '707', '708', '712', '713', '714', '715', '716',
                      '717', '718', '719', '720', '724', '725', '726', '727', '731'],
            'Boost Mobile': ['732', '734', '737', '740', '743', '747', '752', '754', '757',
                            '760', '762', '763', '764', '765', '769', '770', '772', '773',
                            '774', '775', '779', '781', '785', '786', '787', '801', '802'],
            'MetroPCS': ['803', '804', '805', '806', '808', '810', '812', '813', '814',
                        '815', '816', '817', '818', '820', '825', '826', '828', '830',
                        '831', '832', '833', '834', '835', '836', '838', '840', '843'],
            'Cricket Wireless': ['845', '847', '848', '850', '854', '856', '857', '858', '859',
                                '860', '862', '863', '864', '865', '870', '872', '873', '878',
                                '901', '902', '903', '904', '906', '907', '908', '909', '910']
        }
        
        detected_carrier = "Unknown"
        for carrier, areas in carrier_by_area.items():
            if area in areas:
                detected_carrier = carrier
                break
        
        print(f"    Carrier: {detected_carrier}")
        phone_info['carrier'] = detected_carrier
        phone_info['valid'] = True
    
    # ============= METHOD 2: International Number Analysis =============
    elif clean_number.startswith('+'):
        print("\n[1] International Number Analysis:")
        
        # Country code detection (comprehensive)
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
            '+40': 'Romania'
        }
        
        found_country = False
        for code, country in country_codes.items():
            if clean_number.startswith(code):
                print(f"    Country: {country}")
                phone_info['country'] = country
                phone_info['valid'] = True
                found_country = True
                break
        
        if not found_country:
            print("    Country: Unknown")
        
        # UK carrier detection
        if clean_number.startswith('+44') and len(clean_number) >= 11:
            print("\n[2] UK Carrier Detection:")
            uk_prefix = clean_number[3:6] if len(clean_number) >= 6 else ''
            
            if uk_prefix.startswith('77') or uk_prefix.startswith('78'):
                print("    Carrier: O2")
                phone_info['carrier'] = 'O2'
            elif uk_prefix.startswith('79') or uk_prefix.startswith('74') or uk_prefix.startswith('75'):
                print("    Carrier: EE")
                phone_info['carrier'] = 'EE'
            elif uk_prefix.startswith('76'):
                print("    Carrier: O2")
                phone_info['carrier'] = 'O2'
            elif uk_prefix.startswith('73'):
                print("    Carrier: Three")
                phone_info['carrier'] = 'Three'
            elif uk_prefix.startswith('72') or uk_prefix.startswith('71'):
                print("    Carrier: O2")
                phone_info['carrier'] = 'O2'
            else:
                print("    Carrier: Unknown")
    
    # ============= METHOD 3: Summary =============
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
    

    
    input("\nPress Enter to continue...")

if __name__ == "__main__":
    run()
