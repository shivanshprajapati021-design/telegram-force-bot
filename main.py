from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

# ====== TERA BOT TOKEN YAHAN DAL ======
BOT_TOKEN = "YAHAN_APNA_BOT_TOKEN_DALO"

# ====== TERE DIYE HUE LINKS ======
CHANNEL_LINKS = [
    "https://t.me/+xrqm18hD1uVlYzZk",  # CHANNEL 1
    "https://t.me/+j88DIVGmn2E5NzU1",  # CHANNEL 2
    "https://t.me/+rtBe_3wyso85NzRl",  # CHANNEL 3
    "https://t.me/+_M8cMRaOYrlmZWE9",  # CHANNEL 4
    "https://t.me/+c8FeRA7XQNQ4ZTJl"   # CHANNEL 5
]
VERIFY_LINK = "https://t.me/+LqVblnrPGUgyMDZl"

# Key milne pe kya message dena hai
KEY_TEXT = """🔥 𝐖ᴇʟᴄᴏᴍᴇ To Free Panel!

✅ Verification Complete!

🔑 𝐘𝐨𝐮𝐫 𝐊𝐞𝐲: `FREE-PANEL-2025-XYZ`

📥 Download Panel: @freeallfriendbio

🔗 𝐇𝐨𝐰 𝐓𝐨 𝐆𝐞𝐭 𝐊𝐞𝐲 Video: Yaha video link daal dena
"""

WELCOME_PHOTO_URL = "https://i.ibb.co/..." # Yaha teri wali Vali Mod photo ka link daal de, ya maine jo banner banaya hai wo use kar le

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user.first_name
    keyboard = []
    
    for i, link in enumerate(CHANNEL_LINKS, 1):
        keyboard.append([InlineKeyboardButton(f"📢 CHANNEL {i} JOIN", url=link)])
    
    # Verify Button - Link pe bhejega
    keyboard.append([InlineKeyboardButton(f"✅ VERIFY - KEY LO", url=VERIFY_LINK)])
    
    # Neeche wale 2 button
    keyboard.append([
        InlineKeyboardButton("🔗 How To Get Key 📈", url=CHANNEL_LINKS[0]),
        InlineKeyboardButton("🔑 GET KEY 🔥", callback_data="getkey")
    ])

    markup = InlineKeyboardMarkup(keyboard)

    caption = f"""🔥 𝐖ᴇʟᴄᴏᴍᴇ {user}
🚫 𝐉ᴏɪɴ 𝐀ʟʟ 𝐂ʜᴀɴɴᴇʟꜱ 𝐓𝐨 𝐔ɴʟᴏᴄᴋ

👇 5 CHANNEL JOIN KARO 👇
Sab Join Karke Last Wala VERIFY Dabao Aur Key Le Lo!

🔗 𝐇ᴏᴡ 𝐓𝐨 𝐆ᴇᴛ 𝐊ᴇʏ 📈
"""

    # Photo ke saath bhejna
    try:
        await update.message.reply_photo(photo=WELCOME_PHOTO_URL, caption=caption, reply_markup=markup)
    except:
        # Agar photo link nahi hai to bina photo ke bhej dega
        await update.message.reply_text(caption, reply_markup=markup)

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    # Direct key de dega - kyunki private link ka force check nahi hota
    await query.message.reply_text(KEY_TEXT, parse_mode="Markdown")

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(button_handler))
print("Bot Ready - 5 Channel + Verify Mode")
app.run_polling()
