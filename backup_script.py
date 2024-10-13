{\rtf1\ansi\ansicpg1252\deff0\nouicompat\deflang1033{\fonttbl{\f0\fnil\fcharset0 Calibri;}}
{\*\generator Riched20 10.0.22621}\viewkind4\uc1 
\pard\ri-1710\sa200\sl240\slmult1\f0\fs36\lang19 ## backup_script.py\par
\fs22\par
import subprocess\par
from datetime import datetime\par
from telegram_bot import send_message\par
\par
#settings\par
source = '/share/'\par
destination = '/share_backup/'\par
log_file = '/home/demich/backup/share_backup.log'\par
summary_file = '/tmp/rsync-summary'\par
\par
#rsync command\par
rsync_command = ['rsync', '-a', '--stats', 'human-readable', source, destination]\par
process = subprocess.run(rsync_command, capture_output=True, text=True)\par
\par
#summary_content preparation\par
summary_content = process.stdout + process.stderr\par
\par
#log summary\par
with open(log_file, 'a') as log:\par
\tab log.write(f"Backup on: \{datetime.now()\}\\n")\par
\tab log.write(summary_content)\par
\par
#Error check and send message with telegram bot\par
if process.returncode is not 0:\par
\tab send_message(f"FAILED auto-backup NAS '/share/' -->'/share_backup/':\tab\\n\{process.returncode\}\\n\{summary_content\}")\par
else \par
\tab send_message(f"SUCCESFULL auto-backup  '/share/' --> '/share_backup/' :\tab\\n\{summary_content\}")\par
\par
\par
\par
}
 