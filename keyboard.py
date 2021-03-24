from telebot import types




startmenu = types.ReplyKeyboardMarkup(True, True)
startmenu.row('Меню', 'О нас')
startmenu.row('Доставка', 'Помощь')


infomenu = types.ReplyKeyboardMarkup(True, True)
infomenu.row('В начало', 'Помощь')


back = types.ReplyKeyboardMarkup(True, True)
back.row('В начало', 'Меню')



susimenu = types.InlineKeyboardMarkup(row_width=4)
susimenu.add(
	types.InlineKeyboardButton(text='Пицца', callback_data='pizza'),
	types.InlineKeyboardButton(text='Роллы', callback_data='roll'),
	types.InlineKeyboardButton(text='Суши', callback_data='sushi'),
	types.InlineKeyboardButton(text='Сеты', callback_data='sets')

)




roll_cheese = types.InlineKeyboardMarkup()
roll_cheese.add(
	types.InlineKeyboardButton(
	text='Заказать',
	url='https://realroll.com.ua/ru/menu/goryachiy-syrnyy-roll/',
	callback_data='roll_cheese'
	),
	types.InlineKeyboardButton(
	text='Назад',
	callback_data='menuback'
	)
)




sushi_gunkan = types.InlineKeyboardMarkup()
sushi_gunkan.add(
	types.InlineKeyboardButton(
	text='Заказать',
	url='https://realroll.com.ua/ru/menu/gunkan-s-tuntsom/',
	callback_data='sushi_gunkan'
	),
	types.InlineKeyboardButton(
	text='Назад',
	callback_data='menuback'
	)
)



set_dragon = types.InlineKeyboardMarkup()
set_dragon.add(
	types.InlineKeyboardButton(
	text='Заказать',
	url='https://realroll.com.ua/ru/menu/set-real-dragon/',
	callback_data='set_dragon'
	),
	types.InlineKeyboardButton(
	text='Назад',
	callback_data='menuback'
	)
)


pizza_close = types.InlineKeyboardMarkup()
pizza_close.add(
	types.InlineKeyboardButton(
	text='Заказать',
	url='https://realroll.com.ua/ru/menu/kalcone-zakrytaja-pizza/',
	callback_data='pizza_close'
	),
	types.InlineKeyboardButton(
	text='Назад',
	callback_data='menuback'
	)
)


