from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Welcome to Diyorbek\'s calculator bot!\nPlease enter the first number:')

# Foydalanuvchi birinchi raqamni kiritgandan keyin uni saqlaymiz
async def handle_number(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    text = update.message.text

    if 'step' not in context.user_data:
        context.user_data['step'] = 'num1'
    
    if context.user_data['step'] == 'num1':
        try:
            context.user_data['num1'] = float(text)
            context.user_data['step'] = 'operator'
            await update.message.reply_text('Now enter the operator (+, -, *, /):')
        except ValueError:
            await update.message.reply_text('Please enter a valid number.')
    
    elif context.user_data['step'] == 'operator':
        if text in ['+', '-', '*', '/']:
            context.user_data['operator'] = text
            context.user_data['step'] = 'num2'
            await update.message.reply_text('Now enter the second number:')
        else:
            await update.message.reply_text('Invalid operator. Please enter one of (+, -, *, /).')
    
    elif context.user_data['step'] == 'num2':
        try:
            context.user_data['num2'] = float(text)
            await calculate(update, context)
            context.user_data.clear()  # Reset after calculation
        except ValueError:
            await update.message.reply_text('Please enter a valid number.')

async def calculate(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    num1 = context.user_data['num1']
    operator = context.user_data['operator']
    num2 = context.user_data['num2']

    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        if num2 != 0:
            result = num1 / num2
        else:
            await update.message.reply_text('Division by zero is not allowed.')
            return

    await update.message.reply_text(f'Result: {result}\nType /start to start a new calculation.')

if __name__ == '__main__':
    app = ApplicationBuilder().token('7927430842:AAF8_rd6lCfvYvsp1vwfA7f8QNQELLiWHco').build()

    # /start buyrug'ini boshqarish
    app.add_handler(CommandHandler("start", start))
    
    # Xabarlarni qabul qilish
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_number))

    print("Bot is running...")
    app.run_polling()
