import os
import sys
import time
import platform
import subprocess
import importlib
import shutil
import re
import random

W = "\033[38;2;255;255;255m"
G = "\033[38;2;180;180;180m"
M = "\033[38;2;120;120;120m"
D = "\033[38;2;70;70;70m"
B = "\033[38;2;40;40;40m"
BOLD = "\033[1m"
RESET = "\033[0m"
R = "\033[38;2;255;0;0m"
Y = "\033[38;2;255;255;0m"
C = "\033[38;2;0;255;255m"

def clear():
    os.system('cls' if platform.system() == "Windows" else 'clear')

def center(text, width=None):
    if width is None:
        try: width = os.get_terminal_size().columns
        except: width = 120
    visible_length = clean_len(text)
    total_padding = width - visible_length
    left_padding = total_padding // 2
    right_padding = total_padding - left_padding
    return (" " * left_padding) + text + (" " * right_padding)

def get_width():
    try: return os.get_terminal_size().columns
    except: return 120

def clean_len(text):
    ansi_escape = re.compile(r'\x1b\[[0-9;]*m|\033\[[0-9:]*m')
    return len(ansi_escape.sub('', text))

LOGO = [
    f"{G}",
    f"{G}                    ▄▄▄▄    ██▓     ▄▄▄       ▄████  ██ ▄█▀    ████████╗██▓  ▄████  ▓█████  ██▀███",
    f"{G}                   ▓█████▄ ▓██▒   ▄████▄    ██▒ ▀█▒ ██▄█▒        ██║   ██▓ ▓██▒ ██▒ ▓█   ▀ ▓██ ▒ ██▒",
    f"{G}                ▒██▒ ▄██▒██░  ▒██  ▀█▄  ▒██░▄▄▄░███▄███▒      ██║   ██▒ ▒██░▄▄▄░ ▒███   ▓██ ░▄█ ▒",
    f"{G}                ▒██░█▀  ▒██░  ░██▄▄▄▄██ ▒██▀   ████ █▄        ██║   ██░ ░▓█  ██▓ ▒▓█  ▄ ▒██▀▀█▄",
    f"{G}                ░▓█  ▀█▓░██████▒▓█   ▓██▒░██████▒██▒ █▄       ██║   ██░ ░▒▓███▀▒ ░▒████░░██▓ ▒██▒",
    f"{G}                 ░▒▓███▀▒░ ▒░▓  ░▒▒   ▓▒█░░ ▒░▓  ░ ▒▒ ▓▒       ▒ ░   ░   ░▒   ▒  ░░ ▒░ ░░ ▒▓ ░▒▓░",
    f"{G}                  ░▒   ░ ░ ░ ▒  ░ ▒   ▒▒ ░░ ░ ▒  ░ ░▒ ▒░       ░     ▒ ░  ░   ░   ░ ░  ░  ░▒ ░ ▒░",
    f"{G}                  ░    ░   ░ ░    ░   ▒     ░ ░    ░░ ░        ░     ▒ ░░ ░   ░     ░     ░░   ░",
    f"{G}                   ░          ░        ░  ░    ░    ░  ░              ░        ░     ░  ░   ░",
]

EYE = [
    f"{M}",
    f"{W}     .-._   _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ .-.{RESET}",
    f"{W}    /     ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` `     \\{RESET}",
    f"{W}   |    _..----.._                                                                                      _..----.._    |{RESET}",
    f"{W}   |  .'          `.                                                                                  .'          `.  |{RESET}",
    f"{W}   | /  /\      /\  \\                                                                                /  /\      /\  \\ |{RESET}",
    f"{W}   || |  o|    | o|  ||                                                                              || |  o|    | o|  ||{RESET}",
    f"{W}   || |  __|    | __|  ||                                                                              || |  __|    | __|  ||{RESET}",
    f"{W}   ||  \\   /  /\\  \\   /  ||                                                                              ||  \\   /  /\\  \\   /  ||{RESET}",
    f"{W}   |  \\  `.'  (__)  `.'  /  |                                                                            |  \\  `.'  (__)  `.'  /  |{RESET}",
    f"{W}   |   `.  \\  `----'  /  .'   |                                                                          |   `.  \\  `----'  /  .'   |{RESET}",
    f"{W}   |    `-.`--------'.-'    |                                                                          |    `-.`--------'.-'    |{RESET}",
    f"{W}   |       `--------'       |                                                                          |       `--------'       |{RESET}",
    f"{W}   \\                       /                                                                          \\                       /{RESET}",
    f"{W}    `.                   .'                                                                            `.                   .'{RESET}",
    f"{W}      `-._           _.-'                                                                                `-._           _.-'{RESET}",
    f"{W}          `---------´                                                                                      `---------´{RESET}",
    f"{C}═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════{RESET}",
]

