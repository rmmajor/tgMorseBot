import telebot as tb


select_mode_mrkp = tb.types.ReplyKeyboardMarkup(resize_keyboard=True)
select_mode_item1 = tb.types.KeyboardButton('Морзе -> текст')
select_mode_item2 = tb.types.KeyboardButton('текст -> Морзе')
select_mode_mrkp.row(select_mode_item1, select_mode_item2)


select_lang_mrkp = tb.types.InlineKeyboardMarkup()
select_lang_mrkp.row_width = 2
select_lang_mrkp.add(tb.types.InlineKeyboardButton("Русккий, украинский", callback_data="rus"),
           tb.types.InlineKeyboardButton("English", callback_data="eng"))
