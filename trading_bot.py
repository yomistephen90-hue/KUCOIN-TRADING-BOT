"""

BINANCE AUTOMATED TRADING BOT - SURVIVOR MODE
Production-grade trading bot with API error handling and Telegram alerts
Works with Railway - No US geo-blocking issues
KUCOIN AUTOMATED TRADING BOT - SURVIVOR MODE
Production-grade trading bot with API error handling and Telegram alerts
"""

import os
import json
import time
import logging
from datetime import datetime, timedelta
import requests
import pandas as pd
import numpy as np
import hashlib
import hmac
import base64
from typing import Dict, Optional

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('trading_bot.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)


class CredentialManager:
    """Safely loads credentials from environment variables or config file"""
    
    @staticmethod
    def load_credentials():
        """Load Binance API credentials securely"""
        

        api_key = os.getenv('BINANCE_API_KEY')
        api_secret = os.getenv('BINANCE_API_SECRET')

        api_key = os.getenv('KUCOIN_API_KEY')
        api_secret = os.getenv('KUCOIN_API_SECRET')
        api_passphrase = os.getenv('KUCOIN_API_PASSPHRASE')

        telegram_token = os.getenv('TELEGRAM_BOT_TOKEN')
        telegram_chat_id = os.getenv('TELEGRAM_CHAT_ID')
        
        if not api_key:
            try:
                with open('binance_config.json', 'r') as f:
                    config = json.load(f)
                    api_key = config.get('BINANCE_API_KEY')
                    api_secret = config.get('BINANCE_API_SECRET')
                    telegram_token = config.get('TELEGRAM_BOT_TOKEN')
                    telegram_chat_id = config.get('TELEGRAM_CHAT_ID')
            except FileNotFoundError:
                pass
        

        if not all([api_key, api_secret, telegram_token, telegram_chat_id]):

        if not all([api_key, api_secret, telegram_token, telegram_chat_id]):
            raise ValueError("Missing credentials!")
        
        return {
            'api_key': api_key,
            'api_secret': api_secret,
            'telegram_token': telegram_token,
            'telegram_chat_id': telegram_chat_id
        }



class BinanceClient:
    """Binance API client with error handling"""
class KuCoinClient:
    """KuCoin API client with error handling"""
    
    def __init__(self, api_key: str, api_secret: str):
        self.api_key = api_key
        self.api_secret = api_secret
        self.base_url = "https://api.binance.com"
        self.request_timeout = 10
        self.max_retries = 3
        self.last_request_time = 0
        self.min_request_interval = 0.1
        
    def _get_signature(self, params_str: str) -> str:
        """Generate Binance signature"""
        return hmac.new(
            self.api_secret.encode(),
            params_str.encode(),
            hashlib.sha256
        ).hexdigest()
    
    def _get_headers(self) -> Dict:
        """Get Binance request headers"""

    def _get_auth_headers(self, method: str, path: str, params: str = "") -> Dict:
        """Generate KuCoin V2 authentication headers"""
        nonce = str(int(time.time() * 1000))
        
        str_to_sign = nonce + method + path
        if params:
            str_to_sign += params
        
        signature = base64.b64encode(
            hmac.new(
                self.api_secret.encode(),
                str_to_sign.encode(),
                hashlib.sha256
            ).digest()
        ).decode()
        
        encrypted_passphrase = base64.b64encode(
            hmac.new(
                self.api_secret.encode(),
                self.api_passphrase.encode(),
                hashlib.sha256
            ).digest()
        ).decode()
        
        return {
            'X-MBX-APIKEY': self.api_key,
            'Content-Type': 'application/x-www-form-urlencoded'
        }
    
    def _rate_limit_check(self):
        """Enforce rate limiting"""
        elapsed = time.time() - self.last_request_time
        if elapsed < self.min_request_interval:
            time.sleep(self.min_request_interval - elapsed)
        self.last_request_time = time.time()
    
    def _request(self, method: str, endpoint: str, params: Dict = None) -> Dict:
        """Make authenticated API request"""
        
        if params is None:
            params = {}
        
        params['timestamp'] = int(time.time() * 1000)
        
        params_str = "&".join([f"{k}={v}" for k, v in params.items()])
        signature = self._get_signature(params_str)
        params['signature'] = signature
        
        url = f"{self.base_url}{endpoint}"
        headers = self._get_headers()
        
        for attempt in range(self.max_retries):
            try:
                self._rate_limit_check()
                
                if method == "GET":
                    response = requests.get(url, params=params, headers=headers, timeout=self.request_timeout)
                elif method == "POST":
                    response = requests.post(url, params=params, headers=headers, timeout=self.request_timeout)
                else:
                    raise ValueError(f"Unsupported method: {method}")
                
                logger.info(f"DEBUG - Status: {response.status_code}")
                logger.info(f"DEBUG - Response: {response.text[:200]}")
                
                if response.status_code == 429:
                    wait_time = int(response.headers.get('Retry-After', 60))
                    logger.warning(f"Rate limited! Waiting {wait_time}s")
                    time.sleep(wait_time)
                    continue
                
                if response.status_code != 200:
                    logger.error(f"API Error {response.status_code}: {response.text}")
                    if attempt < self.max_retries - 1:
                        time.sleep(2 ** attempt)
                        continue
                    return {}
                
                return response.json()
            
            except requests.exceptions.Timeout:
                logger.warning(f"Request timeout (attempt {attempt + 1}/{self.max_retries})")
                if attempt < self.max_retries - 1:
                    time.sleep(2)
                    continue
            
            except Exception as e:
                logger.error(f"Request failed: {e}")
                if attempt < self.max_retries - 1:
                    time.sleep(2)
                    continue
        
        logger.error(f"Failed to complete request after {self.max_retries} retries")
        return {}
    
    def get_account_balance(self) -> float:
        """Get USDT balance"""
        try:
            response = self._request("GET", "/api/v3/account")
        
            logger.info(f"DEBUG - Raw Response: {str(response)[:200]}")
            
            if not response or 'balances' not in response:
                logger.error(f"Invalid balance response: {response}")
                return 0.0
            
            for balance in response.get('balances', []):
                if balance.get('asset') == 'USDT':
                    free_balance = float(balance.get('free', 0))
                    
                    if free_balance < 0 or free_balance > 1_000_000:
                        logger.warning(f"Suspicious balance: ${free_balance}")

            logger.info(f"DEBUG - Raw API Response: {response}")
            
            if not response or 'data' not in response:
                logger.error(f"Invalid balance response format: {response}")
                return 0.0
            
            for account in response.get('data', []):
                if account.get('type') == 'trade' and account.get('currency') == 'USDT':
                    balance = float(account.get('balance', 0))
                    
                    if balance < 0 or balance > 1_000_000:
                        logger.warning(f"Suspicious balance value: ${balance}")

                        return 0.0
                    
                    return free_balance
            

            logger.warning("No USDT balance found")

            logger.warning("No USDT trade account found")

            return 0.0
        
        except Exception as e:
            logger.error(f"Error getting balance: {e}")
            return 0.0
    
    def get_ticker(self, symbol: str) -> Optional[Dict]:
        """Get current ticker price"""
        try:

            response = self._request("GET", "/api/v3/ticker/price", {"symbol": symbol})
            
            if not response or 'price' not in response:
                logger.error(f"Invalid ticker response for {symbol}")
                return None
            
            price = float(response.get('price', 0))
            
            if price <= 0 or price > 1_000_000:
                logger.error(f"Invalid price for {symbol}: ${price}")
                return None
            
            return {'price': price}
        
        except Exception as e:
            logger.error(f"Error getting ticker for {symbol}: {e}")
            return None
    
    def get_klines(self, symbol: str, interval: str = '1h', limit: int = 100) -> list:
        """Get candlestick data"""
        try:
            response = self._request("GET", "/api/v3/klines", {
                "symbol": symbol,
                "interval": interval,
                "limit": limit
            })
            
            if not response or not isinstance(response, list):
                logger.error(f"Invalid klines response for {symbol}")
                return []
            
            return response
        
        except Exception as e:
            logger.error(f"Error getting klines for {symbol}: {e}")
            return []
    
    def place_order(self, symbol: str, side: str, quantity: float) -> Optional[str]:
        """Place a market order"""
        try:
            response = self._request("POST", "/api/v3/order", {
                "symbol": symbol,
                "side": side,
                "type": "MARKET",
                "quantity": f"{quantity:.8f}"
            })
            
            if not response or 'orderId' not in response:
                logger.error(f"Order placement failed: {response}")
                return None
            
            return str(response['orderId'])

            response = self._request("GET", f"/api/v1/market/orderbook/level1", {"symbol": symbol})
            
            if not response or 'data' not in response:
                logger.error(f"Invalid ticker response for {symbol}")
                return None
            
            data = response['data']
            price = float(data.get('price', 0))
            
            if price <= 0 or price > 1_000_000:
                logger.error(f"Invalid price for {symbol}: ${price}")
                return None
            
            return {
                'price': price,
                'timestamp': int(data.get('time', 0))
            }

        
        except Exception as e:
            logger.error(f"Error getting ticker for {symbol}: {e}")
            return None


class SurvivalTradingBot:

    """Survivor-mode trading bot for Binance"""

    """Survivor-mode trading bot"""

    
    def __init__(self):
        """Initialize bot"""
        try:
            creds = CredentialManager.load_credentials()
            
            self.client = BinanceClient(
                creds['api_key'],
                creds['api_secret']
            )
            
            self.telegram_token = creds['telegram_token']
            self.telegram_chat_id = creds['telegram_chat_id']
            
            self.risk_per_trade = 3
            self.take_profit_pct = 8
            self.stop_loss_pct = 5
            self.max_daily_loss = 5
            self.max_open_positions = 2

            self.trading_pairs = ["BTCUSDT", "ETHUSDT"]

            self.trading_pairs = ["BTC-USDT"]

            
            self.daily_loss = 0
            self.open_positions = {}
            self.last_reset = datetime.now().date()
            self.consecutive_errors = 0
            
            logger.info("✅ Bot initialized successfully")
            self.send_alert("🤖 Trading Bot Started on Binance")
        
        except Exception as e:
            logger.error(f"❌ Failed to initialize bot: {e}")
            raise
    
    def send_alert(self, message: str):
        """Send Telegram alert"""
        try:
            url = f"https://api.telegram.org/bot{self.telegram_token}/sendMessage"
            requests.post(url, json={
                'chat_id': self.telegram_chat_id,
                'text': message
            }, timeout=5)
        except Exception as e:
            logger.error(f"Failed to send alert: {e}")
    
    def check_health(self):
        """Check bot health"""
        try:
            balance = self.client.get_account_balance()
            
            if balance == 0.0:
                self.consecutive_errors += 1
                if self.consecutive_errors >= 3:
                    self.send_alert("⚠️ WARNING: Cannot fetch balance!")
            else:
                self.consecutive_errors = 0
            
            return balance
        
        except Exception as e:
            logger.error(f"Health check failed: {e}")
            return 0.0
    
    def run(self):
        """Main bot loop"""
        logger.info("Starting bot loop...")
        
        while True:
            try:
                balance = self.check_health()
                
                if balance > 0:
                    logger.info(f"✅ Balance: ${balance:.2f}")
                else:
                    logger.warning("⚠️ Cannot fetch balance")
                
                time.sleep(60)
            
            except KeyboardInterrupt:
                logger.info("Bot stopped")
                self.send_alert("🛑 Trading Bot Stopped")
                break
            
            except Exception as e:

                logger.error(f"Error: {e}")

                logger.error(f"Error in main loop: {e}")

                time.sleep(10)


if __name__ == "__main__":
    try:
        bot = SurvivalTradingBot()
        bot.run()
    except Exception as e:
        logger.error(f"Fatal error: {e}")
        raise
