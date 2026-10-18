import os, threading
from flask import Flask
import telebot

BOT_TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(BOT_TOKEN)

C1="https://t.me/+jiU-XAOC02tjMjc1"
C2="https://t.me/+j88DIVGmn2E5NzU1"
C3="https://t.me/+XLLKweUtvEpvYzE1"
C4="https://t.me/+_M8cMRaOYr1mZWE9"
C5="https://t.me/+Om4m__Xns9BiMzI1"
VERIFY="https://t.me/+LqVb1nrPGUgyMDZ"

app = Flask(__name__)

@bot.message_handler(commands=['start'])
def start(m):
    bot.reply_to(m, "Bot Live hai ✅")

@app.route('/')
def home():
    return "Bot is Live"

def run_bot():
    bot.infinity_polling()

if __name__ == "__main__":
    threading.Thread(target=run_bot).start()
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
