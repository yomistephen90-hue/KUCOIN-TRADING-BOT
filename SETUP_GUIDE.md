# KUCOIN TRADING BOT - SECURE SETUP GUIDE

## 🔒 SECURITY FIRST - How to Safely Input Your API Keys

This guide shows you how to set up the bot **WITHOUT hardcoding credentials in code**.

---

## 📋 Prerequisites

- ✅ KuCoin account with API keys created
- ✅ Telegram Bot Token (from @BotFather)
- ✅ Telegram Chat ID (from @RawDataBot)
- ✅ Python 3.8+ installed (or PythonAnywhere account)

---

## 🚀 Setup Option 1: Local Computer (Windows/Mac/Linux)

### Step 1: Create Configuration File

1. In your `trading-bot` folder, create a new file: `kucoin_config.json`
2. Copy this template:

```json
{
  "KUCOIN_API_KEY": "YOUR_KUCOIN_API_KEY_HERE",
  "KUCOIN_API_SECRET": "YOUR_KUCOIN_API_SECRET_HERE",
  "KUCOIN_API_PASSPHRASE": "YOUR_KUCOIN_API_PASSPHRASE_HERE",
  "TELEGRAM_BOT_TOKEN": "YOUR_TELEGRAM_TOKEN_HERE",
  "TELEGRAM_CHAT_ID": "YOUR_TELEGRAM_CHAT_ID_HERE"
}
```

3. **Replace each `YOUR_XXX_HERE` with your actual credentials**
4. **Save the file**

### Step 2: Protect the File

Add to `.gitignore` to prevent accidental upload:

```
kucoin_config.json
.env
*.log
trades.csv
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Test the Bot

```bash
python trading_bot_kucoin_secure.py
```

---

## ☁️ Setup Option 2: PythonAnywhere (Cloud Hosting)

### Step 1: Upload Files

1. Go to PythonAnywhere.com
2. Go to Files tab
3. Create folder: `trading-bot`
4. Upload:
   - `trading_bot_kucoin_secure.py`
   - `requirements.txt`

### Step 2: Set Environment Variables (RECOMMENDED)

This is **MORE SECURE** than using a config file!

1. In PythonAnywhere, go to **Account** → **Environment Variables**
2. Add these 5 variables:

```
KUCOIN_API_KEY = your_kucoin_api_key
KUCOIN_API_SECRET = your_kucoin_api_secret
KUCOIN_API_PASSPHRASE = your_kucoin_passphrase
TELEGRAM_BOT_TOKEN = your_telegram_token
TELEGRAM_CHAT_ID = your_telegram_chat_id
```

3. **Save**

### Step 3: Install Dependencies

Open PythonAnywhere console and run:

```bash
pip install --user -r requirements.txt
```

### Step 4: Create Scheduled Task

1. Go to **Scheduled tasks**
2. Click **Create a new scheduled task**
3. Set time: **00:01** (1 minute after midnight)
4. Command:
```bash
python /home/YourUsername/trading-bot/trading_bot_kucoin_secure.py
```

5. **Save**

---

## 🌊 Setup Option 3: Railway (Cloud Hosting)

### Step 1: Create Railway Project

1. Go to Railway.app
2. Connect your GitHub repo
3. Railway auto-deploys

### Step 2: Set Environment Variables on Railway

1. Go to **Variables** tab
2. Add the 5 environment variables (same as PythonAnywhere)
3. **Save**
4. Click **Redeploy**

---

## 🔑 Where to Get Each Credential

### KuCoin API Key, Secret, Passphrase

1. Login to KuCoin.com
2. Click avatar (top right) → **Account**
3. Click **API Management**
4. Click **Create API**
5. Fill form:
   - **Name:** `TradingBot`
   - **Permissions:** Check `General` (read), `Spot Trading` (buy/sell)
   - **Passphrase:** Create a secure passphrase (7-32 characters)
6. Click **Create**
7. You'll see:
   - **API Key** ← Copy this
   - **API Secret** ← Copy this
   - **API Passphrase** ← The one you created

### Telegram Bot Token

1. Open Telegram
2. Search for **@BotFather**
3. Send: `/newbot`
4. Follow prompts to create bot
5. You'll get: `123456:ABC-DEF1234...` ← **This is your token**

### Telegram Chat ID

1. Open Telegram
2. Search for **@RawDataBot**
3. Send any message
4. Bot replies with your info
5. Find `"id": 1234567890` ← **This is your Chat ID**

---

## 📝 How the Bot Loads Credentials

The bot automatically tries these methods in order:

1. **Environment Variables** (Most secure - PythonAnywhere/Railway)
   - Looks for: `KUCOIN_API_KEY`, `KUCOIN_API_SECRET`, etc.
   - No file needed!

2. **Config File** (Local testing)
   - Looks for: `kucoin_config.json`
   - Only reads if env vars not found
   - Keep this file private!

3. **Error if Neither Found**
   - Bot exits with clear error message

---

## 🛡️ Security Best Practices

✅ **DO:**
- Use environment variables on cloud hosting
- Keep `kucoin_config.json` private
- Add to `.gitignore`
- Regenerate API keys if compromised
- Use unique, strong API passphrases
- Restrict API permissions in KuCoin (read-only where possible)

❌ **DON'T:**
- Paste credentials in chat/emails/public forums
- Commit config files to GitHub
- Share API keys with anyone
- Use same passphrase across services
- Enable withdrawal permissions on API key

---

## 🧪 Test Your Setup

### Test 1: Check Credentials Load

Create file `test_credentials.py`:

```python
import os
import json