SKULL = [
    f"{R}",
    f"{R}   .-. .-. .-. .-. .-. .-. .-. .-. .-. .-. .-. .-. .-. .-. .-. .-. .-. .-. .-. .-. .-. .-. .-. .-. .-. .-. .-. .-.{RESET}",
    f"{R}   | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | |{RESET}",
    f"{R}   `-' `-' `-' `-' `-' `-' `-' `-' `-' `-' `-' `-' `-' `-' `-' `-' `-' `-' `-' `-' `-' `-' `-' `-' `-' `-' `-' `-'{RESET}",
    f"{R}   .-. .-. .-. .-. .-. .-. .-. .-. .-. .-. .-. .-. .-. .-. .-. .-. .-. .-. .-. .-. .-. .-. .-. .-. .-. .-. .-. .-.{RESET}",
    f"{R}   | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | |{RESET}",
    f"{R}   `-' `-' `-' `-' `-' `-' `-' `-' `-' `-' `-' `-' `-' `-' `-' `-' `-' `-' `-' `-' `-' `-' `-' `-' `-' `-' `-' `-'{RESET}",
    f"{R}   .-. .-. .-. .-. .-. .-. .-. .-. .-. .-. .-. .-. .-. .-. .-. .-. .-. .-. .-. .-. .-. .-. .-. .-. .-. .-. .-. .-.{RESET}",
    f"{R}   | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | |{RESET}",
    f"{R}   `-' `-' `-' `-' `-' `-' `-' `-' `-' `-' `-' `-' `-' `-' `-' `-' `-' `-' `-' `-' `-' `-' `-' `-' `-' `-' `-' `-'{RESET}",
]

BLACKTIGER = [
    f"{Y}",
    f"{Y}   _...----.._{RESET}",
    f"{Y} .-'           `-.{RESET}",
    f"{Y}.'  _..----.._     `.{RESET}",
    f"{Y}/  .'          `.     \\{RESET}",
    f"{Y}|  /  /\\      /\\  \\     |{RESET}",
    f"{Y}|| |  o|    | o|  |    ||{RESET}",
    f"{Y}|| |  __|    | __|  |    ||{RESET}",
    f"{Y}||  \\   /  /\\  \\   /     ||{RESET}",
    f"{Y}|  \\  `.'  (__)  `.'  /  |{RESET}",
    f"{Y} `.  \\  `----'  /  .'   {RESET}",
    f"{Y}   `-.`--------'.-'{RESET}",
    f"{Y}      `--------'{RESET}",
    f"{G}═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════{RESET}",
    f"{W}                                                                                                                     {RESET}",
    f"{W}  ____  _        _    ____ _  _______ ___  ____ _____ ____                                                          {RESET}",
    f"{W} | __ )| |      / \\  / ___| |/ /_   _|_ _|/ ___| ____|  _ \\                                                         {RESET}",
    f"{W} |  _ \\| |     / _ \\| |   | ' /  | |  | || |  _|  _| | |_) |                                                        {RESET}",
    f"{W} | |_) | |___ / ___ \\ |___| . \\  | |  | || |_| | |___|  _ <                                                         {RESET}",
    f"{W} |____/|_____/_/   \\_\\____|_|\\_\\ |_| |___|\\____|_____|_| \\_\\                                                        {RESET}",
    f"{W}                                                                                                                     {RESET}",
    f"{W}  __  __ _   _ _   _____ ___   _____ ___   ___  _                                                                   {RESET}",
    f"{W} |  \\/  | | | | | |_   _|_ _| |_   _/ _ \\ / _ \\| |                                                                  {RESET}",
    f"{W} | |\\/| | | | | |   | |  | |    | || | | | | | | |                                                                  {RESET}",
    f"{W} | |  | | |_| | |___| |  | |    | || |_| | |_| | |___                                                               {RESET}",
    f"{W} |_|  |_|\\___/|_____|_| |___|   |_| \\___/ \\___/|_____|                                                              {RESET}",
    f"{G}═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════{RESET}",
]

