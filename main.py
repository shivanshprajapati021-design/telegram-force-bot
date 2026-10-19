import os
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

BOT_TOKEN = os.environ.get("BOT_TOKEN")

CHANNELS = [
    {"name": "CHANNEL 1", "url": "https://t.me/+xrqm18hD1uVlYzZk"},
    {"name": "CHANNEL 2", "url": "https://t.me/+j88DIVGmn2E5NzU1"},
    {"name": "CHANNEL 3", "url": "https://t.me/+rtBe_3wyso85NzRl"},
    {"name": "CHANNEL 4", "url": "https://t.me/+_M8cMRaOYrlmZWE9"},
    {"name": "CHANNEL 5", "url": "https://t.me/+Om4m__Xns9BiMzI1"},
]
VERIFY_URL = "https://t.me/+LqVblnrPGUgyMDZl"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("CHANNEL 1", url=CHANNELS[0]["url"]), InlineKeyboardButton("CHANNEL 2", url=CHANNELS[1]["url"])],
        [InlineKeyboardButton("CHANNEL 3", url=CHANNELS[2]["url"]), InlineKeyboardButton("CHANNEL 4", url=CHANNELS[3]["url"])],
        [InlineKeyboardButton("CHANNEL 5", url=CHANNELS[4]["url"])],
        [InlineKeyboardButton("VERIFY ✅", url=VERIFY_URL)]
    ]
    
    caption = (
        f"🔥 WELCOME {update.effective_user.first_name}\n"
        "🚫 JOIN ALL CHANNELS TO UNLOCK\n\n"
        "🔗 How To Get Key 📈\n"
        "🔑 Get Key 🔥"
    )

    # banner.jpg bhejega
    try:
        with open("banner.jpg", "rb") as photo:
            await update.message.reply_photo(
                photo=photo,
                caption=caption,
                reply_markup=InlineKeyboardMarkup(keyboard)
            )
    except:
        # Agar photo nahi mila to sirf text bhejega
        await update.message.reply_text(
            caption,
            reply_markup=InlineKeyboardMarkup(keyboard)
        )

async def verify(update: Update, context: ContextTypes.DEFAULT_TYPE):
    q = update.callback_query
    await q.answer()
    await q.message.reply_text("✅ Verify ho gaya! Key ke liye VERIFY channel join karo.")

def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(verify, pattern="verify"))
    print("Bot Started")
    app.run_polling()

if __name__ == "__main__":
    main()
