from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, filters

# Kalkulyator funksiyasi
def calculate(update: Update, context):
    try:
        # Xabarni bo'laklarga ajratish
        message = update.message.text.split()
        num1 = float(message[0])
        operator = message[1]
        num2 = float(message[2])

        # Hisoblash
        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            if num2 == 0:
                update.message.reply_text("Nolga bo'lish mumkin emas!")
                return
            result = num1 / num2
        else:
            update.message.reply_text("Noto'g'ri operator!")
            return

        # Natijani chiqarish
        update.message.reply_text(f"Natija: {result}")
    except (IndexError, ValueError):
        update.message.reply_text("Format: <son> <operator> <son> (masalan: 5 + 3)")

# /start komandasi
def start(update: Update, context):
    update.message.reply_text("Kalkulyator botiga xush kelibsiz!\nHisoblash uchun: <son> <operator> <son> yozing.")

if __name__ == '__main__':
    # Bot tokeningizni o'rnating
    TOKEN = '7927430842:AAF8_rd6lCfvYvsp1vwfA7f8QNQELLiWHco'

    # Updater va Dispatcher yaratamiz
    updater = Updater(token=TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    # Buyruqlar va xabarlarni qo'shish
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(filters.text & ~filters.command, calculate))

    # Botni ishga tushirish
    updater.start_polling()
    updater.idle()
