## -*- coding: utf-8 -*-
import vk_api, json, random, time, requests, wikipedia, os
from vk_api import VkUpload
from vkbottle import *
from googletrans import Translator
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from bs4 import BeautifulSoup
from config import main_token
from comands import *
from music import *
from photo import *

#Основная авторизация сообщества
vk_session = vk_api.VkApi(token = main_token)
longpoll = VkBotLongPoll(vk_session, 201980948)
vk = vk_session.get_api()

#Авторизация через user аккаунт
token_m = "9e74e24057621d5387bc313f9929e42b12be947e58b9edbbbb770fc7d782aae1f818fa23d62019c75c696"
vk_sessionss = vk_api.VkApi(token=token_m)
vks = vk_sessionss.get_api()


token = "c482f406afae454c3aa8384e0c39f598e8e317c4011819ae492e663af85a0a2345db0bde5b4341c204cef"
vk_session_u = vk_api.VkApi(login = '+79005131326', password="Dima8950", token=token)
vk_u = vk_session_u.get_api()

#-------------------ФУНКЦИИ--------------------#

#Главный метод отправки сообщений
def sender(id, text):
	vk_session.method('messages.send', {'peer_id' : id, 'message' : text, 'random_id' : 0})

#Метод отправки личных сообщений
def sender_me(id, text):
	vk_session.method('messages.send', {'user_id' : id, 'message' : text, 'random_id' : 0})

#Метод отправки клавиатуры
def send_key(id, text, keyboard):
	vk_session.method('messages.send', {'peer_id' : id, 'message' : text, 'random_id' : 0, 'keyboard': keyboard})

#Метод отправки сообщения и медиа файла
def send(id, text, media):
	vk_session.method('messages.send', {'peer_id' : id, 'message' : text, "attachment": media, 'random_id' : 0})

#Нарушение триггера
def strigger(id, trigger_number):
	sender(id, 'Это действие ограничено триггером ' + trigger_number)

#Метод отправки BTS картинок
def sendBTS():
	photoBTS1 = ['photo-201980948_457239087', 'photo-201980948_457239088', 'photo-201980948_457239089', 'photo-201980948_457239090', 'photo-201980948_457239091', 'photo-201980948_457239092']
	photoBTS2 = ['photo-201980948_457239075', 'photo-201980948_457239076', 'photo-201980948_457239077', 'photo-201980948_457239078', 'photo-201980948_457239079', 'photo-201980948_457239080']
	photoBTS3 = ['photo-201980948_457239081', 'photo-201980948_457239082', 'photo-201980948_457239083', 'photo-201980948_457239084', 'photo-201980948_457239085', 'photo-201980948_457239086']
	send(id, f'Тут есть арми 💜ᗷTS⟭⟬💜', random.choice(photoBTS1) + ',' + random.choice(photoBTS2) +  ',' + random.choice(photoBTS3))

#Метод обработки ссылок и @ в id
def get_user(pattern: str) -> int:
    if "[id" in pattern:
        return int(pattern.split("|")[0].replace("[id", ""))
    if "vk.com/" in pattern:
        domen = pattern.split("/")[-1]
        print(domen)
        return vk.utils.resolveScreenName(screen_name=domen)["object_id"]

r_sex = []

#Настройки CallBack клавиатуры
settings = dict(one_time=False, inline=True)

#Типы CallBack кнопок
CALLBACK_TYPES = ('show_snackbar', 'open_link', 'open_app')

#input("Жмяк enter чтобы запустить бота")

print('Бот запущен')

#Подключение википедии
wikipedia.set_lang("RU")

#Параметр offset для поиска видео
offset = 0

