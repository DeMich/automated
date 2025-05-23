### Telegram_bot.py
import os
import requests
import json
from dotenv import load_dotenv
load_dotenv(os.path.expanduser('~/automated_backup_task/.env_backup_telegram_variables'))

## Telegram settings

bot_token = os.environ.get("BOT_TOKEN")
chat_id = os.environ.get("CHAT_ID")
print("bot_token:", bot_token)
print("chat_id:", chat_id)


def send_message(msg):
    url = f'https://api.telegram.org/bot{bot_token}/sendMessage'
    params = {'chat_id': chat_id, 'text': msg}

    # Make the GET request and capture the response
    response = requests.post(url, params=params)
    
    # Check if the request was successful
    if response.status_code != 200:
        return f"Failed to send message, API response code: {response.text}"
    else:
        return f"Succesful sending message, API response code: {response.text}" 
