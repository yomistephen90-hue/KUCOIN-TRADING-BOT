import os
import json
import sys

print("=" * 70)
print("DETAILED CREDENTIAL TEST")
print("=" * 70)

# Step 1: Check environment variables
print("\n[STEP 1] Checking Environment Variables:")
api_key_env = os.getenv('KUCOIN_API_KEY')
api_secret_env = os.getenv('KUCOIN_API_SECRET')
api_passphrase_env = os.getenv('KUCOIN_API_PASSPHRASE')

if api_key_env:
    print(f"  ✅ KUCOIN_API_KEY found in environment")
else:
    print(f"  ❌ KUCOIN_API_KEY not in environment")

# Step 2: Try loading config file
print("\n[STEP 2] Checking kucoin_config.json file:")
try:
    with open('kucoin_config.json', 'r') as f:
        config = json.load(f)
    print(f"  ✅ File exists and is valid JSON")
    
    # Step 3: Check each field
    print("\n[STEP 3] Checking all 5 required fields:")
    
    fields = [
        'KUCOIN_API_KEY',
        'KUCOIN_API_SECRET', 
        'KUCOIN_API_PASSPHRASE',
        'TELEGRAM_BOT_TOKEN',
        'TELEGRAM_CHAT_ID'
    ]
    
    all_present = True
    for field in fields:
        value = config.get(field)
        if value and len(str(value).strip()) > 0:
            print(f"  ✅ {field}: Found ({len(str(value))} chars)")
        else:
            print(f"  ❌ {field}: MISSING or EMPTY")
            all_present = False
    
    # Step 4: Summary
    print("\n" + "=" * 70)
    if all_present:
        print("✅ SUCCESS! All credentials loaded from kucoin_config.json")
        print("The bot SHOULD work now!")
        sys.exit(0)
    else:
        print("❌ FAILED! Some fields are missing or empty")
        print("Edit kucoin_config.json and fill in all fields!")
        sys.exit(1)

except FileNotFoundError:
    print(f"  ❌ kucoin_config.json NOT FOUND in current directory")
    print(f"  Current directory: {os.getcwd()}")
    sys.exit(1)
    
except json.JSONDecodeError as e:
    print(f"  ❌ JSON FORMATTING ERROR: {e}")
    print(f"  The file is not valid JSON!")
    sys.exit(1)
    
except Exception as e:
    print(f"  ❌ UNEXPECTED ERROR: {e}")
    sys.exit(1)

print("=" * 70)