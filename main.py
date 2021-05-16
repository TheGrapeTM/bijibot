import os, os.path
import random
import json
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update, Bot
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    ConversationHandler,
    CallbackQueryHandler,
    CallbackContext,
)
import keys

#  Indicate that the bot has started
print('Bot started...')

#  Instantiate states for conversation handler
PHOTO, LUB, TALK, ROUTE = map(chr, range(4))
TALKING, STRESS, COMFORT, BORED, STOP = map(chr, range(4, 9))

#  Load data file
with open('data.json') as json_file:
    data = json.load(json_file)


def start(update: Update, context: CallbackContext) -> int:
    reply_keyboard = [['Talk'], ['See a photo'], ['Send some lub']]
    update.message.reply_text(
        #  'Hi! My name is Professor Bot. I will hold a conversation with you. '
        'What would you like biji to do?\n'
        'Send /end at any time to stop talking to me. But I\'ll be sad :(',
        reply_markup=ReplyKeyboardMarkup(reply_keyboard,
                                         one_time_keyboard=True),
    )
    return ROUTE


def start_photo(update: Update, context: CallbackContext) -> int:
    reply_keyboard = [['Biji', 'Hairpees', 'Funnys']]
    update.message.reply_text(
        'okie so what type of photo of yebiji do you wanna see?',
        reply_markup=ReplyKeyboardMarkup(reply_keyboard,
                                         one_time_keyboard=True))
    return PHOTO


def sending_photo(update: Update, context: CallbackContext) -> int:
    photo_type = update.message.text
    pic = get_pic(photo_type)

    reply_keyboard = [['i wanna see another photo'],
                      ['i wanna do something else'], ['okie bye byes']]

    update.message.reply_photo(open(pic, 'rb'))
    update.message.reply_text('okie nah, a ' + photo_type + ' biji',
                              reply_markup=ReplyKeyboardMarkup(
                                  reply_keyboard, one_time_keyboard=True))

    return ROUTE


def get_pic(pic_type) -> str:
    photo_dir = './photos/'
    if pic_type == 'Biji':
        ext = 'biji/'
    if pic_type == 'Hairpees':
        ext = 'happy/'
    if pic_type == 'Funnys':
        ext = 'funny/'

    try:
        directory = photo_dir + ext
        dir_size = len([
            name for name in os.listdir(directory)
            if os.path.isfile(os.path.join(directory, name))
        ])
        #  print(dir_size)
        photo_no = str(random.randint(1, dir_size))
        #  print('sending photo number: '+ photo_no)
        pic = directory + photo_no + '.jpg'
    except Exception:
        pic = photo_dir + 'error.jpg'

    return pic


def start_lub(update: Update, context: CallbackContext) -> int:
    reply_keyboard = [['1', '2'], ['3', '4'], ['5', '6']]
    update.message.reply_text('okie how much lub do you want?',
                              reply_markup=ReplyKeyboardMarkup(
                                  reply_keyboard, one_time_keyboard=True))
    return LUB


def send_lub(update: Update, context: CallbackContext) -> int:
    stickers = data['stickers']['lub']
    no_of_stickers = int(update.message.text)

    reply_keyboard = [['enuf enuf thanks'], ['nu enuf, smore pls'],
                      ['enuf but i wanna nu something else']]

    update.message.reply_text('awww okie here, some lub for you')
    for num in range(no_of_stickers):
        sticker_no = random.randint(0, len(stickers) - 1)
        update.message.reply_sticker(stickers[sticker_no])
    update.message.reply_text('enuf lub? or do you want somemore?',
                              reply_markup=ReplyKeyboardMarkup(
                                  reply_keyboard, one_time_keyboard=True))

    return ROUTE


def talk(update: Update, context: CallbackContext) -> int:
    reply_keyboard = [['i\'m bored... 🙁'], ['biji stressi 😬'], ['biji sad 😞']]
    update.message.reply_text('Aww, what\'s up b?',
                              reply_markup=ReplyKeyboardMarkup(
                                  reply_keyboard, one_time_keyboard=True))
    return TALK


def start_stress(update: Update, context: CallbackContext) -> int:
    update.message.reply_text(
        '🥺 dun stress bitzy, come tell me whats stressing you',
        reply_markup=ReplyKeyboardRemove())
    return STRESS


