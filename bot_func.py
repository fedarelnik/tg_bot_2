import requests
import bot_id
import json
import datetime


TOKEN = misc_2_1.TOKEN
CHANNEL_ID = misc_2_1.CHANNEL_ID

URL = 'https://api.telegram.org/bot'+TOKEN+'/'




def get_updates():
    url = URL + 'getupdates'
    r = requests.get(url)
    return r.json()

def save_updates():
    d = get_updates()
    now = datetime.datetime.now()
    date = str(now)
    with open(date+'.json', 'w') as file:
        json.dump(d, file, indent=2, ensure_ascii=False)
    
def save_update():
    d = get_updates()
    now = datetime.datetime.now()
    date = str(now)
    with open('update.json', 'w', encoding='utf-8') as file:
        json.dump(d, file, indent=2, ensure_ascii=False)

def read_update():
    with open('update.json', 'r', encoding='utf-8') as f:
        d = json.load(f)
        return d

def get_message():
    data = get_updates()
    chat_id = data['result'][-1]['message']['chat']['id']
    try:
        message_text = data['result'][-1]['message']['text']
    except:
        send_message(chat_id, 'Иди на хуй! Только текст!')
        message_text = ''
    message = {'chat_id': chat_id,
               'text': message_text}
    return message
    
def send_message(chat_id, text='Wait a second, please...'):
    url = URL + 'sendmessage?chat_id={}&text={}'.format(chat_id, text)
    requests.get(url)

def resend_message():
    d = get_message()
    text = d['text']
    if(text != ''):
        send_message(CHANNEL_ID, text)
    return d