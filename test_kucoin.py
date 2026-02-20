import os
import json

print("=" * 60)
print("TESTING CREDENTIAL LOADING")
print("=" * 60)

# Method 1: Environment Variables
print("\n1. Checking Environment Variables:")
api_key = os.getenv('KUCOIN_API_KEY')
api_secret = os.getenv('KUCOIN_API_SECRET')
api_passphrase = os.getenv('KUCOIN_API_PASSPHRASE')

if api_key:
    print(f"   ✅ KUCOIN_API_KEY loaded: {api_key[:10]}...")
else:
    print(f"   ❌ KUCOIN_API_KEY NOT found")

if api_secret:
    print(f"   ✅ KUCOIN_API_SECRET loaded: {api_secret[:10]}...")
else:
    print(f"   ❌ KUCOIN_API_SECRET NOT found")

if api_passphrase:
    print(f"   ✅ KUCOIN_API_PASSPHRASE loaded: {api_passphrase[:10]}...")
else:
    print(f"   ❌ KUCOIN_API_PASSPHRASE NOT found")

# Method 2: Config File
print("\n2. Checking Config File:")
try:
    with open('kucoin_config.json', 'r') as f:
        config = json.load(f)
        if config.get('KUCOIN_API_KEY'):
            print(f"   ✅ kucoin_config.json found with API key")
        else:
            print(f"   ❌ kucoin_config.json exists but no API key")
except FileNotFoundError:
    print(f"   ❌ kucoin_config.json NOT found")
except Exception as e:
    print(f"   ❌ Error reading config: {e}")

print("\n" + "=" * 60)
print("RESULT:")
if api_key and api_secret and api_passphrase:
    print("✅ All credentials loaded! Problem is elsewhere.")
else:
    print("❌ Missing credentials! Need to set environment variables or config file.")
print("=" * 60)