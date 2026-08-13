#!/usr/bin/env python3
# System Info Module

import platform, os, socket

def run():
    print("\n" + "="*60)
    print("SYSTEM INFO")
    print("="*60)
    
    info = {
        'OS': platform.system(),
        'Version': platform.release(),
        'Hostname': platform.node(),
        'Python': sys.version,
        'User': os.getlogin(),
        'CPU': os.cpu_count(),
        'IP': socket.gethostbyname(socket.gethostname()),
    }
    
    try:
        import psutil
        info['RAM'] = f"{psutil.virtual_memory().total / 1024**3:.2f} GB"
        info['Disk'] = f"{psutil.disk_usage('/').total / 1024**3:.2f} GB"
    except:
        pass
    
    for k, v in info.items():
        print(f"  {k}: {v}")

if __name__ == "__main__":
    run()