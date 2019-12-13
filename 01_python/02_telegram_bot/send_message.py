import requests
from decouple import config

base = 'https://api.telegram.org'
token = config('TELEGRAM_BOT_TOKEN')
chat_id = config'CHAT_ID'
text = 'Friday'

url = f'{base}/bot{token}/sendMessage?chat_id={chat_id}&text={text}'

send_message = requests.get(url)

print(send_message)
