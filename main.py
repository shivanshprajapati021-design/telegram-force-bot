import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

BOT_TOKEN = os.environ.get("BOT_TOKEN")

CHANNEL_1 = "https://t.me/+xrqm18hD1uVlYzZk"
CHANNEL_2 = "https://t.me/+j88DIVGmn2E5NzU1"
CHANNEL_3 = "https://t.me/+rtBe_3wyso85NzRl"
CHANNEL_4 = "https://t.me/+_M8cMRaOYrlmZWE9"
CHANNEL_5 = "https://t.me/+c8FeRA7XQNQ4ZTJl"
VERIFY_CHANNEL = "https://t.me/+LqVblnrPGUgyMDZl"

WELCOME_PHOTO = "https://i.ibb.co/rfZYbRS3/abc.jpg"  # Apna real link yahan daalna

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user.first_name
    keyboard = [
        [InlineKeyboardButton("CHANNEL 1", url=CHANNEL_1), InlineKeyboardButton("CHANNEL 2", url=CHANNEL_2)],
        [InlineKeyboardButton("CHANNEL 3", url=CHANNEL_3), InlineKeyboardButton("CHANNEL 4", url=CHANNEL_4)],
        [InlineKeyboardButton("CHANNEL 5", url=CHANNEL_5)],
        [InlineKeyboardButton("VERIFY ✅", url=VERIFY_CHANNEL)]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    caption = f"🔥 WELCOME {user}\n🚫 JOIN ALL CHANNELS TO UNLOCK\n\n🔗 How To Get Key 📈\n🔑 Get Key 🔥"
    
    try:
        await update.message.reply_photo(photo=WELCOME_PHOTO, caption=caption, reply_markup=reply_markup)
    except:
        # Agar photo link kharab hua to sirf text bhej dega, crash nahi hoga
        await update.message.reply_text(caption, reply_markup=reply_markup)

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))
print("Bot Running - 5+1")
app.run_polling()
