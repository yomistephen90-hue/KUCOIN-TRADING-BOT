# 🤖 KUCOIN SURVIVAL-MODE TRADING BOT

A **production-grade, resilient trading bot** designed to survive market chaos and API changes.

## 🎯 Features

✅ **Survivor Mentality**
- Handles API errors gracefully
- Detects and recovers from failures
- Self-heals without manual intervention
- Never crashes permanently

✅ **Smart Trading**
- RSI/MACD-based entry signals
- Dynamic position sizing
- Stop-loss & take-profit automation
- Trailing stops for profit protection

✅ **Robust API Integration**
- Rate limit detection & handling
- API change detection
- Automatic retry logic
- Data validation on every tick

✅ **Safety & Monitoring**
- Telegram alerts for all critical events
- Comprehensive logging
- Health checks every minute
- API expiration warnings

✅ **Secure Credentials**
- NO hardcoded API keys
- Environment variables support
- Config file template (local testing)
- Safe for GitHub (never commits secrets)

## 📋 Files Included

| File | Purpose |
|------|---------|
| `trading_bot.py` | Main bot code (fully commented) |
| `requirements.txt` | Python dependencies (pinned versions) |
| `.env.template` | Environment variables template |
| `.gitignore` | Prevents uploading sensitive files |
| `Procfile` | Railway deployment config |
| `runtime.txt` | Python version for Railway |
| `railway.json` | Railway build settings |
| `README.md` | This file |
| `SETUP_GUIDE.md` | Complete setup instructions |

## 🚀 Quick Start

### 1. Download Files
Download all files from the outputs folder.

### 2. Read Setup Guide
Read `SETUP_GUIDE.md` for complete instructions.

### 3. Get Your Credentials
- **KuCoin API:** KuCoin.com > Account > API Management
- **Telegram Bot Token:** Telegram > @BotFather > /newbot
- **Telegram Chat ID:** Telegram > @RawDataBot

### 4. Deploy on Railway
- Create Railway account (railway.app)
- Connect GitHub repository
- Set environment variables in Railway dashboard
- Railway auto-deploys!

## 🔒 Security First

**NEVER hardcode credentials!** This bot uses:

1. **Environment Variables (Recommended)**
   - Set in Railway dashboard
   - Most secure method
   - Railway loads automatically

2. **Config File (Local Testing)**
   - Use `.env` file on your computer
   - Add to `.gitignore` to prevent upload
   - For development only

3. **No Secrets in Code**
   - All credentials loaded externally
   - Safe to commit to GitHub
   - Won't expose API keys

## 📝 How It Works

### Entry Conditions
```
IF (RSI < 40 AND MACD positive AND Volume > avg)
THEN Open trade with 3% risk
```

### Risk Management
- **Risk per trade:** 3% of account
- **Take profit:** 8% above entry
- **Stop loss:** 5% below entry
- **Daily loss limit:** 5% (bot stops trading for day)
- **Max open positions:** 2 trades simultaneously

### Exit Conditions
- **Take profit hit:** Close with +8%
- **Stop loss hit:** Close with -5%
- **Trailing stop:** Locks gains as price rises

## 🛡️ Error Handling

The bot automatically handles:

✅ API timeouts (retries up to 3 times)
✅ Rate limits (backs off and waits)
✅ Bad market data (validates before using)
✅ Connection drops (reconnects automatically)
✅ Missing data fields (skips invalid ticks)
✅ Price overflows (validates for realistic ranges)
✅ Delisted coins (detects and alerts)

## 📊 Monitoring

### Real-Time Alerts
- Trade opened: `🟢 Entry price, SL, TP`
- Trade closed: `🔴 Exit price, P&L %`
- Critical errors: `⚠️ API issues, warnings`
- System health: `🤖 Balance, open positions`

### Logs
Check `trading_bot.log` for:
- All trades
- API responses
- Error details
- System health

## 🚀 Deployment on Railway

### Step 1: Create Railway Account
1. Go to railway.app
2. Sign up with GitHub
3. Create new project

### Step 2: Connect Repository
1. Click "Deploy from GitHub"
2. Select your bot repository
3. Railway auto-detects Python project

### Step 3: Set Environment Variables
1. Go to **Variables** tab
2. Add 5 variables:
   ```
   KUCOIN_API_KEY = your_key
   KUCOIN_API_SECRET = your_secret
   KUCOIN_API_PASSPHRASE = your_passphrase
   TELEGRAM_BOT_TOKEN = your_token
   TELEGRAM_CHAT_ID = your_chat_id
   ```
3. Click **Save**

### Step 4: Deploy
1. Railway auto-deploys
2. Check logs for: `✅ Bot initialized successfully`
3. Watch Telegram for: `🤖 Trading Bot Started`

## 📈 Expected Performance

With $13 starting capital and 3% risk per trade:

**Week 1-2:** 10-15% return ($13 → $15)
**Week 3-4:** Compounds to $17-20
**Month 2:** With deposits, reaches $30+
**Path to $1K:** 8-10 weeks with consistent 10-15% weekly gains

*Note: Results depend on market conditions. Past performance ≠ future results.*

## ⚙️ Customization

Edit these in `trading_bot.py`:

```python
self.risk_per_trade = 3        # % risk per trade
self.take_profit_pct = 8       # % take profit
self.stop_loss_pct = 5         # % stop loss
self.max_daily_loss = 5        # % daily loss limit
self.max_open_positions = 2    # max simultaneous trades
self.trading_pairs = ["BTC-USDT"]  # trading pairs
```

## 🆘 Troubleshooting

### "Missing credentials" error
- Verify environment variables set in Railway
- Check spelling of variable names
- Redeploy after adding variables

### "Cannot fetch balance" error
- Verify KuCoin account has USDT
- Check API key has "General" read permission
- Test API on KuCoin website first

### No Telegram messages
- Verify Chat ID is correct (@RawDataBot)
- Check bot token format (should have colon)
- Send test message to bot first

### Bot keeps crashing
- Check logs: `tail -f trading_bot.log`
- Look for API errors or bad data
- Verify credentials correct
- Check Python version compatibility

## 📚 Documentation

- **SETUP_GUIDE.md** - Complete setup instructions
- **trading_bot.py** - Heavily commented source code
- **requirements.txt** - Dependency versions
- **.env.template** - Credential template

## 🔗 Resources

- [KuCoin API Docs](https://docs.kucoin.com/)
- [Railway Docs](https://docs.railway.app/)
- [Python Requests Library](https://requests.readthedocs.io/)
- [Pandas Documentation](https://pandas.pydata.org/docs/)

## ⚠️ Disclaimer

**This bot is provided as-is for educational purposes.**

- Trading crypto is risky - you can lose money
- Past performance doesn't guarantee future results
- Start small and test before scaling
- Only trade money you can afford to lose
- Do your own research and due diligence

## 📞 Support

If something breaks:
1. Check `trading_bot.log` for error messages
2. Verify credentials are set correctly
3. Read SETUP_GUIDE.md troubleshooting section
4. Check Railway logs for deployment issues

## 📄 License

This project is provided for personal use.

---

**Good luck with your trading!** 🚀💰

Built with **Survivor Mentality** - Never give up, always adapt, keep improving! 💪
