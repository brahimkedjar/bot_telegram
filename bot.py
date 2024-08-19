from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext
import logging
import http.server
import socketserver
import threading

# Replace 'YOUR_API_TOKEN' with your actual API token from BotFather
API_TOKEN = '7226265761:AAFT3jZ2a6sGRHZekSC3g5uBp5GZHX6a8UU'

# Initialize logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Create an Application instance with the bot token
application = Application.builder().token(API_TOKEN).build()

async def start(update: Update, context: CallbackContext) -> None:
    # Create a button that launches the React.js web app
    from telegram import InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
    web_app_url = 'https://master--cheery-arithmetic-7fc8da.netlify.app/'
    keyboard = [
        [InlineKeyboardButton("Open Game UI", web_app=WebAppInfo(url=web_app_url))]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text('Click the button below to open the game UI:', reply_markup=reply_markup)

# Add a handler for the /start command
application.add_handler(CommandHandler("start", start))

def run_bot():
    # Start polling for updates
    application.run_polling()

# Create a simple HTTP server to handle health checks
PORT = 8000

class HealthCheckHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(b"OK")

def run_health_check_server():
    with socketserver.TCPServer(("", PORT), HealthCheckHandler) as httpd:
        print(f"Serving health check on port {PORT}")
        httpd.serve_forever()

if __name__ == '__main__':
    # Start the bot and health check server in separate threads
    bot_thread = threading.Thread(target=run_bot)
    server_thread = threading.Thread(target=run_health_check_server)

    bot_thread.start()
    server_thread.start()

    bot_thread.join()
    server_thread.join()
