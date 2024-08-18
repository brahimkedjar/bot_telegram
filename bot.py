from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext
import logging

# Replace 'YOUR_API_TOKEN' with your actual API token from BotFather
API_TOKEN = '7226265761:AAFT3jZ2a6sGRHZekSC3g5uBp5GZHX6a8UU'

# Initialize logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Create an Application instance with the bot token
application = Application.builder().token(API_TOKEN).build()

async def start(update: Update, context: CallbackContext) -> None:
    # Create a button that launches the React.js web app
    from telegram import InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
    web_app_url = 'https://react-bot-tlgrm.vercel.app/'
    keyboard = [
        [InlineKeyboardButton("Open Game UI", web_app=WebAppInfo(url=web_app_url))]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text('Click the button below to open the game UI:', reply_markup=reply_markup)

# Add a handler for the /start command
application.add_handler(CommandHandler("start", start))

if __name__ == '__main__':
    # Start polling for updates
    application.run_polling()
