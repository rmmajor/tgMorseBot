import telebot as tb
from pyes import consts
from pyes import translator as tr
from pyes import markups as mp

bot = tb.TeleBot(consts.token)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message,
                 """Этот бот - удобный инструмент для работы с азбукой Морзе.
Существует два режима работы:
Режим [Морзе -> текст] - разшифровывает текст, написаный азбукой Морзе.
Режим [текст -> Морзе] - рашифровывает текст, с помощью азбуки Морзе.""")
    bot.send_message(message.from_user.id, 'Пожалуйста, выберите режим работы', reply_markup=mp.select_mode_mrkp)


@bot.message_handler(content_types=['text'])
def select_mode(message):
    if message.text == 'Морзе -> текст':
        bot.send_message(message.from_user.id, "Теперь бот будет превращать морзянку в текст. "
                                               "Пожалуйста, делайте между тире и точками один пробел, между "
                                               "зашифроваными буквами три пробела, а между словами семь.\n"
                                               "Для вашего удобства, все символы будут выводиться в нижний регистр")
        bot.send_message(message.chat.id, "Выберите, пожалуйста, язык на который нужно переводить",
                         reply_markup=mp.select_lang_mrkp)
        consts.mode = 'untranslate'
    elif message.text == 'текст -> Морзе':
        bot.send_message(message.from_user.id, "Теперь бот будет превращать текст в морзянку.")
        consts.mode = 'translate'
    else:
        echo_ans(message)


@bot.message_handler(func=lambda message: True, content_types=['text'])
def echo_ans(message):
    if consts.mode == 'undefined':
        bot.send_message(message.from_user.id, 'Пожалуйста, выберите режим работы')
    elif consts.mode == 'translate':
        ans = tr.trans(message.text)
        bot.send_message(message.from_user.id, ans)
    else:
        ans = tr.untrans(message.text)
        bot.send_message(message.from_user.id, ans)


@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "rus":
        consts.lang = 1
        bot.answer_callback_query(call.id, "Введите код")
    elif call.data == "eng":
        consts.lang = 0
        bot.answer_callback_query(call.id, "Введите код")


bot.polling(none_stop=True, interval=0, timeout=0)
