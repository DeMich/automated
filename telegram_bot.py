{\rtf1\ansi\ansicpg1252\deff0\nouicompat\deflang1033{\fonttbl{\f0\fnil\fcharset0 Calibri;}}
{\colortbl ;\red0\green0\blue255;}
{\*\generator Riched20 10.0.22621}\viewkind4\uc1 
\pard\sa200\sl240\slmult1\f0\fs36\lang19 ## Telegram_bot.py\par
\fs22 import os\par
import requests\par
\par
# Telegram settings\par
bot_token = os.environ.get\{'bot_token'\}\par
chat_id = os.environ.get\{'chat_id'\}\par
#bot_token&chat_id has been stored on linux mint as sensitive data by using the environment variables\par
\par
def send_message(msg):\par
\tab url = f'{{\field{\*\fldinst{HYPERLINK https://api.telegram.org/bot\{bot_token\}/sendMessage }}{\fldrslt{https://api.telegram.org/bot\{bot_token\}/sendMessage\ul0\cf0}}}}\f0\fs22 "\par
\tab params = \{'chat_id': chat_id, 'text': msg\}\par
\tab request.get\{url, params=params\}\par
\tab return response.json()\par
\tab #return for when message sending errors...\par
\par
\par
\par
}
 