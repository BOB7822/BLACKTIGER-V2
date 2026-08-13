#!/usr/bin/env python3
# Phone Lookup Module

def run():
    print("\n" + "="*60)
    print("PHONE LOOKUP")
    print("="*60)
    
    num = input("Phone (with country code): ").strip()
    
    try:
        import phonenumbers
        from phonenumbers import carrier, geocoder
        p = phonenumbers.parse(num)
        print(f"Country: {geocoder.description_for_number(p, 'en')}")
        print(f"Carrier: {carrier.name_for_number(p, 'en')}")
        print(f"Valid: {phonenumbers.is_valid_number(p)}")
    except Exception as e:
        print(f"Error: {e}")
        print("Install phonenumbers: pip install phonenumbers")

if __name__ == "__main__":
    run()