from flask import Flask
from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext, Updater
import logging

# Replace 'YOUR_API_TOKEN' with your actual API token from BotFather
API_TOKEN = '7226265761:AAFT3jZ2a6sGRHZekSC3g5uBp5GZHX6a8UU'

# Initialize logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

app = Flask(__name__)

# Initialize the Updater and pass it your bot's token.
updater = Updater(token=API_TOKEN)

# Get the dispatcher to register handlers
dispatcher = updater.dispatcher

async def start(update: Update, context: CallbackContext) -> None:
    # Create a button that launches the React.js web app
    web_app_url = 'https://react-bot-tlgrm.vercel.app/'
    keyboard = [
        [InlineKeyboardButton("Open Game UI", web_app=WebAppInfo(url=web_app_url))]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text('Click the button below to open the game UI:', reply_markup=reply_markup)

# Add a handler for the /start command
dispatcher.add_handler(CommandHandler("start", start))

def run_bot():
    # Start the Bot
    updater.start_polling()

if __name__ == '__main__':
    run_bot()
    app.run(host='0.0.0.0', port=8080)
