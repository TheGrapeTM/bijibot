import telegram.ext
import os

API_KEY = os.getenv('API_KEY')

print('Bot started...')

def start_command(update, context):
    """
    Starts the bot with /start
    """
    pass

def help_command(update, context):
    """
    Help menu with /help
    """
    pass

def handle_message(update, context):
    """
    Message Handler
    """
    pass

def error(update, context):
    """
    Error handler
    """
    print(f"Update {update} caused error {context.error}")
    pass

def main():
    updater = Updater(API_KEY)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', start_command))
    dispatcher.add_handler(CommandHandler('start', help_command))

    dispatcher.add_error_handler(error)

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()






