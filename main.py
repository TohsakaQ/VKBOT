from vk_api.longpoll import VkLongPoll, VkEventType
import vk_api
from datetime import datetime
import random
import time
import get_pictures
import get_pictures2
import get_hentai
import get_itpedia
import get_fateprikol
import get_fateart
import get_3d
import get_kuk

vk_session = vk_api.VkApi(token="СВОЙ ТОКЕН")
session_api = vk_session.get_api()
longpoll = VkLongPoll(vk_session)

def send_message(vk_session, id_type, id, message=None, attachment=None, keyboard=None):
    vk_session.method('messages.send',{id_type: id, 'message': message, 'random_id': random.randint(-2147483648, +2147483648), "attachment": attachment, 'keyboard': keyboard})

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:
        print('Время: ' + str(datetime.strftime(datetime.now(), "%H:%M:%S")))
        print('Текст ПИДОРАСА: ' + str(event.text))
        print(event.user_id)
        response = event.text.lower()


        if event.text.lower() == "!камни":
            if event.from_chat:
                send_message(vk_session, 'chat_id', event.chat_id, '🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿')

        if event.text.lower() == "!лоли":
            if event.from_chat:
                attachment = get_pictures.get(vk_session, -127518015, session_api)
                vk_session.method('messages.send', {'chat_id': event.chat_id, 'message': 'Держи девочку!', 'random_id': 0, "attachment": attachment})

        if event.text.lower() == "!юри":
            if event.from_chat:
                attachment = get_pictures2.get(vk_session, -153284406, session_api)
                vk_session.method('messages.send', {'chat_id': event.chat_id, 'message': 'держи лесбух!', 'random_id': 0, "attachment": attachment})

        if event.text.lower() == "!хентай":
            if event.from_chat:
                attachment = get_hentai.get(vk_session, -188755008, session_api)
                vk_session.method('messages.send', {'chat_id': event.chat_id, 'message': 'держи хентай, конченый извращенец!', 'random_id': 0, "attachment": attachment})

        if event.text.lower() == "!палата шевцова":
            if event.from_chat:
                attachment = get_itpedia.get(vk_session, -88245281, session_api)
                vk_session.method('messages.send', {'chat_id': event.chat_id, 'message': 'держи мем из палаты Шевцова!', 'random_id': 0, "attachment": attachment})


        if event.text.lower() == "!фейт прикол":
            if event.from_chat:
                attachment = get_fateprikol.get(vk_session, -183563128, session_api)
                vk_session.method('messages.send', {'chat_id': event.chat_id, 'message': 'держи мем из группы Fate/GrandПрикол!', 'random_id': 0, "attachment": attachment})

        if event.text.lower() == "!фейт арт":
            if event.from_chat:
                attachment = get_fateart.get(vk_session, -191752227, session_api)
                vk_session.method('messages.send', {'chat_id': event.chat_id, 'message': 'держи арт из группы far side of the moon!', 'random_id': 0, "attachment": attachment})

        if event.text.lower() == "!3д мусор":
            if event.from_chat:
                attachment = get_3d.get(vk_session, -70232735, session_api)
                vk_session.method('messages.send', {'chat_id': event.chat_id, 'message': 'держи свой 3д мусор!', 'random_id': 0, "attachment": attachment})

        if event.text.lower() == "!кукла":
            if event.from_chat:
                attachment = get_kuk.get(vk_session, -186765691, session_api)
                vk_session.method('messages.send', {'chat_id': event.chat_id, 'message': 'держи свою куклу, куклоёб!', 'random_id': 0, "attachment": attachment})

        if event.text.lower() == "!хуесосина":
            if event.from_chat:
                send_message(vk_session, 'chat_id', event.chat_id, attachment='video210923765_456239280')

        if event.text.lower() == "!колда":
            if event.from_chat:
                send_message(vk_session, 'chat_id', event.chat_id, attachment='video537612639_456239020')



