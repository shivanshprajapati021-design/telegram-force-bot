import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

BOT_TOKEN = os.environ.get("BOT_TOKEN")

CHANNEL_LINKS = [
    "https://t.me/+xrqm18hD1uVlYzZk",
    "https://t.me/+j88DIVGmn2E5NzU1",
    "https://t.me/+rtBe_3wyso85NzRl",
    "https://t.me/+_M8cMRaOYrlmZWE9",
    "https://t.me/+c8FeRA7XQNQ4ZTJl"
]
VERIFY_LINK = "https://t.me/+LqVblnrPGUgyMDZl"
WELCOME_PHOTO_URL = "https://i.ibb.co/YOUR-DIRECT-LINK.jpg"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = []
    for i, link in enumerate(CHANNEL_LINKS, 1):
        keyboard.append([InlineKeyboardButton(f"📢 CHANNEL {i} JOIN", url=link)])
    keyboard.append([InlineKeyboardButton("✅ VERIFY - KEY LO", url=VERIFY_LINK)])
    keyboard.append([InlineKeyboardButton("🔗 How To Get Key 📈", url=CHANNEL_LINKS[0])])
    markup = InlineKeyboardMarkup(keyboard)
    caption = "🔥 WELCOME\n🚫 JOIN ALL CHANNELS TO UNLOCK"
    await update.message.reply_photo(photo=WELCOME_PHOTO_URL, caption=caption, reply_markup=markup)

if not BOT_TOKEN:
    print("ERROR: BOT_TOKEN not found in Environment Variables!")
else:
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    print("Bot Starting...")
    app.run_polling()
