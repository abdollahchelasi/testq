import telebot
from keep_alive import keep_alive
import os
keep_alive()


# TOKEN = '6921639698:AAGgvNBVhXqAaXQxpyAA6NL03zoIcG8yxY4'

bot = telebot.TeleBot(token = os.environ.get("token"))

# تعریف دستور /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "سلام من عبدالله چلاسی هستم")

# تعریف دستور /help
@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, "راهنما: این ربات پیام‌های شما را در چت تلگرام نمایش می‌دهد.")

# پاسخ به پیام‌های متنی
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

# اجرای ربات
bot.polling()
