from telegram import Update, InputMediaPhoto
from telegram.ext import Application, CommandHandler, CallbackContext
import logging

# Replace 'YOUR_API_TOKEN' with your actual API token from BotFather
API_TOKEN = '7226265761:AAFT3jZ2a6sGRHZekSC3g5uBp5GZHX6a8UU'

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

async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text('Welcome! Use /showcombos to see the daily combos.')

async def show_combos(update: Update, context: CallbackContext) -> None:
    text = 'Here are the daily combos:\n'
    for game, data in combos.items():
        text += f'\n{game}:\nCode: {data["code"]}\n'
        await context.bot.send_photo(chat_id=update.effective_chat.id, photo=data['photo'])
    await update.message.reply_text(text)

async def update_combos(update: Update, context: CallbackContext) -> None:
    # Ensure only the admin can update combos (replace 'YOUR_ADMIN_ID' with your actual admin ID)
    if update.message.from_user.id != 6754210573:
        await update.message.reply_text('You are not authorized to use this command.')
        return

    try:
        game = context.args[0]
        photo_url = context.args[1]
        code = context.args[2]
        combos[game] = {'photo': photo_url, 'code': code}
        await update.message.reply_text(f'Updated {game} combo successfully!')
    except (IndexError, ValueError):
        await update.message.reply_text('Usage: /updatecombo <game> <photo_url> <code>')

def main() -> None:
    # Create the application instance
    application = Application.builder().token(API_TOKEN).build()

    # Add handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("showcombos", show_combos))
    application.add_handler(CommandHandler("updatecombo", update_combos))

    # Run the bot
    application.run_polling()

if __name__ == '__main__':
    main()
