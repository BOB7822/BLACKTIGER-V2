#!/usr/bin/env python3
# BlackTiger Installer - Auto-installs all dependencies

import os
import sys
import subprocess
import platform

def install_dependencies():
    print("="*60)
    print("BLACK TIGER - DEPENDENCY INSTALLER")
    print("="*60)
    
    deps = [
        'requests',
        'cryptography',
        'flask',
        'pillow',
        'phonenumbers',
        'faker',
        'psutil',
        'pyinstaller',
        'dnspython',
        'scapy',
        'netifaces',
        'colorama',
        'termcolor'
    ]
    
    print("\nInstalling dependencies...\n")
    
    for dep in deps:
        print(f"Installing {dep}...")
        subprocess.run([sys.executable, "-m", "pip", "install", dep], capture_output=True)
    
    print("\nAll dependencies installed!")
    print("Run: python3 main_menu.py")

if __name__ == "__main__":
    install_dependencies()