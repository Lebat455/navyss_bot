import os
from dotenv import load_dotenv
import telebot

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    welcome_msg = (
        "🚨 NEW QUIZ ALERT! 🚨\n\n"
        "🎉 Ready Na Ba Kayo?\n"
        "📢 Time to challenge your brain and earn while having fun!\n"
        "🎯 Just answer, earn, and enjoy the thrill!\n\n"
        "📲 Type /quiz to begin the game!"
    )
    bot.reply_to(message, welcome_msg)

@bot.message_handler(commands=['quiz'])
def quiz_menu(message):
    quiz_msg = (
        "📚 Piliin ang iyong subject o hamon:\n"
        "📖 /Literature\n🔬 /Science\n🔭 /Physics\n🏛️ /History\n"
        "🌍 /Geography\n🔤 /Jumbleword\n🧩 /Riddle"
    )
    bot.send_message(message.chat.id, quiz_msg)

@bot.message_handler(commands=['balance'])
def check_balance(message):
    bot.reply_to(message, "💰 Your current balance is: ₱0.0000")

if __name__ == "__main__":
    print("✅ Navyss Bot is now running...")
    bot.polling()
