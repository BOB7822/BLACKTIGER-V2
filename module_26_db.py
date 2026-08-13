#!/usr/bin/env python3
# Search Database Module

import sqlite3, os

def run():
    print("\n" + "="*60)
    print("SEARCH DATABASE")
    print("="*60)
    
    search_term = input("Search term: ").strip()
    
    db_path = os.path.expanduser("~/Downloads/BlackTiger_Output/leaks.db")
    os.makedirs(os.path.dirname(db_path), exist_ok=True)
    
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    
    c.execute('''CREATE TABLE IF NOT EXISTS leaks 
                 (email TEXT, password TEXT, source TEXT)''')
    c.execute('''INSERT OR IGNORE INTO leaks VALUES 
                 ('test@test.com', '123456', 'mock')''')
    conn.commit()
    
    c.execute('SELECT * FROM leaks WHERE email LIKE ? OR password LIKE ?', 
              (f'%{search_term}%', f'%{search_term}%'))
    results = c.fetchall()
    
    if results:
        print(f"Found {len(results)} results:")
        for row in results:
            print(f"  {row}")
    else:
        print(f"No results found")
    
    conn.close()

if __name__ == "__main__":
    run()