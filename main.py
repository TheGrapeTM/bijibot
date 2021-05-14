from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    ConversationHandler,
    CallbackContext,
)
import keys

print('Bot started...')

def start_command(update, context):
    reply_keyboard = [['Talk', 'Photo', 'Send lub']]
    update.message.reply_text(
        #  'Hi! My name is Professor Bot. I will hold a conversation with you. '
        'What would you like biji to do?'
        'Send /cancel at any time to stop talking to me. But I\'ll be sad :(\n\n',
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True),
    )
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
    #  bot = telegram.Bot(keys.API_KEY)
    updater = Updater(keys.API_KEY)
    dispatcher = updater.dispatcher

    #  bot.send_message('Hello, type /start to start the program')

    dispatcher.add_handler(CommandHandler('start', start_command))
    #  dispatcher.add_handler(CommandHandler('help', help_command))
    #
    dispatcher.add_error_handler(error)

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()






