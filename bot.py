from telegram import Update, InputMediaPhoto
from telegram.ext import Updater, CommandHandler, CallbackContext
import logging

# Replace '7226265761:AAFT3jZ2a6sGRHZekSC3g5uBp5GZHX6a8UU' with your actual API token from BotFather
API_TOKEN = 'YOUR_API_TOKEN'

# Initialize logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Example data for combos
combos = {
    'game1': {
        'photo': 'https://example.com/photo1.jpg',
        'code': 'COMBO123'
    },
    'game2': {
        'photo': 'https://example.com/photo2.jpg',
        'code': 'COMBO456'
    }
}

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Welcome! Use /showcombos to see the daily combos.')

def show_combos(update: Update, context: CallbackContext) -> None:
    text = 'Here are the daily combos:\n'
    for game, data in combos.items():
        text += f'\n{game}:\nCode: {data["code"]}\n'
        context.bot.send_photo(chat_id=update.effective_chat.id, photo=data['photo'])
    update.message.reply_text(text)

def update_combos(update: Update, context: CallbackContext) -> None:
    # Ensure only the admin can update combos (replace 'YOUR_ADMIN_ID' with your actual admin ID)
    if update.message.from_user.id != YOUR_ADMIN_ID:
        update.message.reply_text('You are not authorized to use this command.')
        return

    try:
        game = context.args[0]
        photo_url = context.args[1]
        code = context.args[2]
        combos[game] = {'photo': photo_url, 'code': code}
        update.message.reply_text(f'Updated {game} combo successfully!')
    except (IndexError, ValueError):
        update.message.reply_text('Usage: /updatecombo <game> <photo_url> <code>')

def main() -> None:
    updater = Updater(API_TOKEN, use_context=True)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("showcombos", show_combos))
    dp.add_handler(CommandHandler("updatecombo", update_combos))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
