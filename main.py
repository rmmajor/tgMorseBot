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


select_mode_mrkp = tb.types.ReplyKeyboardMarkup(resize_keyboard=True)
item1 = tb.types.KeyboardButton('Морзе -> текст')
item2 = tb.types.KeyboardButton('текст -> Морзе')
select_mode_mrkp.row(item1)
select_mode_mrkp.row(item2)


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


@bot.message_handler(func=lambda message: True, content_types=['text'])
def echo_ans(message):
    ans = trans(message.text)
    bot.send_message(message.from_user.id, ans)


bot.polling()
