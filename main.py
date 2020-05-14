import telebot as tb
from pyes import consts

bot = tb.TeleBot(consts.token)

def is_coded(c):
    if 'A' <= c <= 'Z' or 'z' >= c >= 'a' or '0' <= c <= '9':
        return True
    else:
        return False

def trans(text):
    res = ''
    for c in text:
        if c == ' ':
            res += '       '
        if is_coded(c):
            res += consts.morze[c] + '   '
        else:
            res += c
    return res


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message,
                 "Этот бот преобразует ваш текст в шифр азбукой Морзе. \nДля того, что бы зашифровать ваше сообщение, просто введите нужный текст.")


@bot.message_handler(func=lambda message: True, content_types=['text'])
def echo_ans(message):
    ans = trans(message.text)
    bot.send_message(message.from_user.id, ans)


bot.polling()
