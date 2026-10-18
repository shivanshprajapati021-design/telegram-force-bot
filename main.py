import os, threading
from flask import Flask
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

BOT_TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(BOT_TOKEN)

# --- TERE LINKS ---
C1 = "https://t.me/+jiU-XA0CO2tjMjc1"
C2 = "https://t.me/+j88DIVGmn2E5NzU1"
C3 = "https://t.me/+XLLKweUtvEpjYzE1"
C4 = "https://t.me/+_M8cMRaOYrlmZWE9"
C5 = "https://t.me/+Om4m__Xns9BiMzI1"
VERIFY_LINK = "https://t.me/+LqVblnrPGUgyMDZl"

app = Flask(__name__)

@bot.message_handler(commands=['start'])
def start(m):
    markup = InlineKeyboardMarkup(row_width=1)
    markup.add(
        InlineKeyboardButton("📢 CHANNEL 1 JOIN", url=C1),
        InlineKeyboardButton("📢 CHANNEL 2 JOIN", url=C2),
        InlineKeyboardButton("📢 CHANNEL 3 JOIN", url=C3),
        InlineKeyboardButton("📢 CHANNEL 4 JOIN", url=C4),
        InlineKeyboardButton("📢 CHANNEL 5 JOIN", url=C5),
        InlineKeyboardButton("✅ VERIFY - KEY LO", url=VERIFY_LINK)
    )
    bot.send_message(m.chat.id, 
        "🔥 **FREE KEY LENE KE LIYE** 🔥\n\n"
        "👇 **5 CHANNEL JOIN KARO** 👇\n\n"
        "Sab Join Karke Last Wala VERIFY Dabao Aur Key Le Lo!",
        reply_markup=markup)

@app.route('/')
def home():
    return "Bot Live Hai"

def run_bot():
    bot.infinity_polling()

if __name__ == "__main__":
    threading.Thread(target=run_bot).start()
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
