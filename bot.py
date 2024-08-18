from flask import Flask, request
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import Application, CommandHandler, CallbackContext, CallbackQueryHandler
import logging

# Replace 'YOUR_API_TOKEN' with your actual API token from BotFather
API_TOKEN = '7226265761:AAFT3jZ2a6sGRHZekSC3g5uBp5GZHX6a8UU'
WEBHOOK_URL = 'https://react-bot-tlgrm.vercel.app/'  # Update with your Render app URL

# Initialize logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

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

application.add_handler(CommandHandler("start", start))

@app.route('/' + API_TOKEN, methods=['POST'])
def webhook():
    json_str = request.get_data(as_text=True)
    update = Update.de_json(json_str, application.bot)
    application.process_update(update)
    return 'OK'

def set_webhook():
    application.bot.set_webhook(url=WEBHOOK_URL + API_TOKEN)

if __name__ == '__main__':
    set_webhook()
    app.run(host='0.0.0.0', port=8080)
