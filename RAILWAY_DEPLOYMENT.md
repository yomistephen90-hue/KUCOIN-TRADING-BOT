# 🚀 RAILWAY DEPLOYMENT GUIDE

Complete step-by-step guide to deploy your trading bot on Railway.

## ✅ Prerequisites

- ✅ GitHub account (with bot files in a repository)
- ✅ Railway account (railway.app)
- ✅ KuCoin API credentials
- ✅ Telegram Bot Token & Chat ID

## 🎯 Step 1: Prepare Your GitHub Repository

### 1.1 Create GitHub Repository

1. Go to github.com
2. Click "New repository"
3. Name: `kucoin-trading-bot`
4. Description: "Automated KuCoin Trading Bot"
5. Click "Create repository"

### 1.2 Upload Bot Files

Push these files to GitHub:
- `trading_bot.py`
- `requirements.txt`
- `.gitignore`
- `Procfile`
- `runtime.txt`
- `railway.json`
- `README.md`

```bash
cd your-bot-folder
git init
git add .
git commit -m "Initial commit - trading bot"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/kucoin-trading-bot.git
git push -u origin main
```

### 1.3 Verify Files on GitHub

Go to github.com/YOUR_USERNAME/kucoin-trading-bot and confirm all files are there.

---

## 🚀 Step 2: Set Up Railway

### 2.1 Create Railway Account

1. Go to railway.app
2. Click "Start New Project"
3. Sign up with GitHub (recommended)
4. Authorize Railway to access your GitHub

### 2.2 Create New Project

1. Click "New Project"
2. Select "Deploy from GitHub"
3. Search for `kucoin-trading-bot`
4. Click to select it
5. Railway auto-detects Python project

### 2.3 Wait for Initial Deploy

Railway will:
- ✅ Download your files
- ✅ Install Python 3.11
- ✅ Install dependencies
- ✅ Build the project

Watch the "Deployments" tab for progress.

---

## 🔑 Step 3: Set Environment Variables

**THIS IS THE MOST IMPORTANT STEP!**

Railway needs your credentials to run the bot.

### 3.1 Navigate to Variables

1. In Railway project, click **"Variables"** tab
2. You should see "No Environment Variables"

### 3.2 Add KUCOIN_API_KEY

1. Click **"+ New Variable"**
2. **Name:** `KUCOIN_API_KEY`
3. **Value:** Paste your KuCoin API Key (from KuCoin.com > API Management)
4. Click ✓ or press Enter

### 3.3 Add KUCOIN_API_SECRET

1. Click **"+ New Variable"**
2. **Name:** `KUCOIN_API_SECRET`
3. **Value:** Paste your KuCoin API Secret
4. Click ✓

### 3.4 Add KUCOIN_API_PASSPHRASE

1. Click **"+ New Variable"**
2. **Name:** `KUCOIN_API_PASSPHRASE`
3. **Value:** Paste your KuCoin API Passphrase (the one you created)
4. Click ✓

### 3.5 Add TELEGRAM_BOT_TOKEN

1. Click **"+ New Variable"**
2. **Name:** `TELEGRAM_BOT_TOKEN`
3. **Value:** Paste your Telegram Bot Token (from @BotFather)
4. Click ✓

### 3.6 Add TELEGRAM_CHAT_ID

1. Click **"+ New Variable"**
2. **Name:** `TELEGRAM_CHAT_ID`
3. **Value:** Paste your Telegram Chat ID (from @RawDataBot)
4. Click ✓

### 3.7 Save Variables

All 5 variables should now show in the Variables list.

---

## 🔄 Step 4: Trigger Deployment

### 4.1 Redeploy with New Variables

1. Go to **"Deployments"** tab
2. Click the latest deployment
3. Click **"Redeploy"**
4. Railway rebuilds with your credentials

### 4.2 Watch the Logs

1. Click **"Deploy Logs"** tab
2. You should see:
   ```
   2026-02-15 16:27:03 - INFO - Trading Bot Initialized Successfully
   2026-02-15 16:27:03 - INFO - Starting trading bot...
   2026-02-15 16:27:03 - INFO - Telegram message sent
   2026-02-15 16:27:25 - INFO - Balance: $3.00 | Open Positions: 0
   ```

---

## ✅ Step 5: Verify Deployment

### 5.1 Check Telegram

Your bot should have sent a message to Telegram saying:
```
🤖 Trading Bot Started
```

If you got this message, your bot is **LIVE and trading!** 🎉

### 5.2 Monitor Logs

Keep watching the logs for:
- ✅ "Balance: $X.XX" (bot can fetch your account)
- ✅ "Trading Bot Started" (bot is running)
- ❌ Any error messages (fix if found)

### 5.3 Check for Trades

