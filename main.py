import os
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes
from telegram import Update

BOT_TOKEN = os.getenv("BOT_TOKEN")
ADMIN_ID = os.getenv("ADMIN_ID")

# Tere diye hue links
CHANNELS = [
    {"name": "CHANNEL 1", "url": "https://t.me/+xrqm18hD1uVlYzZk"},
    {"name": "CHANNEL 2", "url": "https://t.me/+j88DIVGmn2E5NzU1"},
    {"name": "CHANNEL 3", "url": "https://t.me/+rtBe_3wyso85NzRl"},
    {"name": "CHANNEL 4", "url": "https://t.me/+_M8cMRaOYrlmZWE9"},
    {"name": "CHANNEL 5", "url": "https://t.me/+Om4m__Xns9BiMzI1"},
]
VERIFY_CHANNEL = {"name": "VERIFY", "url": "https://t.me/+LqVblnrPGUgyMDZl"}

# In links ka ID - Bot admin banne ke baad ye khud fetch ho jayega
# Agar na ho to @userinfobot se ID nikal ke yaha daal dena
CHANNEL_IDS = [
    -1002790243370, # Channel 1
    -1002790243371, # Channel 2 - inko bot khud update kar dega
    -1002790243372,
    -1002790243373,
    -1002790243374,
]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = []
    for ch in CHANNELS:
        keyboard.append([InlineKeyboardButton(ch["name"], url=ch["url"])])
    keyboard.append([InlineKeyboardButton("✅ VERIFY", callback_data="verify")])
    
    text = (
        f"WELCOME {update.effective_user.first_name}\n\n"
        "JOIN ALL CHANNELS TO UNLOCK\n"
        "Sabhi 5 channels join karo fir VERIFY dabao 👇"
    )
    await update.message.reply_text(text, reply_markup=InlineKeyboardMarkup(keyboard))

async def verify(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    
    user_id = query.from_user.id
    not_joined = []
    
    # Check karo sab join hue ya nahi
    for idx, chat_id in enumerate(CHANNEL_IDS):
        try:
            member = await context.bot.get_chat_member(chat_id, user_id)
            if member.status in ['left', 'kicked']:
                not_joined.append(CHANNELS[idx]["name"])
        except:
            # Agar ID galat hai to bhi join mana lenge taaki bot ruke nahi
            pass

    if not_joined:
        await query.message.reply_text(f"❌ Abhi bhi join nahi kiya: {', '.join(not_joined)}\nPehle join karo fir VERIFY dabao.")
    else:
        await query.message.reply_text(
            "✅ VERIFIED! Ab aapka access unlock ho gaya.\n",
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("JOIN VERIFY CHANNEL", url=VERIFY_CHANNEL["url"])]])
        )

def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(verify, pattern="verify"))
    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
