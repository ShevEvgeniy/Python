# Напишите Бота, удаляющего из текста все слова, содержащие "абв". (Ввод от пользователя)

# txt = input("Введите текст через пробел:\n")
# print(f"Исходный текст: {txt}")
# find_txt = "абв"
# list1 = [i for i in txt.split() if find_txt not in i]
# print(f'Результат: {" ".join(list1)}')

from telegram import Bot, Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

bot = Bot(token='5868864749:AAF_G_RbB9DJsLNrUGQrGZh2aFY_fWGjClU')
updater = Updater(token='5868864749:AAF_G_RbB9DJsLNrUGQrGZh2aFY_fWGjClU')
dispatcher = updater.dispatcher

def del_abv(update, context):
    text = update.message.text.split()
    list1 = []
    for i in text:
        if "абв" not in i:
            list1.append(i)
    context.bot.send_message(update.effective_chat.id, " ".join(list1))

def del_advV2(update, context):
    text = update.message.text.split()
    list1 = []
    for i in text:
        if "абв" not in i:
            list1.append(i)
    context.bot.send_message(update.effective_chat.id, " ".join(list1[1:]))

    hand_com = CommandHandler('start', del_advV2)
    del_handler = MessageHandler(Filters.text, del_abv)
    dispatcher.add_handler(del_handler)
    dispatcher.add_handler(hand_com)

    updater.start_polling()
    updater.idle()