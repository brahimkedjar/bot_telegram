import asyncio
import logging
from flask import Flask, request
from telegram import Update, WebAppInfo
from telegram.ext import Application, CommandHandler, CallbackContext, CallbackQueryHandler

# Replace 'YOUR_API_TOKEN' with your actual API token from BotFather
API_TOKEN = '7226265761:AAFT3jZ2a6sGRHZekSC3g5uBp5GZHX6a8UU'
WEBHOOK_URL = 'https://bot-telegram-vz95.onrender.com'  # Update with your Render app URL

# Initialize logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Initialize Flask app
app = Flask(__name__)

# Initialize Telegram application
application = Application.builder().token(API_TOKEN).build()

async def start(update: Update, context: CallbackContext) -> None:
    """Handle the /start command."""
    web_app_url = 'https://react-bot-tlgrm.vercel.app/'  # URL of your React app
    keyboard = [
        [InlineKeyboardButton("Open Game UI", web_app=WebAppInfo(url=web_app_url))]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text('Click the button below to open the game UI:', reply_markup=reply_markup)

# Add command handler
application.add_handler(CommandHandler("start", start))

@app.route('/' + API_TOKEN, methods=['POST'])
def webhook():
    """Handle incoming webhook requests."""
    json_str = request.get_data(as_text=True)
    update = Update.de_json(json_str, application.bot)
    application.process_update(update)
    return 'OK'

def run_set_webhook():
    """Set the webhook for the bot."""
    loop = asyncio.get_event_loop()
    webhook_url = WEBHOOK_URL + '/' + API_TOKEN
    loop.run_until_complete(application.bot.set_webhook(url=webhook_url))

if __name__ == '__main__':
    run_set_webhook()
    app.run(host='0.0.0.0', port=8080)
