import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Your bot's API token
API_TOKEN = '7226265761:AAFT3jZ2a6sGRHZekSC3g5uBp5GZHX6a8UU'

# Example game data
games = {
    'game1': {
        'photo': 'PHOTO_FILE_ID_1',
        'combos': ['Combo 1', 'Combo 2', 'Combo 3']
    },
    'game2': {
        'photo': 'PHOTO_FILE_ID_2',
        'combos': ['Combo A', 'Combo B', 'Combo C']
    }
}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = [
        [InlineKeyboardButton(game, callback_data=game)] for game in games
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text('Choose a game:', reply_markup=reply_markup)

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    game = query.data
    game_info = games.get(game)
    
    if game_info:
        photo_id = game_info['photo']
        combos = game_info['combos']
        
        # Send the game photo
        await query.message.reply_photo(photo=photo_id, caption=f"Available combos for {game}:")
        
        # Send the combos
        combos_text = "\n".join(combos)
        await query.message.reply_text(f"Combos:\n{combos_text}")
    else:
        await query.message.reply_text("Game not found!")

async def main() -> None:
    application = Application.builder().token(API_TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button))

    await application.initialize()
    await application.start()
    logger.info("Bot is running...")
    await application.stop()

if __name__ == '__main__':
    import asyncio
    asyncio.run(main())