TIGER_LOGO = [
    f"{Y}",
    f"{Y}   _...----.._{RESET}",
    f"{Y} .-'           `-.{RESET}",
    f"{Y}.'  _..----.._     `.{RESET}",
    f"{Y}/  .'          `.     \\{RESET}",
    f"{Y}|  /  /\\      /\\  \\     |{RESET}",
    f"{Y}|| |  o|    | o|  |    ||{RESET}",
    f"{Y}|| |  __|    | __|  |    ||{RESET}",
    f"{Y}||  \\   /  /\\  \\   /     ||{RESET}",
    f"{Y}|  \\  `.'  (__)  `.'  /  |{RESET}",
    f"{Y} `.  \\  `----'  /  .'   {RESET}",
    f"{Y}   `-.`--------'.-'{RESET}",
    f"{Y}      `--------'{RESET}",
]

def animate_osint():
    width = get_width()
    clear()
    for line in LOGO:
        print(center(f"{W}{BOLD}{line}{RESET}", width))
    border = "═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════"
    print(center(f"{G}{border}{RESET}", width))
    print(center(f"{W}{BOLD}                     ██  BLACK TIGER V2.0 - OSINT PAGE  ██{RESET}", width))
    print(center(f"{G}{border}{RESET}", width))
    print()
    for i in range(3):
        for line in EYE:
            if i == 0:
                print(center(f"{D}{line}{RESET}", width))
            elif i == 1:
                print(center(f"{M}{line}{RESET}", width))
            else:
                print(center(f"{C}{line}{RESET}", width))
        time.sleep(0.15)
    for _ in range(2):
        time.sleep(0.1)
        clear()
        for line in LOGO:
            print(center(f"{W}{BOLD}{line}{RESET}", width))
        print(center(f"{G}{border}{RESET}", width))
        print(center(f"{W}{BOLD}                     ██  BLACK TIGER V2.0 - OSINT PAGE  ██{RESET}", width))
        print(center(f"{G}{border}{RESET}", width))
        print()
        for line in EYE:
            print(center(f"{D}{line}{RESET}", width))
        time.sleep(0.05)
        clear()
        for line in LOGO:
            print(center(f"{W}{BOLD}{line}{RESET}", width))
        print(center(f"{G}{border}{RESET}", width))
        print(center(f"{W}{BOLD}                     ██  BLACK TIGER V2.0 - OSINT PAGE  ██{RESET}", width))
        print(center(f"{G}{border}{RESET}", width))
        print()
        for line in EYE:
            print(center(f"{C}{line}{RESET}", width))
        time.sleep(0.1)
    print()
    print(center(f"{G}═══════════════════════════════════════════════════════════════════════════════════════════════{RESET}", width))
    print(center(f"{W}                     OSINT MODULE LOADED SUCCESSFULLY{RESET}", width))
    print(center(f"{G}═══════════════════════════════════════════════════════════════════════════════════════════════{RESET}", width))
    time.sleep(0.8)

def animate_attack():
    width = get_width()
    clear()
    for line in LOGO:
        print(center(f"{W}{BOLD}{line}{RESET}", width))
    border = "═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════"
    print(center(f"{G}{border}{RESET}", width))
    print(center(f"{W}{BOLD}                     ██  BLACK TIGER V2.0 - ATTACK PAGE  ██{RESET}", width))
    print(center(f"{G}{border}{RESET}", width))
    print()
    for i in range(3):
        for line in SKULL:
            if i == 0:
                print(center(f"{D}{line}{RESET}", width))
            elif i == 1:
                print(center(f"{M}{line}{RESET}", width))
            else:
                print(center(f"{R}{line}{RESET}", width))
        time.sleep(0.15)
    print()
    print(center(f"{G}═══════════════════════════════════════════════════════════════════════════════════════════════{RESET}", width))
    print(center(f"{W}                     ATTACK MODULE LOADED SUCCESSFULLY{RESET}", width))
    print(center(f"{G}═══════════════════════════════════════════════════════════════════════════════════════════════{RESET}", width))
    time.sleep(0.8)

def show_blacktiger():
    width = get_width()
    clear()
    for line in TIGER_LOGO:
        print(center(f"{Y}{line}{RESET}", width))
    print(center(f"{G}═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════{RESET}", width))
    print(center(f"{W}                     BLACK TIGER v2 {RESET}", width))
    print(center(f"{G}═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════{RESET}", width))
    print(center(f"{M}                         made by BOB{RESET}", width))
    print(center(f"{M}                    Discord.gg/nvbQsxFJgz{RESET}", width))
    time.sleep(2)

def show_skull():
    width = get_width()
    clear()
    for line in SKULL:
        print(center(f"{R}{line}{RESET}", width))
    print(center(f"{G}═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════{RESET}", width))
    print(center(f"{W}                     DEATH AWAITS ALL WHO ENTER{RESET}", width))
    print(center(f"{G}═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════{RESET}", width))
    time.sleep(2)

