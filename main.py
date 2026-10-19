import os
import threading
from flask import Flask
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler

BOT_TOKEN = os.environ.get("BOT_TOKEN")
WELCOME_PHOTO = "https://i.ibb.co/rF2Y3Rs3/image-20261019-114127.webp"

CHANNELS = [
    {"name": "CHANNEL 1", "url": "https://t.me/+xrqm18hD1uVlYzZk"},
    {"name": "CHANNEL 2", "url": "https://t.me/+j88DIVGmn2E5NzU1"},
    {"name": "CHANNEL 3", "url": "https://t.me/+rtBe_3wyso85NzRl"},
    {"name": "CHANNEL 4", "url": "https://t.me/+_M8cMRaOYrlmZWE9"},
    {"name": "CHANNEL 5", "url": "https://t.me/+Om4m__Xns9BiMzI1"},
]
VERIFY_URL = "https://t.me/+LqVblnrPGUgyMDZl"

flask_app = Flask(__name__)

@flask_app.route('/')
def home():
    return "Bot is Running!"

async def start(update: Update, context):
    keyboard = [
        [InlineKeyboardButton("CHANNEL 1", url=CHANNELS[0]["url"]), InlineKeyboardButton("CHANNEL 2", url=CHANNELS[1]["url"])],
        [InlineKeyboardButton("CHANNEL 3", url=CHANNELS[2]["url"]), InlineKeyboardButton("CHANNEL 4", url=CHANNELS[3]["url"])],
        [InlineKeyboardButton("CHANNEL 5", url=CHANNELS[4]["url"])],
        [InlineKeyboardButton("VERIFY ✅", url=VERIFY_URL)]
    ]
    caption = f"🔥 WELCOME {update.effective_user.first_name}\n🚫 JOIN ALL CHANNELS TO UNLOCK\n\n🔗 How To Get Key 📈\n🔑 Get Key 🔥"
    
    await update.message.reply_photo(photo=WELCOME_PHOTO, caption=caption, reply_markup=InlineKeyboardMarkup(keyboard))

def run_bot():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    print("Bot Started")
    app.run_polling()

if __name__ == "__main__":
    threading.Thread(target=run_bot).start()
    port = int(os.environ.get("PORT", 10000))
    flask_app.run(host='0.0.0.0', port=port)
