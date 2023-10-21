import requests
import time

API_URL = 'https://api.telegram.org/bot'
BOT_TOKEN = '6407812037:AAHIjdQDfRW4JwyldWtwTN9ApORUEKG4XHk'
TEXT = 'Классный апдейт!'
MAX_COUNTER = 10

offset = -2
counter = 0
chat_id: int

while counter < MAX_COUNTER:

    print('attempt =', counter)
    
    updates = requests.get(f'{API_URL}{BOT_TOKEN}/getUpdates?offset={offset + 1}').json()

    if updates['result']:
        for result in updates['result']:
            offset = result['update_id']
            chat_id = result['message']['from']['id']
            requests.get(f'{API_URL}{BOT_TOKEN}/sendMassage?chat_id={chat_id}&text={TEXT}').json
            
    time.sleep(1)
    counter += 1
#https://api.telegram.org/bot6407812037:AAHIjdQDfRW4JwyldWtwTN9ApORUEKG4XHk/getUpdates
#https://api.telegram.org/bot6407812037:AAHIjdQDfRW4JwyldWtwTN9ApORUEKG4XHk/getMe
#https://api.telegram.org/bot6407812037:AAHIjdQDfRW4JwyldWtwTN9ApORUEKG4XHk/sendMessage?chat_id=5408324739&text=Привет, Mikhail!