def show_eye():
    width = get_width()
    clear()
    for line in EYE:
        print(center(f"{C}{line}{RESET}", width))
    print(center(f"{G}═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════{RESET}", width))
    print(center(f"{W}                     THE EYE SEES ALL{RESET}", width))
    print(center(f"{G}═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════{RESET}", width))
    time.sleep(2)

def menu_banner(page=1):
    clear()
    width = get_width()
    for line in LOGO:
        print(center(f"{W}{BOLD}{line}{RESET}", width))
    border = "═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════"
    print(center(f"{G}{border}{RESET}", width))
    if page == 1:
        print(center(f"{W}{BOLD}                     ██  BLACK TIGER V2.0 - MAIN MENU  ██{RESET}", width))
    elif page == 2:
        print(center(f"{W}{BOLD}                     ██  BLACK TIGER V2.0 - OSINT PAGE  ██{RESET}", width))
    elif page == 3:
        print(center(f"{W}{BOLD}                     ██  BLACK TIGER V2.0 - ATTACK PAGE  ██{RESET}", width))
    print(center(f"{G}{border}{RESET}", width))
    print(center(f"{M}                         made by BOB{RESET}", width))
    print(center(f"{M}                    Discord.gg/nvbQsxFJgz{RESET}", width))
    print(center(f"{D}                   Type 'h' for help | 'q' to quit{RESET}", width))
    print()

def pad_list(lst, target_width):
    result = []
    for item in lst:
        visible_len = clean_len(item)
        padding = target_width - visible_len
        if padding > 0:
            if RESET in item:
                parts = item.split(RESET)
                if len(parts) >= 2:
                    item = parts[0] + " " * padding + RESET + "".join(parts[1:])
                else:
                    item = item + " " * padding
            else:
                item = item + " " * padding
        result.append(item)
    return result

