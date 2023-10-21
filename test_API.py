import requests
import time

API_URL = 'https://api.telegram.org/bot'
API_CATS_URL = 'https://api.thecatapi.com/v1/images/search'
BOT_TOKEN = '6407812037:AAHIjdQDfRW4JwyldWtwTN9ApORUEKG4XHk'
ERROR_TEXT = 'Классный апдейт!'
MAX_COUNTER = 10

offset = -2
counter = 0
chat_id: int
cat_respone: requests.Response
cat_link: str

while counter < MAX_COUNTER:
    
    print('attempt =', counter)

    updates = requests.get(f'{API_URL}{BOT_TOKEN}/getUpdates?offset={offset + 1}').json()

    if updates['result']:
        for result in updates['result']:
            offset = result['update_id']
            chat_id = result['message']['from']['id']
            cat_respone = requests.get(API_CATS_URL)
            if cat_respone.status_code == 200:
                cat_link = cat_respone.json()[0]['url']
                requests.get(f'{API_URL}{BOT_TOKEN}/sendPhoto?chat_id={chat_id}&photo={cat_link}')
            else:
                requests.get(f'{API_URL}{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text={ERROR_TEXT}')
            #requests.get(f'{API_URL}{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text={TEXT}')
            
    time.sleep(1)
    counter += 1
#https://api.telegram.org/bot6407812037:AAHIjdQDfRW4JwyldWtwTN9ApORUEKG4XHk/getUpdates
#https://api.telegram.org/bot6407812037:AAHIjdQDfRW4JwyldWtwTN9ApORUEKG4XHk/getMe
#https://api.telegram.org/bot6407812037:AAHIjdQDfRW4JwyldWtwTN9ApORUEKG4XHk/sendMessage?chat_id=5408324739&text=amazing
#https://api.telegram.org/bot<token>/sendMessage?chat_id=<chat_id>&text=amazing