import os, telebot
from telebot import types

BOT_TOKEN = os.getenv("8222032093:AAFDWw9kO3pPmHu318MwQ-wkkmtqPOQsJZk")
bot = telebot.TeleBot(BOT_TOKEN)

C1="https://t.me/+jiU-XA0CO2tjMjc1"
C2="https://t.me/+j88DIVGmn2E5NzU1"
C3="https://t.me/+XLLKweUtvEpvYzE1"
C4="https://t.me/+_M8cMRaOYrlmZWE9"
C5="https://t.me/+Om4m__Xns9BiMzI1"
VERIFY="https://t.me/+LqVblnrPGUgyMDZl"

@bot.message_handler(commands=['start'])
def start(m):
    kb=types.InlineKeyboardMarkup(row_width=2)
    kb.add(types.InlineKeyboardButton("CHANNEL 1",url=C1),types.InlineKeyboardButton("CHANNEL 2",url=C2))
    kb.add(types.InlineKeyboardButton("CHANNEL 3",url=C3),types.InlineKeyboardButton("CHANNEL 4",url=C4))
    kb.add(types.InlineKeyboardButton("CHANNEL 5",url=C5))
    kb.add(types.InlineKeyboardButton("VERIFY ✅",url=VERIFY))
    bot.send_message(m.chat.id,f"Welcome {m.from_user.first_name}\n\nJoin all 5 then click VERIFY",reply_markup=kb)

bot.infinity_polling()