def menu(page=1):
    menu_banner(page)
    width = get_width()
    
    if page == 1:
        col1 = [
            f"{W}┌────────── NETWORK SCANNER ──────────┐{RESET}",
            f"{W}│                                     │{RESET}",
            f"{W}│  {BOLD}[06]{RESET} Web Vuln Scanner     │{RESET}",
            f"{W}│  {BOLD}[07]{RESET} Web Info Scanner     │{RESET}",
            f"{W}│  {BOLD}[08]{RESET} Web URL Scanner      │{RESET}",
            f"{W}│  {BOLD}[09]{RESET} IP Scanner           │{RESET}",
            f"{W}│  {BOLD}[10]{RESET} Port Scanner         │{RESET}",
            f"{W}│  {BOLD}[11]{RESET} IP Pinger            │{RESET}",
            f"{W}└─────────────────────────────────────┘{RESET}"
        ]
        col2 = [
            f"{W}┌───────────── UTILITIES ──────────────┐{RESET}",
            f"{W}│                                      │{RESET}",
            f"{W}│  {BOLD}[04]{RESET} DOS Attack           │{RESET}",
            f"{W}│  {BOLD}[41]{RESET} UDP Flooder          │{RESET}",
            f"{W}│  {BOLD}[22]{RESET} Phishing Attack      │{RESET}",
            f"{W}│  {BOLD}[23]{RESET} Password Decrypt     │{RESET}",
            f"{W}│  {BOLD}[24]{RESET} Password Encrypt     │{RESET}",
            f"{W}│  {BOLD}[25]{RESET} Hash Generator       │{RESET}",
            f"{W}│  {BOLD}[26]{RESET} Search Database      │{RESET}",
            f"{W}│  {BOLD}[27]{RESET} Dark Web Links       │{RESET}",
            f"{W}│  {BOLD}[28]{RESET} IP Generator         │{RESET}",
            f"{W}└──────────────────────────────────────┘{RESET}"
        ]
        col3 = [
            f"{W}┌───────── MALWARE BUILDER ────────────┐{RESET}",
            f"{W}│                                    │{RESET}",
            f"{W}│  {BOLD}[29]{RESET} Stealer             │{RESET}",
            f"{W}│  {BOLD}[30]{RESET} FUD Malware Gen     │{RESET}",
            f"{W}│                                    │{RESET}",
            f"{W}│  ─── Discord Tools ───             │{RESET}",
            f"{W}│  {BOLD}[31]{RESET} Token Discord       │{RESET}",
            f"{W}│  {BOLD}[32]{RESET} Bot Discord         │{RESET}",
            f"{W}│  {BOLD}[33]{RESET} Webhook Discord     │{RESET}",
            f"{W}│  {BOLD}[34]{RESET} Discord Server      │{RESET}",
            f"{W}│  {BOLD}[35]{RESET} Nitro Generator     │{RESET}",
            f"{W}└────────────────────────────────────┘{RESET}"
        ]
        
        col_width = 38
        col2_width = 40
        col3_width = 40
        
        col1 = pad_list(col1, col_width)
        col2 = pad_list(col2, col2_width)
        col3 = pad_list(col3, col3_width)
        
        combined = []
        max_len = max(len(col1), len(col2), len(col3))
        for i in range(max_len):
            c1 = col1[i] if i < len(col1) else " " * col_width
            c2 = col2[i] if i < len(col2) else " " * col2_width
            c3 = col3[i] if i < len(col3) else " " * col3_width
            combined.append(f"{c1}  {c2}  {c3}")
        
        for line in combined:
            print(center(line, width))
        
        print()
        print(center(f"{W}█  Type 'n' for next page (OSINT)  |  'h' for help  |  'q' to quit  █{RESET}", width))
    
    elif page == 2:
        col1 = [
            f"{W}┌─────────── OSINT TOOLS ────────────┐{RESET}",
            f"{W}│                                     │{RESET}",
            f"{W}│  {BOLD}[12]{RESET} Dox Create           │{RESET}",
            f"{W}│  {BOLD}[13]{RESET} Dox Tracker          │{RESET}",
            f"{W}│  {BOLD}[14]{RESET} Social Media Search  │{RESET}",
            f"{W}│  {BOLD}[15]{RESET} Reverse Image Search │{RESET}",
            f"{W}│  {BOLD}[16]{RESET} Username Tracker     │{RESET}",
            f"{W}│  {BOLD}[17]{RESET} Email Tracker        │{RESET}",
            f"{W}│  {BOLD}[18]{RESET} Email Lookup         │{RESET}",
            f"{W}│  {BOLD}[19]{RESET} Phone Lookup         │{RESET}",
            f"{W}│  {BOLD}[20]{RESET} 10 Min Email Gen     │{RESET}",
            f"{W}└─────────────────────────────────────┘{RESET}"
        ]
        col2 = [
            f"{W}┌───────── GAMING TOOLS ─────────────┐{RESET}",
            f"{W}│                                    │{RESET}",
            f"{W}│  {BOLD}[36]{RESET} Roblox Cookie       │{RESET}",
            f"{W}│  {BOLD}[37]{RESET} Roblox Info         │{RESET}",
            f"{W}│  {BOLD}[38]{RESET} Roblox User         │{RESET}",
            f"{W}│  {BOLD}[39]{RESET} Roblox ID           │{RESET}",
            f"{W}│                                    │{RESET}",
            f"{W}│  ─── Tools ───                     │{RESET}",
            f"{W}│  {BOLD}[01]{RESET} Python Obfuscator   │{RESET}",
            f"{W}│  {BOLD}[02]{RESET} Discord RAT         │{RESET}",
            f"{W}│  {BOLD}[03]{RESET} Ransomware          │{RESET}",
            f"{W}│  {BOLD}[05]{RESET} Proxy Scraper       │{RESET}",
            f"{W}│  {BOLD}[40]{RESET} System Info         │{RESET}",
            f"{W}└────────────────────────────────────┘{RESET}"
        ]
        col3 = [
            f"{W}┌─────────── EXTRA OSINT ─────────────┐{RESET}",
            f"{W}│                                     │{RESET}",
            f"{W}│  {BOLD}[51]{RESET} WHOIS Lookup         │{RESET}",
            f"{W}│  {BOLD}[52]{RESET} DNS Lookup           │{RESET}",
            f"{W}│  {BOLD}[53]{RESET} Subdomain Scanner    │{RESET}",
            f"{W}│  {BOLD}[54]{RESET} IP Geolocation       │{RESET}",
            f"{W}│  {BOLD}[55]{RESET} SSL Certificate Info │{RESET}",
            f"{W}│  {BOLD}[56]{RESET} Port Scanner         │{RESET}",
            f"{W}│  {BOLD}[57]{RESET} Shodan Search        │{RESET}",
            f"{W}│  {BOLD}[58]{RESET} Censys Search        │{RESET}",
            f"{W}│  {BOLD}[59]{RESET} Wayback Machine      │{RESET}",
            f"{W}│  {BOLD}[60]{RESET} Email Reputation     │{RESET}",
            f"{W}└─────────────────────────────────────┘{RESET}"
        ]
        
        col_width = 38
        col2_width = 40
        col3_width = 40
        
        col1 = pad_list(col1, col_width)
        col2 = pad_list(col2, col2_width)
        col3 = pad_list(col3, col3_width)
        
        combined = []
        max_len = max(len(col1), len(col2), len(col3))
        for i in range(max_len):
            c1 = col1[i] if i < len(col1) else " " * col_width
            c2 = col2[i] if i < len(col2) else " " * col2_width
            c3 = col3[i] if i < len(col3) else " " * col3_width
            combined.append(f"{c1}  {c2}  {c3}")
        
        for line in combined:
            print(center(line, width))
        
        print()
        print(center(f"{W}█  Type 'n' for next page (ATTACK)  |  'b' for previous  |  'q' to quit  █{RESET}", width))
    
    elif page == 3:
        col1 = [
            f"{W}┌────────── ATTACK TOOLS ────────────┐{RESET}",
            f"{W}│                                     │{RESET}",
            f"{W}│  {BOLD}[70]{RESET} ARP Spoofing         │{RESET}",
            f"{W}│  {BOLD}[71]{RESET} DNS Spoofing         │{RESET}",
            f"{W}│  {BOLD}[72]{RESET} MAC Flooding         │{RESET}",
            f"{W}│  {BOLD}[73]{RESET} DHCP Starvation      │{RESET}",
            f"{W}│  {BOLD}[74]{RESET} ICMP Redirect        │{RESET}",
            f"{W}│  {BOLD}[75]{RESET} SYN Flood            │{RESET}",
            f"{W}│  {BOLD}[76]{RESET} UDP Flood            │{RESET}",
            f"{W}│  {BOLD}[77]{RESET} HTTP Flood           │{RESET}",
            f"{W}│  {BOLD}[78]{RESET} Slowloris            │{RESET}",
            f"{W}└─────────────────────────────────────┘{RESET}"
        ]
        col2 = [
            f"{W}┌─────────── SNIFFERS ───────────────┐{RESET}",
            f"{W}│                                     │{RESET}",
            f"{W}│  {BOLD}[80]{RESET} Network Sniffer      │{RESET}",
            f"{W}│  {BOLD}[81]{RESET} Packet Sniffer       │{RESET}",
            f"{W}│  {BOLD}[82]{RESET} ARP Sniffer          │{RESET}",
            f"{W}│  {BOLD}[83]{RESET} DNS Sniffer          │{RESET}",
            f"{W}│  {BOLD}[84]{RESET} HTTP Sniffer         │{RESET}",
            f"{W}│  {BOLD}[85]{RESET} SSL Sniffer          │{RESET}",
            f"{W}│  {BOLD}[86]{RESET} WiFi Sniffer         │{RESET}",
            f"{W}│  {BOLD}[87]{RESET} Bluetooth Sniffer    │{RESET}",
            f"{W}│  {BOLD}[88]{RESET} USB Sniffer          │{RESET}",
            f"{W}└─────────────────────────────────────┘{RESET}"
        ]
        col3 = [
            f"{W}┌───────── EXPLOIT TOOLS ────────────┐{RESET}",
            f"{W}│                                     │{RESET}",
            f"{W}│  {BOLD}[90]{RESET} Port Knocking        │{RESET}",
            f"{W}│  {BOLD}[91]{RESET} MAC Changer          │{RESET}",
            f"{W}│  {BOLD}[92]{RESET} Packet Generator     │{RESET}",
            f"{W}│  {BOLD}[93]{RESET} Rogue AP             │{RESET}",
            f"{W}│  {BOLD}[94]{RESET} Deauth Attack        │{RESET}",
            f"{W}│  {BOLD}[95]{RESET} Beacon Flood         │{RESET}",
            f"{W}│  {BOLD}[96]{RESET} Evil Twin            │{RESET}",
            f"{W}│  {BOLD}[97]{RESET} Karma Attack         │{RESET}",
            f"{W}│  {BOLD}[98]{RESET} Probe Request Flood  │{RESET}",
            f"{W}└─────────────────────────────────────┘{RESET}"
        ]
        
        col_width = 38
        col2_width = 40
        col3_width = 40
        
        col1 = pad_list(col1, col_width)
        col2 = pad_list(col2, col2_width)
        col3 = pad_list(col3, col3_width)
        
        combined = []
        max_len = max(len(col1), len(col2), len(col3))
        for i in range(max_len):
            c1 = col1[i] if i < len(col1) else " " * col_width
            c2 = col2[i] if i < len(col2) else " " * col2_width
            c3 = col3[i] if i < len(col3) else " " * col3_width
            combined.append(f"{c1}  {c2}  {c3}")
        
        for line in combined:
            print(center(line, width))
        
        print()
        print(center(f"{W}█  Type 'b' for previous page  |  'h' for help  |  'q' to quit  █{RESET}", width))
    
    print()
    print(center(f"{M}blackti@blacktiger)-[~/BlackTiger/Page-{page}]{RESET}", width))
    print(center(f"{D}$ {RESET}", width), end="")