Your bot will:
1. Monitor BTC-USDT every 60 seconds
2. Wait for entry signal (RSI < 40, MACD positive, volume up)
3. When signal hits: Open trade with 3% risk
4. Send Telegram alert: 🟢 TRADE OPENED
5. Monitor position for TP/SL/trailing stop
6. Close trade and send alert: 🔴 TRADE CLOSED

---

## 🔧 Troubleshooting

### Problem: "Missing credentials" error

**Solution:**
1. Go to Variables tab
2. Verify all 5 variables are present
3. Check spelling exactly (KUCOIN_API_KEY, not kucoin_api_key)
4. No extra spaces in values
5. Click "Redeploy"

### Problem: "Cannot fetch balance" error

**Solution:**
1. Check KuCoin API key is correct
2. Verify API has "General" read permission
3. Verify API has "Spot Trading" permission
4. Test API on KuCoin website first
5. Regenerate API key if needed

### Problem: Bot not sending Telegram messages

**Solution:**
1. Verify Telegram Chat ID is correct (just numbers)
2. Verify Telegram Bot Token has colon (123456:ABC...)
3. Send test message to your Telegram bot first
4. Check Variable spelling: TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID

### Problem: Bot keeps restarting

**Solution:**
1. Check Deploy Logs for error messages
2. Look for "ModuleNotFoundError" (dependency missing)
3. Verify requirements.txt is correct
4. Check Python version: should be 3.11.7

### Problem: "Connection timeout" errors

**Solution:**
1. Normal - KuCoin API sometimes slow
2. Bot has automatic retry logic
3. Watch logs - if it recovers, it's working
4. Only worry if continuous for >1 hour

---

## 🔄 Updating Your Bot

If you make changes to your code:

### 1. Push to GitHub

```bash
git add .
git commit -m "Update bot logic"
git push origin main
```

### 2. Railway Auto-Deploys

Railway detects GitHub changes and auto-deploys (takes 2-5 minutes).

### 3. Monitor Logs

Watch Deploy Logs to confirm update went live.

---

## 📊 Monitoring Your Bot

### Real-Time Logs

1. Go to Railway project
2. Click **"Deploy Logs"** tab
3. Scroll down for latest activity
4. Refresh to see new logs

### Telegram Alerts

Your bot sends messages for:
- ✅ Bot started/stopped
- ✅ Trade opened (entry signal hit)
- ✅ Trade closed (TP/SL hit)
- ✅ Critical errors (API issues)

### Performance Tracking

Logs show:
```
Balance: $3.50 | Open Positions: 1 | Daily Loss: 0.00%
```

This updates every 60 seconds.

---

## 💰 Money Transfer (Once Bot is Live)

Once your bot is running and tested on Railway:

### Transfer $3 USDT from Bybit to KuCoin

1. **Bybit:** Assets → Withdraw
2. Select: USDT, Network: TRC20
3. **KuCoin:** Get deposit address for USDT (TRC20)
4. Paste KuCoin address in Bybit
5. Amount: 3 USDT
6. Wait 5-10 minutes for arrival

### Bot Will Start Trading

Once KuCoin account has USDT balance:
1. Bot checks balance every 60 seconds
2. When signal appears → opens trade
3. Sends you Telegram alert
4. Manages trade automatically

---

## 🎯 What Happens Next

### Hour 1
- ✅ Bot reads balance ($3.00)
- ✅ Starts monitoring BTC-USDT
- ✅ Waits for entry signal

### Day 1-7
- Bot waits for right conditions
- Might open 0-5 trades depending on market
- Each trade risks 3% ($0.09)
- You get Telegram alert for each

### Week 2+
- If profitable → compounds gains
- More capital = bigger trades
- Path to $1K becomes clear

---

## ✅ Deployment Checklist

- [ ] GitHub repo created with all files
- [ ] Railway account created
- [ ] Project created and connected to GitHub
- [ ] 5 environment variables set (KUCOIN_API_KEY, etc.)
- [ ] Deployment complete (no errors in logs)
- [ ] Telegram message received: "🤖 Trading Bot Started"
- [ ] Bot shows balance in logs
- [ ] Ready to transfer $3 USDT from Bybit

---

## 🚀 You're Live!

Once all checkmarks are complete, your bot is:
- ✅ Running 24/7 on Railway
- ✅ Monitoring markets automatically
- ✅ Ready to trade
- ✅ Sending you Telegram alerts
- ✅ Logging everything

**Welcome to automated trading!** 💪💰

---

## 📞 Quick Links

- [Railway Docs](https://docs.railway.app/)
- [KuCoin API Docs](https://docs.kucoin.com/)
- [Telegram Bot API](https://core.telegram.org/bots/api)

---

**Any questions? Check the logs first - they usually tell you what's wrong!** 🔍
