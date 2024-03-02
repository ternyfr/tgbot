# импортируем библиотеку telebot для телеги
import telebot

# записываем токен нашего бота в отдельную переменную
API_TOKEN = "7018646260:AAGDhFB0XJPGissTN0H5rL-jTosEzJZOKXo"

# создаем нового бота и прописываем ему токен
bot = telebot.TeleBot(API_TOKEN)

# создаем переменную, в которую кладем фотку, указываем путь до фотки
photo = open('./img/CAPIBARA.jpg', 'rb')
ph1 = open('./img/kirimi.jpg', 'rb')
ph2 = open('./img/kkrimi.jpg', 'rb')

# рецепт прописла в отдельную переменную, чтобы проще было читать код
# borch = "Для бульона: 1½–2 л воды; \n  400–500 г свинины или говядины на кости. \nДля зажарки: 2 небольшие свёклы;  \n1 средняя морковь;    3 средние луковицы;    4–5 столовых ложек растительного масла;    щепотка лимонной кислоты, немного столового уксуса или ½ лимона; \n2 столовые ложки томатной пасты.Для борща:    300 г свежей белокочанной капусты; \n4 средние картофелины;    соль — по вкусу;    1–2 сушёных лавровых листа;    зелень — по вкусу;    1 зубчик чеснока — опционально;    щепотка молотой гвоздики — опционально;    щепотка молотого чёрного перца — опционально."
rasp = "ЧЕТВЕРГ:\n1. расея маи гарезонты\n2. музыкальная пауза\n3. исторический расстрел\n4. шедеврогеография\n5. C21H23NO5 \n6. математик\n7. amerika\n8. ЧЕРТИЛА"
rec = "два пакетика травы, семьдесят пять ампул мескалина, 5 пакетиков диэтиламида лизергиновой кислоты или ЛСД, солонка, наполовину наполненная кокаином, и целое море разноцветных амфетаминов, барбитуратов и транквилизаторов, а так же литр текилы, литр рома, ящик «Бадвайзера», пинта чистого эфира, и 12 пузырьков амилнитрита"
dela = "— как дела?\n— нормал\n— ну, пон\n— не бери меня на понт\n— ку, кд? Чд?\n— ну, ок\n— всё, бб, давай\n— ну, спок\n— йоу, спс, бро\n— нзч, пнх, ты чё за чел?\n— хз ваще, хз ваще"

# слушатель сообщений
@bot.message_handler(commands=["start"])
# функция с кнопками
def start(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = telebot.types.InlineKeyboardButton(text = "привет")
    button2 = telebot.types.InlineKeyboardButton(text = "рецепт")
    button3 = telebot.types.InlineKeyboardButton(text = "худшее расписание")
    button4 = telebot.types.InlineKeyboardButton(text = "как дела")

    markup.add(button1, button2, button3, button4)
    bot.send_message(message.chat.id, "привет выбери команду", reply_markup = markup)

#  прослушиваем входящие сообщения типа Текст
@bot.message_handler(content_types=['text'])
# будет срабатывать функция при получении сообщения
def get_text_message(message):
    # создаем отдельную переменную и кладем туда id пользователя, с которым общаемся
    chat_id = message.from_user.id
    # Если текст сообщения равен одному из них, то срабатывает код
    if message.text == "привет":
        bot.send_message(chat_id, f"привет, {message.from_user.first_name}")
    elif message.text == "/start":
        bot.send_message(chat_id, 'Чего желаешь, брат?')
    elif message.text == "картинка":
        bot.send_photo(chat_id, photo)
    elif message.text == "худшее расписание":
        bot.send_message(chat_id, rasp)
        bot.send_photo(chat_id, ph1)
    elif message.text == "как дела":
        bot.send_message(chat_id, dela)
        bot.send_photo(chat_id, ph2)
    elif message.text == "рецепт":
        # говорим боту отправить сообщение человеку с таким то id и указываем текст
        bot.send_message(chat_id, rec)
        # отправляем фотку
        bot.send_photo(chat_id, photo)

# пишем, чтобы программа не завершалась сразу
bot.polling(none_stop=True, interval=0)