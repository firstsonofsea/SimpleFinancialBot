# A very simple Flask Hello World app for you to get started with...

from flask import Flask, request, json
import vk
import os.path
import files
import comands
app = Flask(__name__)

TOKEN = ''
CONFIRM_TOKEN = ''
DATA = {}

@app.route('/', methods=['POST'])
def processing():
    global DATA
    data = json.loads(request.data)
    if 'type' not in data.keys():
        return 'not vk'
    if data['type'] == 'confirmation':
        return CONFIRM_TOKEN
    elif data['type'] == 'message_new':
        session = vk.Session()
        api = vk.API(session, v=5.5)
        user_id = data['object']['user_id']
        namef = str(user_id) + ".txt"
        if os.path.exists(namef):
            DATA = files.readf(namef)
        else:
            files.createf(name):
        mes = "ЧОТА ТУТ НЕ ТО"
        if 'добавь' in data['object']['body'].lower():
            s = data['object']['body'].split(' ')
            comands.com1(s[1], s[2], DATA)
            mes = "Cделано!"
        elif data['object']['body'] == '2':
            mes ="Вот ваш список трат:\n" + comands.com2(DATA)
        elif data['object']['body'] == '3':
            comands.clean(DATA)
            mes = "Я всё удалил!"
        files.updatef(namef, DATA):
        api.messages.send(access_token=TOKEN, user_id=str(user_id), message=mes)
        return 'ok'
    