def run():
    page = 1
    try:
        while True:
            menu(page)
            choice = input().strip().lower()
            
            if choice == 'q':
                print(f"\n{W}Goodbye!{RESET}")
                break
            elif choice == 'blacktiger' or choice == 'bt':
                show_blacktiger()
            elif choice == 'skull':
                show_skull()
            elif choice == 'eye':
                show_eye()
            elif choice == 'l':
                print(f"\n{W}Leaving...{RESET}")
                time.sleep(1)
                break
            elif choice == 'n':
                if page == 1:
                    page = 2
                    animate_osint()
                elif page == 2:
                    page = 3
                    animate_attack()
                else:
                    print(f"\n{M}Already on last page{RESET}")
                    time.sleep(0.5)
            elif choice == 'b':
                if page == 2:
                    page = 1
                elif page == 3:
                    page = 2
                else:
                    print(f"\n{M}Already on first page{RESET}")
                    time.sleep(0.5)
            elif choice in ['01', '1']:
                import module_01_obfuscator
                module_01_obfuscator.run()
            elif choice in ['02', '2']:
                import module_02_discord_rat
                module_02_discord_rat.run()
            elif choice in ['03', '3']:
                import module_03_ransomware
                module_03_ransomware.run()
            elif choice in ['04', '4']:
                import module_04_dos
                module_04_dos.run()
            elif choice in ['05', '5']:
                import module_05_proxy
                module_05_proxy.run()
            elif choice in ['06', '6']:
                import module_06_vuln
                module_06_vuln.run()
            elif choice in ['07', '7']:
                import module_07_info
                module_07_info.run()
            elif choice in ['08', '8']:
                import module_08_url
                module_08_url.run()
            elif choice in ['09', '9']:
                import module_09_ip
                module_09_ip.run()
            elif choice in ['10']:
                import module_10_port
                module_10_port.run()
            elif choice in ['11']:
                import module_11_pinger
                module_11_pinger.run()
            elif choice in ['12']:
                import module_12_dox
                module_12_dox.run()
            elif choice in ['13']:
                import module_13_dox_tracker
                module_13_dox_tracker.run()
            elif choice in ['14']:
                import module_14_social
                module_14_social.run()
            elif choice in ['15']:
                import module_15_reverse_image
                module_15_reverse_image.run()
            elif choice in ['16']:
                import module_16_username
                module_16_username.run()
            elif choice in ['17']:
                import module_17_email_tracker
                module_17_email_tracker.run()
            elif choice in ['18']:
                import module_18_email_lookup
                module_18_email_lookup.run()
            elif choice in ['19']:
                import module_19_phone
                module_19_phone.run()
            elif choice in ['20']:
                import module_20_email_gen
                module_20_email_gen.run()
            elif choice in ['22']:
                import module_22_phishing
                module_22_phishing.run()
            elif choice in ['23']:
                import module_23_decrypt
                module_23_decrypt.run()
            elif choice in ['24']:
                import module_24_encrypt
                module_24_encrypt.run()
            elif choice in ['25']:
                import module_25_hash
                module_25_hash.run()
            elif choice in ['26']:
                import module_26_db
                module_26_db.run()
            elif choice in ['27']:
                import module_27_darkweb
                module_27_darkweb.run()
            elif choice in ['28']:
                import module_28_ipgen
                module_28_ipgen.run()
            elif choice in ['29']:
                import module_29_stealer
                module_29_stealer.run()
            elif choice in ['30']:
                import module_30_malware
                module_30_malware.run()
            elif choice in ['31']:
                import module_31_token
                module_31_token.run()
            elif choice in ['32']:
                import module_32_bot
                module_32_bot.run()
            elif choice in ['33']:
                import module_33_webhook
                module_33_webhook.run()
            elif choice in ['34']:
                import module_34_server
                module_34_server.run()
            elif choice in ['35']:
                import module_35_nitro
                module_35_nitro.run()
            elif choice in ['36']:
                import module_36_roblox_cookie
                module_36_roblox_cookie.run()
            elif choice in ['37']:
                import module_37_roblox_info
                module_37_roblox_info.run()
            elif choice in ['38']:
                import module_38_roblox_user
                module_38_roblox_user.run()
            elif choice in ['39']:
                import module_39_roblox_id
                module_39_roblox_id.run()
            elif choice in ['40']:
                import module_40_system
                module_40_system.run()
            elif choice in ['41']:
                import module_41_udp
                module_41_udp.run()
            elif choice in ['51']:
                import module_51_whois
                module_51_whois.run()
            elif choice in ['52']:
                import module_52_dns
                module_52_dns.run()
            elif choice in ['53']:
                import module_53_subdomain
                module_53_subdomain.run()
            elif choice in ['54']:
                import module_54_geolocation
                module_54_geolocation.run()
            elif choice in ['55']:
                import module_55_sslchecker
                module_55_sslchecker.run()
            elif choice in ['56']:
                import module_56_portscan
                module_56_portscan.run()
            elif choice in ['57']:
                import module_57_shodan
                module_57_shodan.run()
            elif choice in ['58']:
                import module_58_censys
                module_58_censys.run()
            elif choice in ['59']:
                import module_59_wayback
                module_59_wayback.run()
            elif choice in ['60']:
                import module_60_emailrep
                module_60_emailrep.run()
            elif choice in ['70']:
                import module_70_arpspoof
                module_70_arpspoof.run()
            elif choice in ['71']:
                import module_71_dnsspoof
                module_71_dnsspoof.run()
            elif choice in ['72']:
                import module_72_macflood
                module_72_macflood.run()
            elif choice in ['73']:
                import module_73_dhcpstarve
                module_73_dhcpstarve.run()
            elif choice in ['74']:
                import module_74_icmpredirect
                module_74_icmpredirect.run()
            elif choice in ['75']:
                import module_75_synflood
                module_75_synflood.run()
            elif choice in ['76']:
                import module_76_udpflood
                module_76_udpflood.run()
            elif choice in ['77']:
                import module_77_httpflood
                module_77_httpflood.run()
            elif choice in ['78']:
                import module_78_slowloris
                module_78_slowloris.run()
            elif choice in ['80']:
                import module_80_netsniffer
                module_80_netsniffer.run()
            elif choice in ['81']:
                import module_81_packetsniffer
                module_81_packetsniffer.run()
            elif choice in ['82']:
                import module_82_arpsniffer
                module_82_arpsniffer.run()
            elif choice in ['83']:
                import module_83_dnssniffer
                module_83_dnssniffer.run()
            elif choice in ['84']:
                import module_84_httpsniffer
                module_84_httpsniffer.run()
            elif choice in ['85']:
                import module_85_sslsniffer
                module_85_sslsniffer.run()
            elif choice in ['86']:
                import module_86_wifisniffer
                module_86_wifisniffer.run()
            elif choice in ['87']:
                import module_87_bluetoothsniffer
                module_87_bluetoothsniffer.run()
            elif choice in ['88']:
                import module_88_usbsniffer
                module_88_usbsniffer.run()
            elif choice in ['90']:
                import module_90_portknock
                module_90_portknock.run()
            elif choice in ['91']:
                import module_91_macchanger
                module_91_macchanger.run()
            elif choice in ['92']:
                import module_92_packetgen
                module_92_packetgen.run()
            elif choice in ['93']:
                import module_93_rogueap
                module_93_rogueap.run()
            elif choice in ['94']:
                import module_94_deauth
                module_94_deauth.run()
            elif choice in ['95']:
                import module_95_beaconflood
                module_95_beaconflood.run()
            elif choice in ['96']:
                import module_96_eviltwin
                module_96_eviltwin.run()
            elif choice in ['97']:
                import module_97_karma
                module_97_karma.run()
            elif choice in ['98']:
                import module_98_proberequest
                module_98_proberequest.run()
            elif choice == 'h':
                print(f"\n{W}Help:{RESET}")
                print(f"{M}Enter the number of the module you want to run{RESET}")
                print(f"{M}Type 'n' for next page, 'b' for previous page{RESET}")
                print(f"{M}Type 'blacktiger' or 'bt' for BlackTiger logo{RESET}")
                print(f"{M}Type 'skull' for Skull art{RESET}")
                print(f"{M}Type 'eye' for Eye art{RESET}")
                print(f"{M}Type 'l' to leave{RESET}")
                print(f"{M}Type 'q' to quit{RESET}")
                time.sleep(3)
            else:
                print(f"\n{W}Invalid choice!{RESET}")
                time.sleep(1)
                
    except KeyboardInterrupt:
        print(f"\n{W}Exiting...{RESET}")
        sys.exit(0)
    except Exception as e:
        print(f"\n{W}Error: {e}{RESET}")
        time.sleep(2)

if __name__ == "__main__":
    run()
