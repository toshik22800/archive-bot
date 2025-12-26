import telebot
import os
from dotenv import load_dotenv

load_dotenv()
bot = telebot.TeleBot(os.getenv('BOT_TOKEN'))

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "✅ Бот работает! Добро пожаловать!\nИспользуйте /help")

@bot.message_handler(commands=['help'])
def send_help(message):
    help_text = """
📋 **Доступные команды:**
/start - Начать
/help - Помощь
/contacts - Контакты архива
/schedule - График работы
/request - Подать запрос
    """
    bot.reply_to(message, help_text)

@bot.message_handler(commands=['contacts'])
def send_contacts(message):
    bot.reply_to(message, "📞 Контакты:\nТел: +7(3462)111-111\nEmail: archive@surgut.ru")

@bot.message_handler(commands=['schedule'])
def send_schedule(message):
    bot.reply_to(message, "🕒 График:\nПн-Чт: 9:00-18:00\nПт: 9:00-17:00")

print("Бот запущен... Нажмите Ctrl+C для остановки")
bot.polling()
