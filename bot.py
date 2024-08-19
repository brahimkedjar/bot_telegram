from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import Application, CommandHandler, CallbackContext
import logging
import threading
import http.server
import socketserver

# Replace 'YOUR_API_TOKEN' with your actual API token from BotFather
API_TOKEN = '7226265761:AAFT3jZ2a6sGRHZekSC3g5uBp5GZHX6a8UU'

# Initialize logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Create an Application instance with the bot token
application = Application.builder().token(API_TOKEN).build()

async def start(update: Update, context: CallbackContext) -> None:
    # Create a button that launches the React.js web app
    web_app_url = 'https://master--cheery-arithmetic-7fc8da.netlify.app/'
    keyboard = [
        [InlineKeyboardButton("Open Game UI", web_app=WebAppInfo(url=web_app_url))]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text('Click the button below to open the game UI:', reply_markup=reply_markup)

# Add a handler for the /start command
application.add_handler(CommandHandler("start", start))

# Function to run the bot
def run_bot():
    application.run_polling()

# Function to run a simple HTTP server for health checks
def run_server():
    PORT = 8000
    class Handler(http.server.SimpleHTTPRequestHandler):
        def do_GET(self):
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(b"Health check passed")

    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print("Serving at port", PORT)
        httpd.serve_forever()

if __name__ == '__main__':
    # Start the bot and the HTTP server in parallel threads
    threading.Thread(target=run_bot).start()
    threading.Thread(target=run_server).start()
