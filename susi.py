import telebot

from telebot import types

import keyboard as kb


TOKEN = '160648Ri7QDtyg'

bot = telebot.TeleBot(TOKEN)


PHOTOMENU = 'AgACAgIAAxkBAAIFNmBbLjXDFiV9gnqPQMSNht9WgPuCAALArzEbjO3YSrQ4K1F0XaVullCMoi4AAwEAAwIAA3kAA648AAIeBA'

PHOTOROLL = 'AgACAgIAAxkBAAN8YEC7MVLlZKS0m4-xdhGplWmiVsYAAtuwMRttVwhKVuYzZ0u9ae9DcDSbLgADAQADAgADeAADsBAEAAEeBA'

PHOTOSUSI = 'AgACAgIAAxkBAAOLYEDCrhZAGbuinP2WvYLM86KMYc8AAuawMRttVwhKJH5-Rz6v3weFi9qWLgADAQADAgADeAADClUHAAEeBA'

PHOTOSETS = 'AgACAgIAAxkBAAIB6mBA5MP_Q78q9igJZGwFhXDfx2g5AAImsTEbbVcISmI-DsV0QwFDRt0Smy4AAwEAAwIAA3gAA1ULAwABHgQ'

PHOTOPIZZA = 'AgACAgIAAxkBAAIB7WBA6U4_cQ9_YTFi4HL_EvJIHiTFAAIwsTEbbVcISusMZoLtIh6sT1Uumy4AAwEAAwIAA3gAA1rAAwABHgQ'

@bot.message_handler(commands=['start'])
def startmenu(message):
	bot.send_message(message.chat.id, 'Приветствуем вас.\nЭтот бот поможет вам сделать заказ в нашем ресторане', reply_markup=kb.startmenu)




@bot.message_handler(commands=['info'])
def infomenu(message):
	bot.send_message(message.chat.id, 'При вознекновении проблем с заказом нажмите кнопку "Помощь"\nДля вопросов связанных с ботом @whiteyod', reply_markup=kb.infomenu)




@bot.message_handler(content_types=['text'])
def main(message):
	if message.text == 'В начало':
		global mainmenu
		mainmenu = 'mainmenu'
		startmenu(message)
	elif message.text == 'Меню':
		bot.send_photo(message.chat.id, PHOTOMENU, caption='Это пробная версия меню, в нём показаны лишь некоторые наши блюда:', reply_markup=kb.susimenu)
	elif message.text == 'О нас':
		bot.send_message(message.chat.id, 'Сеть ресторанов "Real Roll" уже более шести лет радует наших клиентов вкуснейшими блюдами по всей стране', reply_markup=kb.back)
	elif message.text == 'Помощь':
		bot.send_message(message.chat.id, 'Если у вас не получется сделать заказ или не работают ссылки - свяжитесь с нашим менеджером @pixel_photoshop\nОн с радостью ответит на все ваши вопросы и поможет совершить заказ.', reply_markup=kb.back)
	elif message.text == 'Доставка':
		bot.send_message(message.chat.id, 'Доставка осуществялется в пределах Винницы, цена зависит от расстояния и начинается от 100р.\nТочную стоимость вам сообщит оператор при обработке вашего заказа.', reply_markup=kb.back)




@bot.callback_query_handler(func=lambda c: True)
def inline(c):
	if c.data == 'roll':
		bot.send_message(c.message.chat.id, 'Роллы', reply_markup=kb.back)
		bot.send_photo(
			c.message.chat.id,
			PHOTOROLL,
			caption='Горячий сырный ролл XL\nСыр чеддер, крем сыр, лист салата, сухари Панко, нори, рис\n105 грн',
			reply_markup=kb.roll_cheese
			)

	elif c.data == 'sushi':
		bot.send_message(c.message.chat.id, 'Суши', reply_markup=kb.back)
		bot.send_photo(
			c.message.chat.id,
			PHOTOSUSI,
			caption='Гункан с тунцом\nТунец, икра тобико, соус спайси, нори, рис\n34 грн',
			reply_markup=kb.sushi_gunkan
			)

	elif c.data == 'sets':
		bot.send_message(c.message.chat.id, 'Сеты', reply_markup=kb.back)
		bot.send_photo(
			c.message.chat.id,
			PHOTOSETS,
			caption='Сет Real Dragon\nБронзовый дракон, красный дракон, тигровый дракон, зелёный дракон\n725 грн',
			reply_markup=kb.set_dragon
			)

	elif c.data == 'pizza':
		bot.send_message(c.message.chat.id, 'Пицца', reply_markup=kb.back)
		bot.send_photo(
			c.message.chat.id,
			PHOTOPIZZA,
			caption='Кальцоне — закрытая пицца\nСыр Моцарелла, балык, грибы  шампиньйоны, сыр Дор Блю, помидоры\n141 грн\n\n*примечание: овощи, изображенные на фото, являются способом сервировки и в заказ не входят',
			reply_markup=kb.pizza_close
			)


	elif c.data == 'menuback':
		 bot.send_photo(c.message.chat.id, PHOTOMENU, caption='Это пробная версия меню, в нём показаны лишь некоторые наши блюда:', reply_markup=kb.susimenu)






bot.polling()
