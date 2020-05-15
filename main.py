import telebot as tb
from pyes import consts

bot = tb.TeleBot(consts.token)


def is_coded(c):
    if c in consts.morze:
        return True
    else:
        return False


def trans(text):
    res = ''
    for c in text:
        if c == ' ':
            res += '    '
        if is_coded(c):
            res += consts.morze[c] + '   '
        else:
            res += c
    return res

# keyboard cofig
select_mode_mrkp = tb.types.ReplyKeyboardMarkup(resize_keyboard=True)
item1 = tb.types.KeyboardButton('Морзе -> текст')
item2 = tb.types.KeyboardButton('текст -> Морзе')
select_mode_mrkp.row(item1, item2)
# select_mode_mrkp.row(item2)


# @bot.message_handler(commands=['change_mode'])
# def change_mode():


@bot.message_handler(commands=['help'])
def send_help(message):
    bot.send_message(message.from_user.id,
                     """Пожалуйста выберете режим работы бота:
Режим [Морзе -> текст] Разшифроывает текст, написаный азбукой Морзе.
Режим [текст -> Морзе] Зашифроывает текст, с помощью азбуки Морзе.
Вы также можете использовать команду /change_mode для изменения режима работы
""")


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message,
                 """Этот бот - удобный инструмент для работы с азбукой Морзе.
Существует два режима работы:
Режим [Морзе -> текст] Разшифроывает текст, написаный азбукой Морзе.
Режим [текст -> Морзе] Зашифроывает текст, с помощью азбуки Морзе.
Используйте команду /help, чтобы узнать больше""")
    # select_mode_mrkp = tb.types.ReplyKeyboardRemove(selective=False)
    bot.send_message(message.from_user.id, "test", reply_markup=select_mode_mrkp)


@bot.message_handler(content_types=['text'])
def select_mode(message):
    if message.text == 'Морзе -> текст':
        bot.send_message(message.from_user.id, "Теперь бот будет превращать морзянку в текст")
        consts.mode = False
    elif message.text == 'текст -> Морзе':
        bot.send_message(message.from_user.id, "Теперь бот будет превращать текст в морзянку."
                                               "Пожалуйста, делайте между тире и точками один пробел, между "
                                               "зашифроваными буквами три пробела, а между словами семь") 
                                               
        consts.mode = True
    else: echo_ans(message)


@bot.message_handler(func=lambda message: True, content_types=['text'])
def echo_ans(message):
    if consts.mode:
        ans = trans(message.text)
    # else:
    # ans = un
    bot.send_message(message.from_user.id, ans)


bot.polling()
# todo помінять словарь на кортеж, реалізувати поіск символа в кортежі, реалізувати обратний перевод, закончить тим самим проект
