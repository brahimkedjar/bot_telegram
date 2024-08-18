import asyncio
from flask import Flask, request
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import Application, CommandHandler, CallbackContext
import logging

API_TOKEN = '7226265761:AAFT3jZ2a6sGRHZekSC3g5uBp5GZHX6a8UU'  # Ensure you set this in Render's environment variables
WEBHOOK_URL = 'https://bot-telegram-vz95.onrender.com/'  # Ensure this matches your Render URL
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

app = Flask(__name__)
application = Application.builder().token(API_TOKEN).build()

async def start(update: Update, context: CallbackContext) -> None:
    web_app_url = 'https://react-bot-tlgrm.vercel.app/'
    keyboard = [
        [InlineKeyboardButton("Open Game UI", web_app=WebAppInfo(url=web_app_url))]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text('Click the button below to open the game UI:', reply_markup=reply_markup)

application.add_handler(CommandHandler("start", start))

@app.route('/' + API_TOKEN, methods=['POST'])
def webhook():
    json_data = request.get_json()
    if json_data is None:
        return 'Invalid JSON', 400
    update = Update.de_json(json_data, application.bot)
    application.process_update(update)
    return 'OK'

def run_set_webhook():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(application.bot.set_webhook(url=WEBHOOK_URL))

if __name__ == '__main__':
    run_set_webhook()
    app.run(host='0.0.0.0', port=8080)
