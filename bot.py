import logging
from flask import Flask
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import Application, CommandHandler, CallbackContext, MessageHandler, filters

# Replace 'YOUR_API_TOKEN' with your actual API token from BotFather
API_TOKEN = '7226265761:AAFT3jZ2a6sGRHZekSC3g5uBp5GZHX6a8UU'

# Initialize logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Initialize Flask app
app = Flask(__name__)
application = Application.builder().token(API_TOKEN).build()

async def start(update: Update, context: CallbackContext) -> None:
    # Create a button that launches the React.js web app
    web_app_url = 'https://react-bot-tlgrm.vercel.app/'
    keyboard = [
        [InlineKeyboardButton("Open Game UI", web_app=WebAppInfo(url=web_app_url))]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text('Click the button below to open the game UI:', reply_markup=reply_markup)

# Add handler to process /start command
application.add_handler(CommandHandler("start", start))

# Use Polling instead of Webhook
def run_polling():
    application.run_polling()

if __name__ == '__main__':
    # Run the bot with polling
    run_polling()