#-------------------ЦИКЛ--------------------#
for event in longpoll.listen():
	if event.type == VkBotEventType.MESSAGE_EVENT:			#Обработка нажатия на CallBack кнопку
		id = event.obj.peer_id
		user = event.obj.user_id
		a_time = event.obj.timestamp

		if event.object.payload.get('type') == 'cmmunic':
			sender_me(user, "Опишите вашу проблему ему - vk.com/maaaasyyyniiik")

		if event.object.payload.get('type') == 'report_appeal':
			sender(2000000001, "Пользователь " + report_u_n_f + " был обжалован")

		if event.object.payload.get('type') == 'report_warn':
			if str(user) in admin_from:
				warn_m_u = vk.users.get(user_ids=user)
				warn_m_u_m_n_1 = warn_m_u[0]["first_name"]
				warn_m_u_m_n_2 = warn_m_u[0]["last_name"]
				warn_m_u_m_n_f = warn_m_u_m_n_1 + ' ' + warn_m_u_m_n_2
				warn_user_m = '[id' + str(user) + '|' + warn_m_u_m_n_f + ']'

				sp_msg_w_p = msgl.split(" ",2)
				drtg1 = int(sp_msg_w_p[1].split("|")[0].replace("[id", ""))

				warn1_m_u = vk.users.get(user_ids=drtg1)
				warn1_m_u_m_n_1 = warn1_m_u[0]["first_name"]
				warn1_m_u_m_n_2 = warn1_m_u[0]["last_name"]
				warn1_m_u_m_n_f = warn1_m_u_m_n_1 + ' ' + warn_m_u_m_n_2
				warn1_user_m = '[id' + str(drtg1) + '|' + warn1_m_u_m_n_f + ']'

				with open('users.json', encoding='utf-8') as f:
					data = json.load(f)
				rtryh6 = int(data[str(drtg1)]["warn"]) + 1
				if str(rtryh6) == '3':
					sender(2000000001, warn1_user_m + ' получил(а) максимальное колличество предупреждений 3/3')
					vk.messages.removeChatUser(chat_id='1', user_id=str(drtg1))
				else:
					with open('users.json', encoding='utf-8') as f:
						data = json.load(f)

					warn_w_p = int(data[str(drtg1)]["warn"]) + 1

					data[str(drtg1)]["warn"] = int(warn_w_p)

					with open('users.json', 'w', encoding='utf-8') as f:
						json.dump(data, f, ensure_ascii=False, indent=4)

					try:
						sender(2000000001, f'Готово!<br>Всего предупреждений: ' + str(rtryh6) + '/3<br>Модератор: ' + warn_user_m + '<br>Причина: Решение по репорту')
					except:
						sender(2000000001, f'Готово!<br>Всего предупреждений: ' + str(rtryh6) + '/3<br>Модератор: ' + warn_user_m)

			else:
				sender(id, f'Вам отказано в доступе')

		if event.object.payload.get('type') == 'my_dick':
			vk.messages.sendMessageEventAnswer(event_id=event.object.event_id, user_id=event.object.user_id, peer_id=event.object.peer_id, event_data=json.dumps({"type": "show_snackbar", "text": "нахуй"}))

		if event.object.payload.get('type') == 'sex_a':
			try:
				if str(user) in r_sex[1]:
					p_sex_n_u = vk.users.get(user_ids=r_sex[0])
					p_sex_n_1 = p_sex_n_u[0]["first_name"]
					p_sex_n_2 = p_sex_n_u[0]["last_name"]
					p_sex_n_f_l = p_sex_n_1 + ' ' + p_sex_n_2
					p_sex_n_f = '[id' + str(r_sex[0]) + '|' + p_sex_n_f_l + ']'
					p_sex_sex1 = vk_session.method('users.get', {'user_ids' : str(r_sex[0]), 'fields' : 'sex', 'name_case' : 'nom'})
					p_sex_sex0 = p_sex_sex1[0]
					p_sex_sex = json.dumps(p_sex_sex0['sex'])
					if int(p_sex_sex) == 1:
						p_sex_sex_s = 'принудила к интиму '
					if int(p_sex_sex) == 2:
						p_sex_sex_s = 'принудил к интиму '
					p_sex_w_u_n = vk.users.get(user_ids=r_sex[1], name_case='acc')
					p_sex_w_1 = p_sex_w_u_n[0]["first_name"]
					p_sex_w_2 = p_sex_w_u_n[0]["last_name"]
					p_sex_w_n_f_l = p_sex_w_1 + ' ' + p_sex_w_2
					p_sex_w_n_f = '[id' + str(r_sex[1]) + '|' + p_sex_w_n_f_l + ']'

					p_sex_w_u_n1 = vk.users.get(user_ids=r_sex[1], name_case='nom')
					p_sex_w_11 = p_sex_w_u_n1[0]["first_name"]
					p_sex_w_21 = p_sex_w_u_n1[0]["last_name"]
					p_sex_w_n_f_l1 = p_sex_w_11 + ' ' + p_sex_w_21
					p_sex_w_n_f1 = '[id' + str(r_sex[1]) + '|' + p_sex_w_n_f_l1 + ']'

					r_sex_9875 = random.choice(r_sex)

					kid_rod = r_sex

					r_sex = []

					sex_kid_l = [1, 0, 0, 0, 0]

					sex_kid = random.choice(sex_kid_l)

					if sex_kid == 1:
						sender(id, p_sex_n_f + ' ' + p_sex_sex_s + p_sex_w_n_f)
						if int(p_sex_sex) == 1:
							p_sex_sex_kid = ' забеременила '
						if int(p_sex_sex) == 2:
							p_sex_sex_kid = ' забеременил '

						kid_sex_l = [1, 2]
						kid_sex = random.choice(kid_sex_l)
						if kid_sex == 1:
							kid_sex_s = 'девочка'
						if kid_sex == 2:
							kid_sex_s = 'мальчик'

						sex_kid_name_g = VkKeyboard(**settings)
						sex_kid_name_g.add_callback_button(label='Дать имя ребёнку', color=VkKeyboardColor.POSITIVE, payload={"type": "kid_reg_a"})

						sex_kid_name_r = vk.users.get(user_ids=r_sex_9875, name_case='dat')
						kid_name_r_1 = sex_kid_name_r[0]["first_name"]
						kid_name_r_2 = sex_kid_name_r[0]["last_name"]
						kid_name_r_f_l = kid_name_r_1 + ' ' + kid_name_r_2
						kid_name_r_f = '[id' + str(r_sex_9875) + '|' + kid_name_r_f_l + ']'

						msg_kid_sex = 'Оуууу, похоже ' + p_sex_w_n_f1 + p_sex_sex_kid + '<br>У вас ' + kid_sex_s + '!<br>Право выбрать имя педоставляется ' + kid_name_r_f
						vk_session.method("messages.send", {"peer_id": id, "message": msg_kid_sex, "random_id": 0, "keyboard": sex_kid_name_g.get_keyboard()})

						with open('users.json', encoding='utf-8') as f:
							data = json.load(f)

						data[str(r_sex_9875)]["me_msg"] = 1

						with open('users.json', 'w', encoding='utf-8') as f:
							json.dump(data, f, ensure_ascii=False, indent=4)


					if sex_kid == 0:
						sender(id, p_sex_n_f + ' ' + p_sex_sex_s + p_sex_w_n_f)

				else:
					vk.messages.sendMessageEventAnswer(event_id=event.object.event_id, user_id=event.object.user_id, peer_id=event.object.peer_id, event_data=json.dumps({"type": "show_snackbar", "text": "Ей, это не тебе"}))

			except Exception as e:
				sender(2000000001, str(e))
				print(e)

		if event.object.payload.get('type') == 'marry_q':
			with open('marry.json', encoding='utf-8') as f:
				data = json.load(f)
			marry = data["marry"]
			if str(user) in marry[1]:
				marry_u_1 = vk.users.get(user_ids=marry[0], name_case='nom')
				marry_n_1_1 = marry_u_1[0]["first_name"]
				marry_n_2_1 = marry_u_1[0]["last_name"]
				marry_n_f_1 = marry_n_1_1 + ' ' + marry_n_2_1
				marry_n_f_n_1 = '[id' + str(marry[0]) + '|' + marry_n_f_1 + ']'

				marry_u_2 = vk.users.get(user_ids=marry[1], name_case='nom')
				marry_n_1_2 = marry_u_2[0]["first_name"]
				marry_n_2_2 = marry_u_2[0]["last_name"]
				marry_n_f_2 = marry_n_1_2 + ' ' + marry_n_2_2
				marry_n_f_n_2 = '[id' + str(marry[1]) + '|' + marry_n_f_2 + ']'

				with open('marry.json', encoding='utf-8') as f:
					data = json.load(f)

				a_dict = ({str(marry[0]): {"partner": marry[1], "i_am_id": marry_n_f_n_1, "partner_id": marry_n_f_n_2, "time": a_time}})
				b_dict = ({str(marry[1]): {"partner": marry[0], "i_am_id": marry_n_f_n_2, "partner_id": marry_n_f_n_1, "time": a_time}})

				data.update(a_dict)
				data.update(b_dict)

				with open('marry.json', 'w', encoding='utf-8') as f:
					json.dump(data, f, ensure_ascii=False, indent=4)

				sender(id, '💍 В беселе зарегистрирован новый брак<br>👰👨‍⚖ С сегодняшнего дня ' + marry_n_f_n_1 + ' и ' + marry_n_f_n_2 + ' состоят в браке')
			else:
				vk.messages.sendMessageEventAnswer(event_id=event.object.event_id, user_id=event.object.user_id, peer_id=event.object.peer_id, event_data=json.dumps({"type": "show_snackbar", "text": "Ей, это не тебе"}))

		if event.object.payload.get('type') == "kid_reg_a":
			try:
				with open('users.json', encoding='utf-8') as f:
					data = json.load(f)

				if data[str(user)]["me_msg"] == 0:
					vk.messages.sendMessageEventAnswer(event_id=event.object.event_id, user_id=event.object.user_id, peer_id=event.object.peer_id, event_data=json.dumps({"type": "show_snackbar", "text": "У вас нет ожидающих запросов к серверу"}))

				if data[str(user)]["me_msg"] == 1:
					sender_me(user, "Введите айди ребенка<br>(kid @durov или kid vk.com/durov)")			

			except Exception as e:
				if str(e) == "[901] Can't send messages for users without permission":
					sender(id, 'Разрешите сообществу отправлять вам сообщения<br>satira-group.tk')

		if event.object.payload.get('type') == "kid_reg_me":
			try:
				with open('users.json', encoding='utf-8') as f:
					data = json.load(f)

				if data[str(id)]["me_msg"] == 0:
					vk.messages.sendMessageEventAnswer(event_id=event.object.event_id, user_id=event.object.user_id, peer_id=event.object.peer_id, event_data=json.dumps({"type": "show_snackbar", "text": "У вас нет ожидающих запросов к серверу"}))

				if data[str(id)]["me_msg"] == 1:
					sender_me(id, "Введите айди ребенка<br>(kid @durov или kid vk.com/durov)")			

			except Exception as e:
				if str(e) == "[901] Can't send messages for users without permission":
					sender(id, 'Разрешите сообществу отправлять вам сообщения<br>satira-group.tk')

		if event.object.payload.get('type') == "koronavirus_menu":
			url = 'https://koronavirus-today.ru/covid-19'
			response = requests.get(url)
			soup = BeautifulSoup(response.text, 'lxml')
			quotes = soup.find_all('div', class_='stat_container')
			infected = quotes[0].find_all('p')
			infected_p = quotes[0].find('p', class_="plus_confirmed")
			dead = quotes[0].find_all('p')
			dead_p = quotes[0].find('p', class_="plus_death")
			recovered = quotes[0].find_all('p')
			recovered_p = quotes[0].find('p', class_="plus_recovered")
			kowid_send = "Статистика коронавируса в мире<br>Заражённых:<br>" + infected[0].text + " " + infected_p.text + "<br>Погибших:<br>" + dead[2].text + " " + dead_p.text + "<br>Выздоровели:<br>" + recovered[4].text + " " + recovered_p.text

			koronavirus1 = VkKeyboard(**settings)
			koronavirus1.add_callback_button(label='Россия', color=VkKeyboardColor.PRIMARY, payload={"type": "koronavirus_menu_r"})

			vk.messages.edit(peer_id=event.obj.peer_id, message=kowid_send, conversation_message_id=event.obj.conversation_message_id, keyboard=koronavirus1.get_keyboard())

		if event.object.payload.get('type') == "koronavirus_menu_r":
			url = 'https://koronavirus-today.ru/covid-19'
			response = requests.get(url)
			soup = BeautifulSoup(response.text, 'lxml')
			quotes = soup.find_all('div', class_='stat_container')
			infected = quotes[1].find_all('p')
			infected_p = quotes[1].find('p', class_="plus_confirmed")
			dead = quotes[1].find_all('p')
			dead_p = quotes[1].find('p', class_="plus_death")
			recovered = quotes[1].find_all('p')
			recovered_p = quotes[1].find('p', class_="plus_recovered")
			kowid_send = "Статистика коронавируса в России<br>Заражённых:<br>" + infected[0].text + " " + infected_p.text + "<br>Погибших:<br>" + dead[2].text + " " + dead_p.text + "<br>Выздоровели:<br>" + recovered[4].text + " " + recovered_p.text

			koronavirus1 = VkKeyboard(**settings)
			koronavirus1.add_callback_button(label='Мир', color=VkKeyboardColor.PRIMARY, payload={"type": "koronavirus_menu"})

			vk.messages.edit(peer_id=event.obj.peer_id, message=kowid_send, conversation_message_id=event.obj.conversation_message_id, keyboard=koronavirus1.get_keyboard())

	if event.type == VkBotEventType.MESSAGE_NEW:				#Обработка команд
		if event.from_user:		#Если написали в ЛС
			id = event.obj.from_id
			msg = event.obj.text.lower()
			msgl = event.obj.text
			attachment = event.obj.attachments
			a_time = event.obj.timestamp
			reply = event.object.reply_message
			te2xt = msg.split(' ')
			chat_id1 = event.chat_id
			
			if msg in ["начать", "привет", "ей", "бот"]:
				start_k = VkKeyboard(**settings)
				start_k.add_callback_button(label='Связаться с создателем', color=VkKeyboardColor.POSITIVE, payload={"type": "cmmunic"})
				start_k.add_line()
				start_k.add_callback_button(label='Регистрация ребёнка', color=VkKeyboardColor.POSITIVE, payload={"type": "kid_reg_me"})
				send_key(id, 'Приветствую тебя', start_k.get_keyboard())

			if "kid" in event.obj.text.lower():
				kid_reg_n_l = te2xt[1]
				kid_reg_n = get_user(kid_reg_n_l)

				with open('users.json', encoding='utf-8') as f:
					data = json.load(f)

				if data[str(id)]["me_msg"] == 1:
					kid_reg_u_n = vk.users.get(user_ids=kid_reg_n, name_case='nom')
					kid_reg_n_1 = kid_reg_u_n[0]["first_name"]
					kid_reg_n_2 = kid_reg_u_n[0]["last_name"]
					kid_reg_n_l = kid_reg_n_1 + ' ' + kid_reg_n_2
					kid_reg_n_f = '[id' + str(kid_reg_n) + '|' + kid_reg_n_l + ']'
					sender_me(id, 'Вашего ребёнка зовут ' + kid_reg_n_f)
					sender(2000000001, 'Вашего ребёнка зовут ' + kid_reg_n_f)
					with open('users.json', encoding='utf-8') as f:
						data = json.load(f)

					data[str(id)]["me_msg"] = 0
					data[str(id)]["kid"] += " " + kid_reg_n_f 
					data[str(r_sex_9875)]["kid"] += " " + kid_reg_n_f

					with open('users.json', 'w', encoding='utf-8') as f:
						json.dump(data, f, ensure_ascii=False, indent=4)

				else:
					sender_me(id, "У вас нет ожидающих запросов к серверу")

					'''kid_reg_f_o = open('profiles\\kid\\' + str(kid_rod[0]) + '.txt','r')
					kid_reg_op1 = kid_reg_f_o.read()
					kid_reg_f_o.close()

					kid_reg_f_o = open('profiles\\kid\\' + str(kid_rod[1]) + '.txt','r')
					kid_reg_op2 = kid_reg_f_o.read()
					kid_reg_f_o.close()

					kid_reg_w_o = open('profiles\\kid\\' + str(kid_rod[0]) + '.txt', 'w')
					kid_reg_w_o.write(kid_reg_op1 + ' ' + kid_reg_n_f)
					kid_reg_w_o.close()

					kid_reg_w_o = open('profiles\\kid\\' + str(kid_rod[1]) + '.txt', 'w')
					kid_reg_w_o.write(kid_reg_op2 + ' ' + kid_reg_n_f)
					kid_reg_w_o.close()'''

			'''with open('users.json', encoding='utf-8') as f:
				data = json.load(f)

			if data[str(user)]["me_msg"] == 0:
				sender_me(id, "У вас нет ожидаюющих запросов к серверу")

			if data[str(user)]["me_msg"] == 1:
				sender_me(id, "Введите айди ребенка (kid @durov или kid vk.com\\durov)")

			if msg 
				

			with open('users.json', 'w', encoding='utf-8') as f:
				json.dump(data, f, ensure_ascii=False, indent=4)'''
			
		if event.from_chat:		#Если написали в чат
			try:
				user = event.obj.from_id
				msg = event.obj.text.lower()
				msgl = event.obj.text
				id = event.obj.peer_id
				attachment = event.obj.attachments
				a_time = event.obj.timestamp
				reply = event.object.reply_message
				te2xt = msg.split(' ')
				chat_id1 = event.chat_id
				
				#Приветствие

				 

				try:
					invite_type = event.obj.action["type"]
					invite_id = event.obj.action["member_id"]
					if event.obj.action["type"] == "chat_invite_user":
						join_n_u = vk.users.get(user_ids=invite_id)
						join_n_1 = join_n_u[0]["first_name"]
						join_n_2 = join_n_u[0]["last_name"]
						join_n_f = join_n_1 + ' ' + join_n_2
						join_n_f_id = "[id" + str(invite_id) + "|" + join_n_f + "]"
						join_id_text = 'Привет, ' + join_n_f_id + '!<br>Я - Сатира, <br>Приветствую, тебя, в нашей беседе.<br>Меня призвали из древних сказок, и теперь я служу вам, слежу за порядком и помогаю приятно провести время.<br>С моими командами ты можешь ознакомиться написав: Cатира команды.'
						sender(id, join_id_text)
						vk.messages.removeChatUser(chat_id=chat_id1, user_id=str(event.obj.action["member_id"]))

				except:
					a = 1

				try:		
					if event.obj.action["type"] == "chat_title_update":
						if str(user) in admin_from:
							a = 1

						else:
							vk.messages.editChat(chat_id=chat_id1, title="СатираProject")
							sender(id, "Вам нельзя изменять название беседы")
				except:
					a = 1

				try:
					if event.obj.action["type"] == "chat_kick_user":
						vk.messages.removeChatUser(chat_id=chat_id1, user_id=str(event.obj.action["member_id"]))
				except:
					a = 1

				if "-" in str(user):		#Защита от команд бота
					erf = 0

				else:
					try:		#Создание профиля если он не создан
						with open('users.json', encoding='utf-8') as f:
							dicks = json.load(f)
						dwt34 = dicks[str(user)]

					except:
						user_n_r = vk.users.get(user_ids=user)
						user_n_r_1 = user_n_r[0]["first_name"]
						user_n_r_2 = user_n_r[0]["last_name"]

						a_dict = ({user: {"first_name": str(user_n_r_1), "last_name": user_n_r_2, "full_name": user_n_r_1 + ' ' + user_n_r_2, "id_name": "[id" + str(user) + "|" + user_n_r_1 + " " + user_n_r_2 + "]", "money": 0, "role": "Участник", "warn": 0, "nick": "none", "kid": "none", "me_msg": 0},})

						with open('users.json', encoding='utf-8') as f:
							data = json.load(f)

						data.update(a_dict)

						with open('users.json', 'w', encoding='utf-8') as f:
							json.dump(data, f, ensure_ascii=False, indent=4)
						
						sender(id, f'Ваш профиль создан')

					with open('settings.json', encoding='utf-8') as f:
						data = json.load(f)
					admin_from = data["admins"]

					kpad598 = open('message.txt','r')
					klad597 = kpad598.read()
					kpad598.close()
					rwr4 = int(klad597) + 1
					kpad98 = open('message.txt','w')
					klad97 = kpad98.write(str(rwr4)) 
					kpad98.close()

					#vk.messages.sendMessageEventAnswer(event_id=event.object.event_id, user_id=event.object.user_id, peer_id=event.object.peer_id, event_data=json.dumps({"type": "show_snackbar", "text": "Трахни меня в член"}))

					if msg in ['сатира сколько всего сообщений', 'сатира сколько сообщений всего', 'сатира сколько сообщений']:
						kpad5t8 = open('message.txt','r')
						klad5t7 = kpad5t8.read()
						kpad5t8.close()
						sender(id, f'Всего сообщений: ' + klad5t7)

					if msg in ['сатира правила']:
						sender(id, RULES)

					if msg in ['сатира поставить диму раком', 'сатира поставить раком диму']:
						if user == 504945503:
							kd3 = ['Ну Заря блин<br>', ' ']
							send(id, random.choice(kd3) + 'Ты поставила [id400484262|меня] раком,<br>Так уж и быть😔', 'photo-201980948_457239144')
						else:
							sender(id, 'Не тронь! [id400484262|Я] Хюрем')

					if "сатира обнять" in event.obj.text.lower():
						if (len(te2xt) == 2):
							hug_w_n = reply["from_id"]
						if (len(te2xt) == 3):
							hug1 = msg.replace('сатира обнять ', '')
							hug_w_n = hug1.split("|")[0].replace("[id", "")

						###Идентификатор альбома ----- 277598460
						album_hug = vk_u.photos.get(owner_id=-201980948, album_id=277598460)
						hug_p1 = random.choice(album_hug["items"])
						hug_p = 'photo' + str(hug_p1["owner_id"]) + "_" + str(hug_p1["id"])

						hug_n_u = vk.users.get(user_ids=user)
						hug_n_1 = hug_n_u[0]["first_name"]
						hug_n_2 = hug_n_u[0]["last_name"]
						hug_n_f = hug_n_1 + ' ' + hug_n_2
						hug_sex1 = vk_session.method('users.get', {'user_ids' : str(user), 'fields' : 'sex', 'name_case' : 'nom'})
						hug_sex0 = hug_sex1[0]
						hug_sex = json.dumps(hug_sex0['sex'])
						hug_sex_s = ''
						if int(hug_sex) == 1:
							hug_sex_s = 'обняла'
						if int(hug_sex) == 2:
							hug_sex_s = 'обнял'
						hug_w_u_n = vk.users.get(user_ids=hug_w_n)
						hug_w_1 = hug_w_u_n[0]["first_name"]
						hug_w_2 = hug_w_u_n[0]["last_name"]
						hug_w_n_f = hug_w_1 + ' ' + hug_w_2
						send(id, '[id' + str(user) + '|' + hug_n_f + '] ' + hug_sex_s + ' [id' + str(hug_w_n) + '|' + hug_w_n_f + ']', hug_p)

					if "сатира поцеловать" in event.obj.text.lower():
						if (len(te2xt) == 2):
							kiss_w_n = reply["from_id"]

						if (len(te2xt) == 3):
							kiss1 = msg.replace('сатира поцеловать ', '')
							kiss_w_n = kiss1.split("|")[0].replace("[id", "")

						###Идентификатор альбома ----- 277597858
						album_kiss = vk_u.photos.get(owner_id=-201980948, album_id=277597858)
						kiss_p1 = random.choice(album_kiss["items"])
						kiss_p = 'photo' + str(kiss_p1["owner_id"]) + "_" + str(kiss_p1["id"])

						kiss_n_u = vk.users.get(user_ids=user)
						kiss_n_1 = kiss_n_u[0]["first_name"]
						kiss_n_2 = kiss_n_u[0]["last_name"]
						kiss_n_f = kiss_n_1 + ' ' + kiss_n_2
						kiss_sex1 = vk_session.method('users.get', {'user_ids' : str(user), 'fields' : 'sex', 'name_case' : 'nom'})
						kiss_sex0 = kiss_sex1[0]
						kiss_sex = json.dumps(kiss_sex0['sex'])
						kiss_sex_s = ''
						if int(kiss_sex) == 1:
							kiss_sex_s = 'поцеловала'
						if int(kiss_sex) == 2:
							kiss_sex_s = 'поцеловал'
						kiss_w_u_n = vk.users.get(user_ids=kiss_w_n)
						kiss_w_1 = kiss_w_u_n[0]["first_name"]
						kiss_w_2 = kiss_w_u_n[0]["last_name"]
						kiss_w_n_f = kiss_w_1 + ' ' + kiss_w_2
						send(id, '[id' + str(user) + '|' + kiss_n_f + '] ' + kiss_sex_s + ' [id' + str(kiss_w_n) + '|' + kiss_w_n_f + ']', kiss_p)

					if "сатира отшлëпать" in event.obj.text.lower():
						if (len(te2xt) == 2):
							slap_w_n = reply["from_id"]

						if (len(te2xt) == 3):
							slap1 = msg.replace('сатира отшлëпать ', '')
							slap_w_n = slap1.split("|")[0].replace("[id", "")
						
						###Идентификатор альбома ----- 277598113
						album_slap = vk_u.photos.get(owner_id=-201980948, album_id=277598113)
						slap_p1 = random.choice(album_slap["items"])
						slap_p = 'photo' + str(slap_p1["owner_id"]) + "_" + str(slap_p1["id"])

						slap_n_u = vk.users.get(user_ids=user)
						slap_n_1 = slap_n_u[0]["first_name"]
						slap_n_2 = slap_n_u[0]["last_name"]
						slap_n_f = slap_n_1 + ' ' + slap_n_2
						slap_sex1 = vk_session.method('users.get', {'user_ids' : str(user), 'fields' : 'sex', 'name_case' : 'nom'})
						slap_sex0 = slap_sex1[0]
						slap_sex = json.dumps(slap_sex0['sex'])
						slap_sex_s = ''
						if int(slap_sex) == 1:
							slap_sex_s = 'отшлëпала'
						if int(slap_sex) == 2:
							slap_sex_s = 'отшлëпал'
						slap_w_u_n = vk.users.get(user_ids=slap_w_n, name_case='gen')
						slap_w_1 = slap_w_u_n[0]["first_name"]
						slap_w_2 = slap_w_u_n[0]["last_name"]
						slap_w_n_f = slap_w_1 + ' ' + slap_w_2
						send(id, '[id' + str(user) + '|' + slap_n_f + '] ' + slap_sex_s + ' [id' + str(slap_w_n) + '|' + slap_w_n_f + ']', slap_p)

					if "сатира трахнуть" in event.obj.text.lower():
						if (len(te2xt) == 2):
							fuck_w_n = reply["from_id"]

						if (len(te2xt) == 3):
							fuck1 = msg.replace('сатира трахнуть ', '')
							fuck_w_n = fuck1.split("|")[0].replace("[id", "")

						###Идентификатор альбома ----- 277598113
						album_fuck = vk_u.photos.get(owner_id=-201980948, album_id=277598113)
						fuck_p1 = random.choice(album_fuck["items"])
						fuck_p = 'photo' + str(fuck_p1["owner_id"]) + "_" + str(fuck_p1["id"])

						fuck_n_u = vk.users.get(user_ids=user)
						fuck_n_1 = fuck_n_u[0]["first_name"]
						fuck_n_2 = fuck_n_u[0]["last_name"]
						fuck_n_f = fuck_n_1 + ' ' + fuck_n_2
						fuck_sex1 = vk_session.method('users.get', {'user_ids' : str(user), 'fields' : 'sex', 'name_case' : 'nom'})
						fuck_sex0 = fuck_sex1[0]
						fuck_sex = json.dumps(fuck_sex0['sex'])
						fuck_sex_s = ''
						if int(fuck_sex) == 1:
							fuck_sex_s = 'принудила к интиму'
						if int(fuck_sex) == 2:
							fuck_sex_s = 'принудил к интиму'
						fuck_w_u_n = vk.users.get(user_ids=fuck_w_n, name_case='gen')
						fuck_w_1 = fuck_w_u_n[0]["first_name"]
						fuck_w_2 = fuck_w_u_n[0]["last_name"]
						fuck_w_n_f = fuck_w_1 + ' ' + fuck_w_2
						send(id, '[id' + str(user) + '|' + fuck_n_f + '] ' + fuck_sex_s + ' [id' + str(fuck_w_n) + '|' + fuck_w_n_f + ']', fuck_p)

					if "сатира сжечь" in event.obj.text.lower():
						if (len(te2xt) == 2):
							fire_w_n = reply["from_id"]

						if (len(te2xt) == 3):
							fire1 = msg.replace('сатира сжечь ', '')
							fire_w_n = fire1.split("|")[0].replace("[id", "")

						###Идентификатор альбома ----- 277598139
						album_fire = vk_u.photos.get(owner_id=-201980948, album_id=277598139)
						fire_p1 = random.choice(album_fire["items"])
						fire_p = 'photo' + str(fire_p1["owner_id"]) + "_" + str(fire_p1["id"])

						fire_n_u = vk.users.get(user_ids=user)
						fire_n_1 = fire_n_u[0]["first_name"]
						fire_n_2 = fire_n_u[0]["last_name"]
						fire_n_f = fire_n_1 + ' ' + fire_n_2
						fire_sex1 = vk_session.method('users.get', {'user_ids' : str(user), 'fields' : 'sex', 'name_case' : 'nom'})
						fire_sex0 = fire_sex1[0]
						fire_sex = json.dumps(fire_sex0['sex'])
						fire_sex_s = ''
						if int(fire_sex) == 1:
							fire_sex_s = 'сожгла'
						if int(fire_sex) == 2:
							fire_sex_s = 'сжёг'
						fire_w_u_n = vk.users.get(user_ids=fire_w_n)
						fire_w_1 = fire_w_u_n[0]["first_name"]
						fire_w_2 = fire_w_u_n[0]["last_name"]
						fire_w_n_f = fire_w_1 + ' ' + fire_w_2
						send(id, '[id' + str(user) + '|' + fire_n_f + '] ' + fire_sex_s + ' [id' + str(fire_w_n) + '|' + fire_w_n_f + ']', fire_p)		

					if msg in [COMMANDS[7]]:
						sender(id, f''+ JOIN)

					if msg in ['сатира курс доллара']:
						class Currency:
							DOLLAR_RUB = 'https://www.google.com/search?sxsrf=ALeKk01NWm6viYijAo3HXYOEQUyDEDtFEw%3A1584716087546&source=hp&ei=N9l0XtDXHs716QTcuaXoAg&q=%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80+%D0%BA+%D1%80%D1%83%D0%B1%D0%BB%D1%8E&oq=%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80+&gs_l=psy-ab.3.0.35i39i70i258j0i131l4j0j0i131l4.3044.4178..5294...1.0..0.83.544.7......0....1..gws-wiz.......35i39.5QL6Ev1Kfk4'
							headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}
							current_converted_price = 0

							def __init__(self):
								# Установка курса валюты при создании объекта
								self.current_converted_price = float(self.get_currency_price().replace(",", "."))

							# Метод для получения курса валюты
							def get_currency_price(self):
								full_page = requests.get(self.DOLLAR_RUB, headers=self.headers)
								soup = BeautifulSoup(full_page.content, 'html.parser')
								convert = soup.findAll("span", {"class": "DFlfde", "class": "SwHCTb", "data-precision": 2})
								return convert[0].text

							# Проверка изменения валюты
							def check_currency(self):
								currency = float(self.get_currency_price().replace(",", "."))
								sender(id, f'Курс доллара: ' + str(currency))

						# Создание объекта и вызов метода
						currency = Currency()
						currency.check_currency()

					if msg in ['сатира команды', 'сатира помощь', 'сатира помошь', 'сатира помощ']:
						with open('settings.json', encoding='utf-8') as f:
							data = json.load(f)
						sender(id, f''+ data["commands"])

					if "сатира похороны панка" in event.obj.text.lower():
						if str(user) in admin_from:
							dead_p = msgl.replace('Сатира похороны панка ', '')
							dead_d_n = dead_p.split("|")[0].replace("[id", "")
							dead_n_u = vk.users.get(user_ids=dead_d_n)
							dead_n_1 = dead_n_u[0]["first_name"]
							dead_n_2 = dead_n_u[0]["last_name"]
							dead_n_1f = dead_n_1 + ' ' + dead_n_2
							dead_n_f = '[id' + str(dead_d_n) + '|' + dead_n_1f + '] '
							
							if dead_p in ['https://vk.com/maaaasyyyniiik', '[id400484262|@maaaasyyyniiik]']:
								sender(id, f'Панк никогда не умрёт!')

							if dead_p in ['https://vk.com/id504945503', '[id504945503|@ikadicccc]']:
								sender(id, f'Панк никогда не умрёт!')

							else:
								sender(id, dead_n_f + ' скоро умрёт<br>Скажи свою прощальную речь,<br>У тебя есть 15 секунд, время пошло')
								time.sleep(5)
								sender(id, f'Осталось: 10 секунд')
								time.sleep(5)
								sender(id, f'Осталось: 5 секунд')
								time.sleep(5)
								send(id, f'*псссссс притворись что умер<br>Ок?', 'audio-201980948_456239022')
						else:
							sender(id, 'Вы не являетесь панокм')
											
					if msg in ['сатира админы']:
						kpad58 = open('admins.txt','r')
						klad57 = kpad58.read()
						sender(id, f'Создатели: <br>[id360873634|Александр Ртищев] [id400484262|Дмитрий Князев]<br>Админы этой беседы:<br>' + klad57)
						kpad58.close()

					if "сатира ударить" in event.obj.text.lower():
						if (len(te2xt) == 2):
							hit_w_n = reply["from_id"]

						if (len(te2xt) == 3):
							hit1 = msg.replace('сатира ударить ', '')
							hit_w_n = hit1.split("|")[0].replace("[id", "")

						###Идентификатор альбома ----- 277598253
						album_hit = vk_u.photos.get(owner_id=-201980948, album_id=277598253)
						hit_p1 = random.choice(album_hit["items"])
						hit_p = 'photo' + str(hit_p1["owner_id"]) + "_" + str(hit_p1["id"])

						hit_n_u = vk.users.get(user_ids=user)
						hit_n_1 = hit_n_u[0]["first_name"]
						hit_n_2 = hit_n_u[0]["last_name"]
						hit_n_f = hit_n_1 + ' ' + hit_n_2
						hit_sex1 = vk_session.method('users.get', {'user_ids' : str(user), 'fields' : 'sex', 'name_case' : 'nom'})
						hit_sex0 = hit_sex1[0]
						hit_sex = json.dumps(hit_sex0['sex'])
						hit_sex_s = ''
						if int(hit_sex) == 1:
							hit_sex_s = 'ударила'
						if int(hit_sex) == 2:
							hit_sex_s = 'ударил'
						hit_w_u_n = vk.users.get(user_ids=hit_w_n)
						hit_w_1 = hit_w_u_n[0]["first_name"]
						hit_w_2 = hit_w_u_n[0]["last_name"]
						hit_w_n_f = hit_w_1 + ' ' + hit_w_2
						send(id, '[id' + str(user) + '|' + hit_n_f + '] ' + hit_sex_s + ' [id' + str(hit_w_n) + '|' + hit_w_n_f + ']', hit_p)

					if "сатира кража" in event.obj.text.lower():
						if (len(te2xt) == 2):
							steal_w_n = reply["from_id"]

						if (len(te2xt) == 3):
							steal1 = msg.replace('сатира кража ', '')
							steal_w_n = steal1.split("|")[0].replace("[id", "")
							
						steal_11 = ['трусы', 'трусы', 'трусы', 'девственность']

						###Идентификатор альбома ----- 277598193
						album_steal = vk_u.photos.get(owner_id=-201980948, album_id=277598193)
						steal_p1 = random.choice(album_steal["items"])
						steal_p = 'photo' + str(steal_p1["owner_id"]) + "_" + str(steal_p1["id"])

						steal_n_u = vk.users.get(user_ids=user)
						steal_n_1 = steal_n_u[0]["first_name"]
						steal_n_2 = steal_n_u[0]["last_name"]
						steal_n_f = steal_n_1 + ' ' + steal_n_2
						steal_sex1 = vk_session.method('users.get', {'user_ids' : str(user), 'fields' : 'sex', 'name_case' : 'nom'})
						steal_sex0 = steal_sex1[0]
						steal_sex = json.dumps(steal_sex0['sex'])
						steal_sex_s = ''
						if int(steal_sex) == 1:
							steal_sex_s = 'украла ' + random.choice(steal_11) + ' у'
						if int(steal_sex) == 2:
							steal_sex_s = 'украл ' + random.choice(steal_11) + ' у'
						steal_w_u_n = vk.users.get(user_ids=steal_w_n)
						steal_w_1 = steal_w_u_n[0]["first_name"]
						steal_w_2 = steal_w_u_n[0]["last_name"]
						steal_w_n_f = steal_w_1 + ' ' + steal_w_2
						send(id, '[id' + str(user) + '|' + steal_n_f + '] ' + steal_sex_s + ' [id' + str(steal_w_n) + '|' + steal_w_n_f + ']', steal_p)	

					if msg in ['сатира загрустить']:
						###Идентификатор альбома ----- 277598026
						album_sad = vk_u.photos.get(owner_id=-201980948, album_id=277598026)
						sad_p1 = random.choice(album_sad["items"])
						sad_p = 'photo' + str(sad_p1["owner_id"]) + "_" + str(sad_p1["id"])

						sad_n_u = vk.users.get(user_ids=user)
						sad_n_1 = sad_n_u[0]["first_name"]
						sad_n_2 = sad_n_u[0]["last_name"]
						sad_n_f = sad_n_1 + ' ' + sad_n_2
						send(id, '[id' + str(user) + '|' + sad_n_f + '] ' + 'грустит', sad_p)

					if msg in ['сатира орел и решка', 'сатира монетка']:
						o_and_r = ['Выпал орёл', 'Выпала решка']
						r232313 = random.choice(o_and_r)
						sender(id, f'' + r232313)

					if "сатира рассылка+" in event.obj.text.lower():
						rl1 = msgl.replace('Сатира рассылка+ ', '')
						rl2 = rl1.replace('сатира рассылка+ ', '')
						if str(user) in admin_from:
								sender(1, f'Внимание @all!<br>Рассылка от администрации:<br>' + rl2)
								sender(11, f'Внимание @all!<br>Рассылка от администрации:<br>' + rl2)
						else:
							sender(id, f'У вас нет прав доступа')

					if msg in ['bts+']:
						sendBTS()

					#############ПЕРЕДЕЛАТЬ#####################ПЕРЕДЕЛАТЬ#######################ПЕРЕДЕЛАТЬ#####################ПЕРЕДЕЛАТЬ##########################	
					if "сатира админ+" in event.obj.text.lower():
						admin_p_l = msg.replace('сатира админ+ ', '')
						admin_p_id = admin_p_l.split("|")[0].replace("[id", "")
						if str(user) in ['400484262', '360873634', '504945503']:

							with open('users.json', encoding='utf-8') as f:
								data = json.load(f)

							data[str(user)]["role"] = "Админ"

							with open('users.json', 'w', encoding='utf-8') as f:
								json.dump(data, f, ensure_ascii=False, indent=4)

							with open('settings.json', encoding='utf-8') as f:
								data = json.load(f)

							a_list = []
							a_list.append(str(admin_p_id))

							data["admins"] = data["admins"] + a_list

							with open('settings.json', 'w', encoding='utf-8') as f:
								json.dump(data, f, ensure_ascii=False, indent=4)

							admin_p_u = vk.users.get(user_ids=admin_p_id)
							admin_p_n_1 = admin_p_u[0]["first_name"]
							admin_p_n_2 = admin_p_u[0]["last_name"]
							admin_p_n_f = admin_p_n_1 + ' ' + admin_p_n_2
								
							kpad8 = open('admins.txt','w')
							kpad8.write(klad57 + '\n' + '[id' + str(admin_p_id) + '|' + admin_p_n_f + ']') 
							sender(id, f'Готово!')
							kpad8.close()

						else:
							sender(id, f'У вас нет доступа')

					#############ПЕРЕДЕЛАТЬ#####################ПЕРЕДЕЛАТЬ#######################ПЕРЕДЕЛАТЬ#####################ПЕРЕДЕЛАТЬ##########################	
					if "сатира админ-" in event.obj.text.lower():
						admin_m_l = msg.replace('сатира админ- ', '')
						admin_m_id = admin_p_l.split("|")[0].replace("[id", "")
						if str(user) in ['400484262', '360873634', '504945503']:
							kpad58 = open('admins.txt','r')
							klad57 = kpad58.read()
							kpad58.close()

							role = open('profiles\\role\\' + str(admin_m_id) + '.txt', 'w')
							role.write('Участник')
							role.close()

							admin_m_u = vk.users.get(user_ids=admin_m_id)
							admin_m_n_1 = admin_m_u[0]["first_name"]
							admin_m_n_2 = admin_m_u[0]["last_name"]
							admin_m_n_f = admin_m_n_1 + ' ' + admin_m_n_2

							try:
								'''admin_int_f_e = open('profiles\\admins_int.txt', 'r')
								admin_from_e = admin_int_f_e.read()
								admin_int_f_e.close()'''

								with open('settings.json', encoding='utf-8') as f:
									data = json.load(f)

								del data["admins"]["8950"]

								with open('settings.json', 'w', encoding='utf-8') as f:
									json.dump(data, f, ensure_ascii=False, indent=4)

								'''dyts57 = klad57.replace('[id' + str(admin_m_id) + '|' + admin_m_n_f + ']', "")
								admin_m_int = admin_from_e.replace('\n' + admin_m_id, '')
								admin_int_f_w = open('profiles\\admins_int.txt', 'w')
								admin_int_f_w.write(admin_m_int)
								admin_int_f_w.close()'''
							except:
								sender(id, f'Ошибка! Данный пользователь не является админом')

							'''kpad8 = open('admins.txt','w')
							klad7 = kpad8.write(dyts57) 
							sender(id, f'Готово!')
							kpad8.close()'''

						else:
							sender(id, f'Вам отказано в доступе')
										
					if msg in ['сатира рок']:
						r1 = random.choice(rock1)
						r2 = random.choice(rock2)
						r3 = random.choice(rock3)
						r4 = random.choice(rock4)
						r5 = random.choice(rock5)

						sad_n_u = vk.users.get(user_ids=user)
						sad_n_1 = sad_n_u[0]["first_name"]
						sad_n_2 = sad_n_u[0]["last_name"]
						sad_n2_f = sad_n_1 + ' ' + sad_n_2
						sad_n_f = '[id' + str(user) + '|' + sad_n2_f + ']'

						send(id, sad_n_f + ' - в рядях панков!<br>ХОЙ🤘', r1 + ',' + r2 + ',' + r3 + ',' + r4 + ',' + r5)	

					if "сатира вики" in event.obj.text.lower():
						qies3t_wiki = msg.replace("сатира вики ", "")
						try:
							wiki_redsult = str(wikipedia.summary(qies3t_wiki))
							sewnd_wiki = "Вот что я нашла: <br>" + wiki_redsult
							sender(id, f'' + sewnd_wiki)
						except:
							sender(id, f'По вашему запросу ничего не найдено')

					if "сатира ник" in event.obj.text.lower():
						nick = msgl.split(" ",2)
						with open('users.json', encoding='utf-8') as f:
							data = json.load(f)

						data[str(user)]["nick"] = str(nick[2])

						with open('users.json', 'w', encoding='utf-8') as f:
							json.dump(data, f, ensure_ascii=False, indent=4)

						sender(id, f'Готово!')

					if msg in ['сатира профиль']:
						with open('users.json', encoding='utf-8') as f:
							prof = json.load(f)

						sender(id, f'Имя: ' + prof[str(user)]["id_name"] + '<br>Айди: ' + str(user) + '<br>Роль: ' + prof[str(user)]["role"] + '<br>Ник: ' + prof[str(user)]["nick"] + '<br>Дети: ' + prof[str(user)]["kid"]  + '<br>Деньги: ' + str(prof[str(user)]["money"]) + '<br>Варны: ' + str(prof[str(user)]["warn"]) + '/3')

					if "варн+" in event.obj.text.lower():
						if str(user) in admin_from:

							warn_m_u = vk.users.get(user_ids=user)
							warn_m_u_m_n_1 = warn_m_u[0]["first_name"]
							warn_m_u_m_n_2 = warn_m_u[0]["last_name"]
							warn_m_u_m_n_f = warn_m_u_m_n_1 + ' ' + warn_m_u_m_n_2
							warn_user_m = '[id' + str(user) + '|' + warn_m_u_m_n_f + ']'

							sp_msg_w_p = msgl.split(" ",2)
							drtg1 = int(sp_msg_w_p[1].split("|")[0].replace("[id", ""))

							warn1_m_u = vk.users.get(user_ids=drtg1)
							warn1_m_u_m_n_1 = warn1_m_u[0]["first_name"]
							warn1_m_u_m_n_2 = warn1_m_u[0]["last_name"]
							warn1_m_u_m_n_f = warn1_m_u_m_n_1 + ' ' + warn_m_u_m_n_2
							warn1_user_m = '[id' + str(drtg1) + '|' + warn1_m_u_m_n_f + ']'

							with open('users.json', encoding='utf-8') as f:
								data = json.load(f)
							rtryh6 = int(data[str(drtg1)]["warn"]) + 1
							if str(rtryh6) == '3':
								sender(id, warn1_user_m + ' получил(а) максимальное колличество предупреждений 3/3')
								vk.messages.removeChatUser(chat_id='1', user_id=str(drtg1))
							else:
								with open('users.json', encoding='utf-8') as f:
									data = json.load(f)

								warn_w_p = int(data[str(drtg1)]["warn"]) + 1

								data[str(drtg1)]["warn"] = int(warn_w_p)

								with open('users.json', 'w', encoding='utf-8') as f:
									json.dump(data, f, ensure_ascii=False, indent=4)

								try:
									sender(id, f'Готово!<br>Всего предупреждений: ' + str(rtryh6) + '/3<br>Модератор: ' + warn_user_m + '<br>Причина: ' + sp_msg_w_p[2])
								except:
									sender(id, f'Готово!<br>Всего предупреждений: ' + str(rtryh6) + '/3<br>Модератор: ' + warn_user_m)

						else:
							sender(id, f'Вам отказано в доступе')

					if "варн-" in event.obj.text.lower():
						try:
							if str(user) in admin_from:
								id_warns = msg.replace('варн- ', '')
								drtg0 = id_warns.split("|")[0].replace("[id", "")
								with open('users.json', encoding='utf-8') as f:
									data = json.load(f)

								rt9 = data[str(drtg0)]["warn"]
								if str(rt9) == '0':
									warn_m_u = vk.users.get(user_ids=drtg0, name_case='acc')
									warn_m_n_1 = warn_m_u[0]["first_name"]
									warn_m_n_2 = warn_m_u[0]["last_name"]
									warn_m_n_f = warn_m_n_1 + ' ' + warn_m_n_2
									sender(id, 'У ' + '[id' + drtg0 + '|' + warn_m_n_f + ']' + ' нет предупреждений')

								else:
									rtryh62 = int(rt9) - 1
									data[str(drtg0)]["warn"] = int(rtryh62)
									with open('users.json', 'w', encoding='utf-8') as f:
										json.dump(data, f, ensure_ascii=False, indent=4)
									sender(id, f'Готово!<br>Всего предупреждений: ' + str(rtryh62))
							else:
								sender(id, f'У вас нет доступа')
						except:
							sender(id, f'Данного пользователя не существует')

					if "сатира профиль чужой" in event.obj.text.lower():
						try:
							chprof = msg.split(" ", 4)
							drcht9 = chprof[3].split("|")[0].replace("[id", "")
							with open('users.json', encoding='utf-8') as f:
								prof = json.load(f)

							sender(id, f'Имя: ' + prof[str(drcht9)]["id_name"] + '<br>Айди: ' + str(drcht9) + '<br>Роль: ' + prof[str(drcht9)]["role"] + '<br>Ник: ' + prof[str(drcht9)]["nick"] + '<br>Дети: ' + prof[str(drcht9)]["kid"]  + '<br>Деньги: ' + str(prof[str(drcht9)]["money"]) + '<br>Варны: ' + str(prof[str(drcht9)]["warn"]) + '/3')

						except:
							sender(id, f'Данного пользователя не существует')

					if "сатира айди числовое" in event.obj.text.lower():
						try:
							chp3rof = msg.replace("сатира айди числовое ", "")
							dfkqw2 = chp3rof.split("|")[0].replace("[id", "")
							sender(id, f'' + str(dfkqw2))
						except:
							sender(id, f'Данного пользователя не существует')

					if "пк выкл" in event.obj.text.lower():
						if user == 400484262:
							try:
								frg4 = msg.replace("пк выкл ", "")
								os.system("shutdown /s /t " + str(frg4))
								sender(id, f'ПК отключится через ' + str(frg4) + ' секунд(ы)')
							except:
								sender(id, f'ПК OFF')
								os.system("shutdown /s /t " + str(frg4))
						else:
							sender(id, f'Многочлен')

					if "пк перезагрузка" in event.obj.text.lower() or "пк ребут" in event.obj.text.lower():
						if user == 400484262:
							frg4 = msg.replace("пк ребут ", "")
							sender(id, f'ПК перезагрузится через ' + str(frg4) + ' секунд(ы)')
							os.system("shutdown /r /t " + str(frg4))
						else:
							sender(id, f'Многочлен')

					if "сатира брак запрос" in event.obj.text.lower():
						marry_l = msg.split(" ", 3)
						marry_l_u = marry_l[3].split("|")[0].replace("[id", "")

						marry_k = VkKeyboard(**settings)
						marry_k.add_callback_button(label='❤ Согласиться', color=VkKeyboardColor.PRIMARY, payload={"type": "marry_q"})

						marry_u = vk.users.get(user_ids=marry_l_u, name_case='nom')
						marry_n_1 = marry_u[0]["first_name"]
						marry_n_2 = marry_u[0]["last_name"]
						marry_n_f = marry_n_1 + ' ' + marry_n_2
						marry_n_f_n = '[id' + str(marry_l_u) + '|' + marry_n_f + ']'

						marry = []

						marry = [str(user)] + [str(marry_l_u)]

						with open('marry.json', encoding='utf-8') as f:
							data = json.load(f)

						a_dict = ({"marry": marry})

						data.update(a_dict)

						with open('marry.json', 'w', encoding='utf-8') as f:
							json.dump(data, f, ensure_ascii=False, indent=4)

						send_key(id, marry_n_f_n + ', для подтверждения нажмите на кнопку ниже', marry_k.get_keyboard())

					if "брак принять" in event.obj.text.lower():
						if str(user) in marry[1]:
							marry_u_1 = vk.users.get(user_ids=marry[0], name_case='nom')
							marry_n_1_1 = marry_u_1[0]["first_name"]
							marry_n_2_1 = marry_u_1[0]["last_name"]
							marry_n_f_1 = marry_n_1_1 + ' ' + marry_n_2_1
							marry_n_f_n_1 = '[id' + str(marry[0]) + '|' + marry_n_f_1 + ']'

							marry_u_2 = vk.users.get(user_ids=marry[1], name_case='nom')
							marry_n_1_2 = marry_u_2[0]["first_name"]
							marry_n_2_2 = marry_u_2[0]["last_name"]
							marry_n_f_2 = marry_n_1_2 + ' ' + marry_n_2_2
							marry_n_f_n_2 = '[id' + str(marry[1]) + '|' + marry_n_f_2 + ']'

							with open('marry.json', encoding='utf-8') as f:
								data = json.load(f)

							a_dict = ({str(marry[0]): {"partner": marry[1], "i_am_id": marry_n_f_n_1, "partner_id": marry_n_f_n_2, "time": a_time}})
							b_dict = ({str(marry[1]): {"partner": marry[0], "i_am_id": marry_n_f_n_2, "partner_id": marry_n_f_n_1, "time": a_time}})

							data.update(a_dict)
							data.update(b_dict)

							with open('marry.json', 'w', encoding='utf-8') as f:
								json.dump(data, f, ensure_ascii=False, indent=4)

							sender(id, 'Свадьба!')
						else:
							sender(id, 'У вас нет ожидающих запросов на брак')

					if msg in ['сатира браки']:
						with open('marry.json', encoding='utf-8') as f:
							data = json.load(f)
						sender(id, f'Браки этой беседы: <br>' + str(data))

					if msg in ['сатира']:
						helo_s = ['Приветствую! Чем могу помочь?', 'Приветствую!<br>Мои команды можешь узнать написав Cатира помощь']
						sender(id, '' + random.choice(helo_s))
						
					if msg in ['отклик', 'сатира отклик']:
						f43 = time.time()
						sender(id, str(f43) + ' мс')
					
					if "сатира кнб" in event.obj.text.lower():
						kmb11 = msg.split(" ", 3)
						kmb1 = kmb11[2]
						kmb2 = ['камень', 'ножницы', 'бумага']
						kmb3 = random.choice(kmb2)
						if kmb1 == 'камень':
							if kmb3 == 'камень':
								sender(id, 'Камень<br>Ничья!')
							if kmb3 == 'ножницы':
								sender(id, 'Ножницы<br>Вы выйграли')
							if kmb3 == 'бумага':
								sender(id, 'Бумага<br>Вы проиграли')
								
						if kmb1 == 'ножницы':
							if kmb3 == 'ножницы':
								sender(id, 'Ножницы<br>Ничья!')
							if kmb3 == 'камень':
								sender(id, 'Камень<br>Вы проиграли')
							if kmb3 == 'бумага':
								sender(id, 'Бумага<br>Вы выйграли')

						if kmb1 == 'бумага':
							if kmb3 == 'бумага':
								sender(id, 'Бумага<br>Ничья!')
							if kmb3 == 'ножницы':
								sender(id, 'Ножницы<br>Вы проиграли')
							if kmb3 == 'камень':
								sender(id, 'Камень<br>Вы выйграли')

					if (len(te2xt) == 2) and te2xt[0] == "кик":
						if str(user) in admin_from:
							try:
								if get_user(te2xt[1]) in admin_from:
									sender(id, "Вы не можете исключить данного пользователя")
								else:
									vk.messages.removeChatUser(chat_id=chat_id1, user_id=get_user(te2xt[1]))
							except Exception as e:
								if str(e) == "[935] User not found in chat":
									sender(id, 'Этого пользователя нет в этом чате')
						else:
							sender(id, 'Вам отказано в доступе')

					if (len(te2xt) == 1) and te2xt[0] == "кик":
						if str(user) in admin_from:
							try:
								if reply["from_id"] in admin_from:
									sender(id, "Невозможно исключить данного пользователя")
								else:
									vk.messages.removeChatUser(chat_id=chat_id1, user_id=reply["from_id"])
							except Exception as e:
								if str(e) == "[935] User not found in chat":
									sender(id, 'Этого пользователя нет в этом чате')
						
						else:
							sender(id, 'Вам отказано в доступе')

					if msg in ["бот"]:
						sender(id, "На месте✅")

					if msg in ["инквизиция"]:
						if str(user) in admin_from:
							userclfo = vk.messages.getConversationMembers(peer_id=id)
							user_r_fef = userclfo["items"]
							user_r_fef_l = random.choice(user_r_fef)
							user_r_fef_l_o = user_r_fef_l["member_id"]

							user_r_u = vk.users.get(user_ids=user_r_fef_l_o, name_case='nom')
							user_r_n_1 = user_r_u[0]["first_name"]
							user_r_n_2 = user_r_u[0]["last_name"]
							user_r_n_f = user_r_n_1 + ' ' + user_r_n_2
							user_n_f_n = '[id' + str(user_r_fef_l_o) + '|' + user_r_n_f + ']'

							user_r_u2 = vk.users.get(user_ids=user, name_case='nom')
							user_r_n_12 = user_r_u2[0]["first_name"]
							user_r_n_22 = user_r_u2[0]["last_name"]
							user_r_n_f2 = user_r_n_12 + ' ' + user_r_n_22
							user_n_f_n2 = '[id' + str(user) + '|' + user_r_n_f2 + ']'

							if str(user_r_fef_l_o) in admin_from:
								sender(id, 'Преступник не был пойман')
							else:
								sender(id, user_n_f_n + ' приговорён к инквизиции<br>Инквизитор: ' + user_n_f_n2)
								id_k_w3er = id - 2000000000
								vk.messages.removeChatUser(chat_id=id_k_w3er, user_id=str(user_r_fef_l_o))

						else:
							sender(id, f'Вам отказано в доступе')

					if "сатира кто" in event.obj.text.lower():
						user_q_r = msgl.split(" ", 2)
						userclfo = vk.messages.getConversationMembers(peer_id=id)
						user_r_fef = userclfo["items"]
						user_r_fef_l = random.choice(user_r_fef)
						user_r_fef_l_o = user_r_fef_l["member_id"]

						user_r_u = vk.users.get(user_ids=user_r_fef_l_o, name_case='nom')
						user_r_n_1 = user_r_u[0]["first_name"]
						user_r_n_2 = user_r_u[0]["last_name"]
						user_r_n_f = user_r_n_1 + ' ' + user_r_n_2
						user_n_f_n = '[id' + str(user_r_fef_l_o) + '|' + user_r_n_f + ']'

						who_acept = ['Я думаю ' + str(user_q_r[2]) + ' ' + user_n_f_n, 'Хмммм, мне кажется ' + user_q_r[2] + " - " + user_n_f_n]

						sender(id, random.choice(who_acept))

					if "сатира инфа" in event.obj.text.lower() or "сатира как думаешь" in event.obj.text.lower():
						infa_ra = random.randint(0, 100)
						sender(id, 'Я думаю это ' + str(infa_ra) + '%')

					if "сатира секс" in event.obj.text.lower():
						if (len(te2xt) == 2):
							r_sex_l_u = reply["from_id"]

						if (len(te2xt) == 3):
							r_sex_l = msg.replace('сатира секс ', '')
							r_sex_l_u = r_sex_l.split("|")[0].replace("[id", "")

						sex_a = VkKeyboard(**settings)
						sex_a.add_callback_button(label='Подтвердить', color=VkKeyboardColor.POSITIVE, payload={"type": "sex_a"})

						r_sex_u = vk.users.get(user_ids=r_sex_l_u, name_case='nom')
						r_sex_n_1 = r_sex_u[0]["first_name"]
						r_sex_n_2 = r_sex_u[0]["last_name"]
						r_sex_n_f = r_sex_n_1 + ' ' + r_sex_n_2
						r_sex_n_f_n = '[id' + str(r_sex_l_u) + '|' + r_sex_n_f + ']'
						

						r_sex = [str(user)] + [str(r_sex_l_u)]

						vk_session.method("messages.send", {"peer_id": id, "message": r_sex_n_f_n + ', для подтверждения нажмите на кнопку ниже', "random_id": 0, "keyboard": sex_a.get_keyboard()})

					if "деньги" in event.obj.text.lower():
						with open('users.json', encoding='utf-8') as f:
							data = json.load(f)

						sender(id, str(data[str(user)]["money"]))

					if "деньги+" in event.obj.text.lower():
						if str(user) in admin_from:
							money_s_p = msg.split(" ", 3)
							money_p_u = money_s_p[1].split("|")[0].replace("[id", "")

							with open('users.json', encoding='utf-8') as f:
								data = json.load(f)

							money_w_p = int(data[str(money_p_u)]["money"]) + int(money_s_p[2])

							data[str(money_p_u)]["money"] = int(money_w_p)

							with open('users.json', 'w', encoding='utf-8') as f:
								json.dump(data, f, ensure_ascii=False, indent=4)


							money_u_n_p = vk.users.get(user_ids=money_p_u, name_case='acc')
							money_u_n_1 = money_u_n_p[0]["first_name"]
							money_u_n_2 = money_u_n_p[0]["last_name"]
							money_u_n_l = money_u_n_1 + ' ' + money_u_n_2
							money_u_n_f = '[id' + str(money_p_u) + '|' + money_u_n_l + ']'

							sender(id, '+' + str(money_s_p[2]) + ' рублей добавлено к счёту ' + money_u_n_f + '<br>Баланс: ' + str(money_w_p))

						else:
							sender(id, f'Вам отказано в доступе')

					if "деньги-" in event.obj.text.lower():
						if str(user) in admin_from:
							money_s_p = msg.split(" ", 3)
							money_p_u = money_s_p[1].split("|")[0].replace("[id", "")

							with open('users.json', encoding='utf-8') as f:
								data = json.load(f)

							money_w_p = int(data[str(money_p_u)]["money"]) - int(money_s_p[2])

							data[str(money_p_u)]["money"] = int(money_w_p)

							with open('users.json', 'w', encoding='utf-8') as f:
								json.dump(data, f, ensure_ascii=False, indent=4)


							money_u_n_p = vk.users.get(user_ids=money_p_u, name_case='acc')
							money_u_n_1 = money_u_n_p[0]["first_name"]
							money_u_n_2 = money_u_n_p[0]["last_name"]
							money_u_n_l = money_u_n_1 + ' ' + money_u_n_2
							money_u_n_f = '[id' + str(money_p_u) + '|' + money_u_n_l + ']'

							sender(id, '+' + str(money_s_p[2]) + ' рублей добавлено к счёту ' + money_u_n_f + '<br>Баланс: ' + str(money_w_p))

						else:
							sender(id, f'Вам отказано в доступе')

					if msg in ['сатира кинь порно']:	

						vid = vks.video.search(q='Порно', count=100, adult=1)
						vidH = vid['items']
						vidHc = random.choice(vidH)
						vid_id = vidHc['id']
						vid_oid = vidHc['owner_id']

						vid_offset = 'video' + str(vid_oid) + '_' + str(vid_id)

						send(id, '', vid_offset)

					if msg in ['сатира кинь хентай']:

						vid = vks.video.search(q='Хентай аниме', count=100, adult=1)
						vidH = vid['items']
						vidHc = random.choice(vidH)
						vid_id = vidHc['id']
						vid_oid = vidHc['owner_id']

						vid_offset = 'video' + str(vid_oid) + '_' + str(vid_id)

						send(id, '', vid_offset)

					if "фото поиск" in event.obj.text.lower():
						photo_s_l = msg.split(" ", 2)
						photo_s = vks.photos.search(q=photo_s_l[2],sort=1)
						photo_s_r = photo_s['items']
						photo_s_r_l = random.choice(photo_s_r)
						photo_oid = photo_s_r_l['owner_id']
						photo_id = photo_s_r_l['id']
						photo_s_f = 'photo' + str(photo_oid) + '_' + str(photo_id)
						send(id, '', photo_s_f)

					if "видео поиск" in event.obj.text.lower():
						video_s_l = msg.split(" ", 2)
						video_s = vks.video.search(q=video_s_l[2], count=100, adult=1, filters='youtube')
						video_s_r = video_s['items']
						video_s_r_l = random.choice(video_s_r)
						video_oid = video_s_r_l['owner_id']
						video_id = video_s_r_l['id']
						video_s_f = 'video' + str(video_oid) + '_' + str(video_id)
						send(id, '', video_s_f)

					if "репорт" in event.obj.text.lower() or "жалоба" in event.obj.text.lower():
						report_m_s = msg.split(" ", 2)
						report_ex_u = report_m_s[1].split("|")[0].replace("[id", "")

						report_u_n_pu = vk.users.get(user_ids=user, name_case='acc')
						report_u_n_1u = report_u_n_pu[0]["first_name"]
						report_u_n_2u = report_u_n_pu[0]["last_name"]
						report_u_n_lu = report_u_n_1u + ' ' + report_u_n_2u
						report_u_n_fu = '[id' + str(user) + '|' + report_u_n_lu + ']'

						report_u_n_p = vk.users.get(user_ids=report_ex_u, name_case='nom')
						report_u_n_1 = report_u_n_p[0]["first_name"]
						report_u_n_2 = report_u_n_p[0]["last_name"]
						report_u_n_l = report_u_n_1 + ' ' + report_u_n_2
						report_u_n_f = '[id' + str(report_ex_u) + '|' + report_u_n_l + ']'

						report_u_n_pr = vk.users.get(user_ids=report_ex_u, name_case='acc')
						report_u_n_1r = report_u_n_pr[0]["first_name"]
						report_u_n_2r = report_u_n_pr[0]["last_name"]
						report_u_n_lr = report_u_n_1r + ' ' + report_u_n_2r
						report_u_n_fr = '[id' + str(report_ex_u) + '|' + report_u_n_lr + ']'

						report_sex1 = vk_session.method('users.get', {'user_ids' : str(report_ex_u), 'fields' : 'sex', 'name_case' : 'nom'})
						report_sex0 = report_sex1[0]
						report_sex = json.dumps(report_sex0['sex'])
						report_sex_s = ''
						if int(report_sex) == 1:
							report_sex_s = 'Обвиняемая: '
						if int(report_sex) == 2:
							report_sex_s = 'Обвиняемый: '

						try:
							a = report_m_s[2]
						except:
							report_m_s.append("None")

						report_k = VkKeyboard(**settings)
						report_k.add_callback_button(label='Обжаловать', color=VkKeyboardColor.PRIMARY, payload={"type": "report_appeal"})
						report_k.add_line()
						report_k.add_callback_button(label='Выдать варн', color=VkKeyboardColor.PRIMARY, payload={"type": "report_warn"})
						print("что")
						send_key(2000000011, 'От ' + report_u_n_fu + ' поступила жалоба<br>' + report_sex_s + report_u_n_f + '<br>Текст жалобы: ' + report_m_s[2], report_k.get_keyboard())
						sender(id, 'Жалоба на ' + report_u_n_fr + ' отправлена')
						
					if msg in ["прочесть", "прочитать"]:
						try:
							if reply["attachments"][0]["type"] == "audio_message":
								if reply["attachments"][0]["audio_message"]["transcript"] == "":
									sender(id, 'Слова в сообщении не распознаны')
								else:
									sender(id, 'Текст голового сообщения:<br>' + reply["attachments"][0]["audio_message"]["transcript"])
							else:
								sender(id, "Прочесть можно только голосовое сообщение")

						except Exception as e:
							print(e)
							sender(id, "Прочесть можно только голосовое сообщение")

					if msg in ["сатира онлайн"]:
						f = vk.messages.getConversationMembers(peer_id=id, fields="online")
						al = -1
						sw_all = ""
						try:
							while True:
								al = al + 1
								sw1 = f["profiles"][al]["first_name"]
								sw2 = f["profiles"][al]["last_name"]
								sw3 = f["profiles"][al]["id"]
								sw4 = f["profiles"][al]["online"]
								if sw4 == 1:
									sw_al = "[id" + str(sw3) + "|" + sw1 + " " + sw2 + "]"
									sw_all += "<br>" + sw_al
						except:
							sender(id, 'Пользователи онлайн:' + sw_all)

					if msg in ["сатира курс биткоина"]:
						url = 'https://www.rbc.ru/crypto/currency/btcusd'
						response = requests.get(url)
						soup = BeautifulSoup(response.text, 'lxml')
						quotes = soup.find_all('div', class_='chart__subtitle js-chart-value')
						aswqr = str(quotes).replace('[<div class="chart__subtitle js-chart-value">', '')
						de = aswqr.split(" ")
						sender(id, "Курс биткоина: " + de[12] + " " + de[13].replace("\n", "") + " USD")

					if msg in ["пинг"]:
						ping_msg = ["29", "29", "29", "29", "30", "31"]
						sender(id, "Текущее состояние платформы:<br>messages: " + random.choice(ping_msg) + " мс<br>Uptime: 100%")

					if msg in ["сатира коронавирус"]:
						url = 'https://koronavirus-today.ru/covid-19'
						response = requests.get(url)
						soup = BeautifulSoup(response.text, 'lxml')
						quotes = soup.find_all('div', class_='stat_container')
						infected = quotes[1].find_all('p')
						infected_p = quotes[1].find('p', class_="plus_confirmed")
						dead = quotes[1].find_all('p')
						dead_p = quotes[1].find('p', class_="plus_death")
						recovered = quotes[1].find_all('p')
						recovered_p = quotes[1].find('p', class_="plus_recovered")
						kowid_send = "Статистика коронавируса в России<br>Заражённых:<br>" + infected[0].text + " " + infected_p.text + "<br>Погибших:<br>" + dead[2].text + " " + dead_p.text + "<br>Выздоровели:<br>" + recovered[4].text + " " + recovered_p.text

						koronavirus = VkKeyboard(**settings)
						koronavirus.add_callback_button(label='Мир', color=VkKeyboardColor.PRIMARY, payload={"type": "koronavirus_menu"})
						send_key(id, kowid_send, koronavirus.get_keyboard())

					'''if msg in ["жмых"]:
						audio = reply["attachments"][0]['audio_message']['link_ogg']
						filename = "files/" + os.path.basename(audio).split('?')[0]
						r = requests.get(audio)
						with open(filename, 'wb') as f:
							f.write(r.content)

						if(os.path.isfile('files/render1.ogg')): os.remove('files/render1.ogg')
						if(os.path.isfile('files/render2.ogg')): os.remove('files/render2.ogg')

						cmd = f'ffmpeg -i {filename} -af "chorus=0.5:0.9:50|60|40:0.4|0.32|0.3:0.25|0.4|0.3:2|2.3|1.3" files/render1.ogg'
						os.system(cmd)

						cmd = f'ffmpeg -i files/render1.ogg -filter_complex "vibrato=f=15" files/render2.ogg'
						os.system(cmd)

					if msg in ["арты"]:
						album_kiss = vk_u.photos.get(owner_id=-201980948, album_id=277597858)'''

					if "арт+" in event.obj.text.lower():
						if str(user) in admin_from:
							if (len(te2xt) == 2):
								art_c = msg.split(' ', 2)

								if art_c[1] == 'поцеловать':
									iendd = len(attachment[0]['photo']['sizes'])
									photo = attachment[0]['photo']['sizes'][int(iendd - 1)]['url']
									filename = "files/" + os.path.basename(photo).split('?')[0]
									r = requests.get(photo)
									with open(filename, 'wb') as f:
										f.write(r.content)
									
									upload = VkUpload(vk_session_u)
									ph = [filename]
									photo_list = upload.photo(photos=ph, album_id=277597858, group_id=201980948)
									sender(id, "Готово<br>Айди: " + str(photo_list[0]["id"]))
									'''
									owner_id = photo_list[0]["owner_id"]
									id_own = photo_list[0]["id"]
									attachment ='photo{}_{}'.format(owner_id,id_own)
									send(id, '', attachment)'''

								if art_c[1] == 'обнять':
									iendd = len(attachment[0]['photo']['sizes'])
									photo = attachment[0]['photo']['sizes'][int(iendd - 1)]['url']
									filename = "files/" + os.path.basename(photo).split('?')[0]
									r = requests.get(photo)
									with open(filename, 'wb') as f:
										f.write(r.content)
									
									upload = VkUpload(vk_session_u)
									ph = [filename]
									photo_list = upload.photo(photos=ph, album_id=277598460, group_id=201980948)
									sender(id, "Готово<br>Айди: " + str(photo_list[0]["id"]))
								
								if art_c[1] == 'сжечь':
									iendd = len(attachment[0]['photo']['sizes'])
									photo = attachment[0]['photo']['sizes'][int(iendd - 1)]['url']
									filename = "files/" + os.path.basename(photo).split('?')[0]
									r = requests.get(photo)
									with open(filename, 'wb') as f:
										f.write(r.content)
									
									upload = VkUpload(vk_session_u)
									ph = [filename]
									photo_list = upload.photo(photos=ph, album_id=277598139, group_id=201980948)
									sender(id, "Готово<br>Айди: " + str(photo_list[0]["id"]))

								if art_c[1] == 'отшлëпать':
									iendd = len(attachment[0]['photo']['sizes'])
									photo = attachment[0]['photo']['sizes'][int(iendd - 1)]['url']
									filename = "files/" + os.path.basename(photo).split('?')[0]
									r = requests.get(photo)
									with open(filename, 'wb') as f:
										f.write(r.content)
									
									upload = VkUpload(vk_session_u)
									ph = [filename]
									photo_list = upload.photo(photos=ph, album_id=277598460, group_id=201980948)
									sender(id, "Готово<br>Айди: " + str(photo_list[0]["id"]))

					if "погода" in event.obj.text.lower():
						if (len(te2xt) == 1) or (len(te2xt) == 2):
							ecx = 0
							if (len(te2xt) == 1):
								try:
									getCountry = vk.users.get(user_ids=str(user), fields="city")

									city = getCountry[0]["city"]["title"]
									print(city)
								except Exception as e:
									if str(e) == "'city'":
										ecx = 1
										sender(id, "Вы не указали свой город<br>Повторите запрос<br>Погода + город")

							if (len(te2xt) == 2):
								city = msgl.split(' ', 2)[1]
							
							if ecx == 0:
								url = "http://api.openweathermap.org/data/2.5/weather"
								parameters = {
								'q': city,
								'appid': "778d98cf94b6609bec655b872f24b907",
								'units':'metric',
								'lang' : 'ru'
								}

								res = requests.get(url, params = parameters)
								data = res.json()

								print(data)

								if int(data['main']['temp']) <= 0:
									t = '❄'
								elif int(data['main']['temp']) > 0 < 15:
									t = '☁'
								elif int(data['main']['temp']) >= 20:
									t = '☀'
								elif int(data['main']['temp']) >= 15 < 20:
									t = '🌥'

								sender(id, "Погода в " + city.capitalize() + "<br>Погода: " + t + "<br>" + str(data['weather'][0]['description']).capitalize() + "<br>Температура: " + str(data['main']['temp']) + "<br>Скорость ветра: " + str(data['wind']['speed']))

			except Exception as e:
				print(e)
				sender(id, 'На сервере возникла ошибка!<br>Текст ошибки:<br>' + str(e))

#keyboard_1 = VkKeyboard(**settings) #Настройки кнопки
#keyboard_1.add_callback_button(label='Номер 1', color=VkKeyboardColor.POSITIVE, payload={"type": "show_snackbar", "text": "Саня гей"}) #Кнопка
#keyboard_1.add_line() #Перенос строки
#send_key(id, 'член', keyboard_1.get_keyboard()) 