def stress(update: Update, context: CallbackContext) -> int:
    stickers = data['stickers']['stress']

    reply_keyboard = [['i wanna talk smore🥺'], ['i wanna do something else'],
                      ['okie bye byes ']]

    update.message.reply_text(
        'ohh i see...\n'
        'its okie you can do its!! 💖\n'
        'yebiji believe in you 😊\n'
        '(if you\'re still stressed, you can drop the real biji a text and he\'ll reply as soon as he\'s free😘)'
    )

    sticker_no = random.randint(0, len(stickers) - 1)
    update.message.reply_sticker(stickers[sticker_no],
                                 reply_markup=ReplyKeyboardMarkup(
                                     reply_keyboard, one_time_keyboard=True))

    return ROUTE


def start_comfort(update: Update, context: CallbackContext) -> int:
    update.message.reply_text(
        'aiyo wai my biji sad...☹️ \n'
        'come tell biji what happened?',
        reply_markup=ReplyKeyboardRemove())
    return COMFORT


def comfort(update: Update, context: CallbackContext) -> int:
    stickers = data['stickers']['sad']

    reply_keyboard = [['i wanna talk smore🥺'], ['i wanna do something else'],
                      ['okie bye byes']]

    update.message.reply_text(
        'awww i see\n'
        'nun sad okie biji💖\n'
        'your biji will always be here for yous hehehe\n'
        'next time biji bring you out to eat sugois food okies 😋')

    sticker_no = random.randint(0, len(stickers) - 1)
    update.message.reply_sticker(stickers[sticker_no],
                                 reply_markup=ReplyKeyboardMarkup(
                                     reply_keyboard, one_time_keyboard=True))

    return ROUTE


def start_bored(update: Update, context: CallbackContext) -> int:
    update.message.reply_text(
        'aww dont bored hehe\n'
        'come biji share with you something 😜',
        reply_markup=ReplyKeyboardMarkup([['okies']]))
    return BORED


def bored(update: Update, context: CallbackContext) -> int:
    links = [link for link in data['links']]
    link = links[random.randint(0, len(links) - 1)]
    desc = data['links'][link]

    reply_keyboard = [['still bored 😕'],
                      ['sugois enuf but i wanna do something else'],
                      ['i wanna talk smore🥺'], ['okie bye byes']]

    update.message.reply_text(f'Link: {link}\nits about: {desc}',
                              reply_markup=ReplyKeyboardMarkup(reply_keyboard))

    return ROUTE


def end(update: Update, context: CallbackContext) -> int:
    update.message.reply_text(
        'okie bye bye biji <3\ndo a /start when you need me agains hehe',
        reply_markup=ReplyKeyboardRemove(),
    )
    return ConversationHandler.END


def main():
    #  bot = telegram.Bot(keys.API_KEY)
    updater = Updater(keys.API_KEY)
    dispatcher = updater.dispatcher

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            PHOTO: [
                MessageHandler(Filters.regex('^Biji|Hairpees|Funnys$'),
                               sending_photo),
            ],
            LUB: [MessageHandler(Filters.regex('^1|2|3|4|5|6$'), send_lub)],
            TALK: [
                MessageHandler(Filters.regex('^i\'m bored... 🙁$'),
                               start_bored),
                MessageHandler(Filters.regex('^biji stressi 😬$'),
                               start_stress),
                MessageHandler(Filters.regex('^biji sad 😞$'), start_comfort),
            ],
            ROUTE: [
                MessageHandler(Filters.regex('^Talk|i wanna talk smore🥺$'),
                               talk),
                MessageHandler(
                    Filters.regex('^See a photo|i wanna see another photo$'),
                    start_photo),
                MessageHandler(
                    Filters.regex('^Send some lub|nu enuf, smore pls$'),
                    start_lub),
                MessageHandler(
                    Filters.regex(
                        '^i wanna do something else|enuf but i wanna nu something else|sugois enuf but i wanna do something else$'
                    ), start),
                MessageHandler(Filters.regex('^still bored 😕$'), bored),
                MessageHandler(
                    Filters.regex('^okie bye byes|enuf enuf thanks$'), end),
            ],
            STRESS: [MessageHandler(Filters.text, stress)],
            COMFORT: [MessageHandler(Filters.text, comfort)],
            BORED: [MessageHandler(Filters.text, bored)]
        },
        fallbacks=[CommandHandler('end', end)])

    dispatcher.add_handler(conv_handler)

    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()
