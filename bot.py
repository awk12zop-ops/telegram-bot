import telebot

# ضع التوكن اللي يجيك من @BotFather هنا
TOKEN = "ضع_التوكن_هنا"
bot = telebot.TeleBot(TOKEN)

# هذا اسم قناتك (مثال: @mychannel)
CHANNEL = "@اسم_قناتك"

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "✅ البوت يعمل بنجاح!")

# نشر رسالة تلقائية للقناة
bot.send_message(CHANNEL, "🚀 تم تشغيل البوت بنجاح!")

bot.polling()