# Try environment variables
api_key = os.getenv('KUCOIN_API_KEY')
print(f"Env var loaded: {api_key is not None}")

# Try config file
try:
    with open('kucoin_config.json') as f:
        config = json.load(f)
        print(f"Config file loaded: {config.get('KUCOIN_API_KEY') is not None}")
except:
    print("Config file not found")
```

Run: `python test_credentials.py`

### Test 2: Check Bot Starts

```bash
python trading_bot_kucoin_secure.py
```

Should see:
```
✅ Bot initialized successfully
🤖 Trading Bot Started (Telegram message)
Balance: $X.XX
```

---

## 🆘 Troubleshooting

### "Missing credentials" Error

**Solution:**
- Verify environment variables are set (if using cloud)
- Verify `kucoin_config.json` exists and filled correctly (if using local)
- Check no extra spaces in credentials

### "Invalid API credentials" Error

**Solution:**
- Copy API key/secret EXACTLY from KuCoin (no extra spaces)
- Make sure API key not expired
- Verify passphrase matches what KuCoin has

### "Cannot fetch balance" Error

**Solution:**
- Check KuCoin account has USDT balance
- Verify API has "General" read permission
- Try API test on KuCoin dashboard first

### Bot doesn't send Telegram messages

**Solution:**
- Verify Telegram Chat ID is correct
- Send a test message to your bot first
- Check bot token format (should have colon)

---

## 📊 What Comes Next

Once setup is complete, the bot will:

✅ Monitor your account balance
✅ Check KuCoin API health
✅ Detect rate limits
✅ Send Telegram alerts
✅ Log all activity
✅ Eventually trade BTC/USDT

Check logs:
```bash
tail -f trading_bot.log  # View live logs
```

---

## 🎯 Summary

| Step | What | Where |
|------|------|-------|
| 1 | Get API credentials | KuCoin website |
| 2 | Set up credentials | Config file or env vars |
| 3 | Install dependencies | `pip install -r requirements.txt` |
| 4 | Test setup | `python trading_bot_kucoin_secure.py` |
| 5 | Monitor | Check logs and Telegram alerts |

---

## ✅ Ready?

You now have a **secure, production-grade trading bot** that:
- ✅ Never hardcodes secrets
- ✅ Handles API errors gracefully
- ✅ Sends critical alerts
- ✅ Logs everything
- ✅ Self-recovers from failures

**Good luck with your trading!** 🚀💰
