import os
import threading
from flask import Flask
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

BOT_TOKEN = os.environ.get("BOT_TOKEN")

CHANNEL_1 = "https://t.me/+xrqm18hD1uVlYzZk"
CHANNEL_2 = "https://t.me/+j88DIVGmn2E5NzU1"
CHANNEL_3 = "https://t.me/+rtBe_3wyso85NzRl"
CHANNEL_4 = "https://t.me/+_M8cMRaOYrlmZWE9"
CHANNEL_5 = "https://t.me/+c8FeRA7XQNQ4ZTJl"
VERIFY_CHANNEL = "https://t.me/+LqVblnrPGUgyMDZl"

WELCOME_PHOTO = "https://i.ibb.co/rfZYbRS3/abc.jpg"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user.first_name
    keyboard = [
        [InlineKeyboardButton("CHANNEL 1", url=CHANNEL_1), InlineKeyboardButton("CHANNEL 2", url=CHANNEL_2)],
        [InlineKeyboardButton("CHANNEL 3", url=CHANNEL_3), InlineKeyboardButton("CHANNEL 4", url=CHANNEL_4)],
        [InlineKeyboardButton("CHANNEL 5", url=CHANNEL_5)],
        [InlineKeyboardButton("VERIFY ✅", url=VERIFY_CHANNEL)]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    caption = f"🔥 WELCOME {user}\n🚫 JOIN ALL CHANNELS TO UNLOCK"
    try:
        await update.message.reply_photo(photo=WELCOME_PHOTO, caption=caption, reply_markup=reply_markup)
    except:
        await update.message.reply_text(caption, reply_markup=reply_markup)

# Flask app for Render port binding
app_flask = Flask(__name__)
@app_flask.route('/')
def home():
    return "Bot is Running!"

def run_bot():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    print("Bot Running - 5+1")
    app.run_polling()

if __name__ == "__main__":
    threading.Thread(target=run_bot).start()
    port = int(os.environ.get("PORT", 10000))
    app_flask.run(host='0.0.0.0', port=port)
