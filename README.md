
# 🐅 BLACKTIGER PRO V2.0

### The Ultimate All-in-One Penetration Testing & OSINT Toolkit

[![Version](https://img.shields.io/badge/version-2.0-red.svg)](https://github.com/BOB7822/BLACKTIGER-V2)
[![Python](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Discord](https://img.shields.io/badge/Discord-join-7289DA.svg)](https://discord.gg/nvbQsxFJgz)

</div>

---

## 📌 Overview

**BLACKTIGER PRO V2.0** is a powerful, modular penetration testing and OSINT framework with over **80+ tools** organized into three main categories:

- **Network Scanning** - Vulnerability scanners, port scanners, IP tools
- **OSINT** - Social media intelligence, data gathering, email/phone lookup
- **Attack Tools** - Flood attacks, sniffers, spoofing, exploitation

All tools are accessible through an elegant terminal-based menu system with animated boot sequences and ASCII art.

---

## ✨ Features

### 🔍 Network Scanner

| Module | Description |
|--------|-------------|
| `[06]` | Web Vulnerability Scanner |
| `[07]` | Web Info Scanner |
| `[08]` | Web URL Scanner |
| `[09]` | IP Scanner |
| `[10]` | Port Scanner |
| `[11]` | IP Pinger |

### 🔎 OSINT Tools

| Module | Description |
|--------|-------------|
| `[12]` | DOX Creator |
| `[13]` | DOX Tracker |
| `[14]` | Social Media Search |
| `[15]` | Reverse Image Search |
| `[16]` | Username Tracker |
| `[17]` | Email Tracker |
| `[18]` | Email Lookup |
| `[19]` | Phone Lookup |
| `[20]` | 10-Minute Email Generator |
| `[51]` | WHOIS Lookup |
| `[52]` | DNS Lookup |
| `[53]` | Subdomain Scanner |
| `[54]` | IP Geolocation |
| `[55]` | SSL Certificate Checker |
| `[57]` | Shodan Search |
| `[59]` | Wayback Machine |

### 💀 Attack Tools

| Module | Description |
|--------|-------------|
| `[04]` | DOS Attack |
| `[41]` | UDP Flooder |
| `[75]` | SYN Flood |
| `[76]` | UDP Flood |
| `[77]` | HTTP Flood |
| `[78]` | Slowloris |
| `[70]` | ARP Spoofing |
| `[71]` | DNS Spoofing |
| `[80]` | Network Sniffer |
| `[90]` | Port Knocking |
| `[91]` | MAC Changer |
| `[94]` | Deauth Attack |

### 🛠️ Malware Builder

| Module | Description |
|--------|-------------|
| `[02]` | Discord RAT |
| `[03]` | Ransomware (AES-256) |
| `[29]` | Stealer |
| `[30]` | Reverse Shell / Keylogger |

### 🎮 Gaming Tools

| Module | Description |
|--------|-------------|
| `[36]` | Roblox Cookie Login |
| `[37]` | Roblox Cookie Info |
| `[38]` | Roblox User Info |
| `[39]` | Roblox ID Info |

### 💬 Discord Tools

| Module | Description |
|--------|-------------|
| `[31]` | Token Discord Checker |
| `[32]` | Bot Discord Checker |
| `[33]` | Webhook Discord Spammer |
| `[34]` | Discord Server Info |
| `[35]` | Nitro Generator |

---

## 🚀 Installation

### One-Liner Install

```bash
git clone https://github.com/BOB7822/BLACKTIGER-V2.git ~/blacktiger && cd ~/blacktiger && python3 main_menu.py

With Dependencies
bash

git clone https://github.com/BOB7822/BLACKTIGER-V2.git ~/blacktiger && cd ~/blacktiger && pip3 install -r requirements.txt && python3 main_menu.py

Manual Install
bash

# Clone the repository
git clone https://github.com/BOB7822/BLACKTIGER-V2.git

# Navigate to directory
cd BLACKTIGER-V2

# Install dependencies
pip3 install -r requirements.txt

# Run the tool
python3 main_menu.py

Install Dependencies Manually
bash

pip3 install requests cryptography flask pillow phonenumbers faker psutil pyinstaller dnspython

Create Alias (Optional)
bash

echo 'alias blacktiger="cd ~/blacktiger && python3 main_menu.py"' >> ~/.bashrc && source ~/.bashrc

🎮 Usage
Navigation
Key	Action
n	Next page
b	Previous page
h	Help
q	Quit
Special Commands
Command	Action
blacktiger or bt	Show BlackTiger logo
skull	Show skull ASCII art
eye	Show eye ASCII art
l	Leave/Exit
Example
text

$ python3 main_menu.py

█  Type 'n' for next page (OSINT)  |  'h' for help  |  'q' to quit  █

blackti@blacktiger)-[~/BlackTiger/Page-1]
$ 12  # Runs DOX Creator

📁 Project Structure
text

BLACKTIGER-V2/
├── main_menu.py          # Main launcher with menu
├── module_XX_*.py        # Individual modules (80+ files)
├── install.py            # Dependency installer
├── requirements.txt      # Python dependencies
└── README.md             # This file

🔧 Requirements

    Python 3.8 or higher

    Linux / macOS / Windows (with WSL)

    pip3

    Git

🛠️ Module List
Page 1 - Main Menu (Network, Utilities, Malware)
Code	Module
01	Python Obfuscator
02	Discord RAT Builder
03	Ransomware Builder
04	DOS Attack
05	Proxy Scraper
06	Web Vuln Scanner
07	Web Info Scanner
08	Web URL Scanner
09	IP Scanner
10	Port Scanner
11	IP Pinger
22	Phishing Attack
23	Password Decrypt
24	Password Encrypt
25	Hash Generator
26	Search Database
27	Dark Web Links
28	IP Generator
29	Stealer
30	FUD Malware Gen
31	Token Discord
32	Bot Discord
33	Webhook Discord
34	Discord Server
35	Nitro Generator
40	System Info
41	UDP Flooder
Page 2 - OSINT & Gaming Tools
Code	Module
12	Dox Create
13	Dox Tracker
14	Social Media Search
15	Reverse Image Search
16	Username Tracker
17	Email Tracker
18	Email Lookup
19	Phone Lookup
20	10 Min Email Gen
21	Instagram Info
36	Roblox Cookie
37	Roblox Info
38	Roblox User
39	Roblox ID
51	WHOIS Lookup
52	DNS Lookup
53	Subdomain Scanner
54	IP Geolocation
55	SSL Checker
56	Port Scanner
57	Shodan Search
58	Censys Search
59	Wayback Machine
60	Email Reputation
Page 3 - Attack Tools
Code	Module
70	ARP Spoofing
71	DNS Spoofing
72	MAC Flooding
73	DHCP Starvation
74	ICMP Redirect
75	SYN Flood
76	UDP Flood
77	HTTP Flood
78	Slowloris
80	Network Sniffer
81	Packet Sniffer
82	ARP Sniffer
83	DNS Sniffer
84	HTTP Sniffer
85	SSL Sniffer
86	WiFi Sniffer
87	Bluetooth Sniffer
88	USB Sniffer
90	Port Knocking
91	MAC Changer
92	Packet Generator
93	Rogue AP
94	Deauth Attack
95	Beacon Flood
96	Evil Twin
97	Karma Attack
98	Probe Request Flood
⚠️ Legal Disclaimer

    WARNING: This tool is for educational and authorized testing purposes only.

        Do not use on systems you do not own or have explicit permission to test

        The authors are not responsible for any misuse or damage caused

        Always comply with local laws and regulations

    By using this tool, you agree to these terms.

🛡️ Security Recommendations

    Run in a isolated environment (VM, container)

    Use VPN when performing external tests

    Never share logs or data collected

    Always get written permission before testing

🤝 Contributing

    Fork the repository

    Create a feature branch (git checkout -b feature/amazing-feature)

    Commit your changes (git commit -m 'Add some amazing feature')

    Push to the branch (git push origin feature/amazing-feature)

    Open a Pull Request

📞 Contact & Support
Platform	Link
Discord	Discord.gg/nvbQsxFJgz
GitHub	BOB7822
Issues	Report Bug
🙏 Acknowledgments

    All open-source contributors

    Security community for testing and feedback

    Discord community for support

<div align="center">

Made with ❤️ by BOB

⬆ Back to Top
