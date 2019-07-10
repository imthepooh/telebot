"""
Simple Bot to reply to Telegram messages.

First, a few handler functions are defined. Then, those functions are passed to
the Dispatcher and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.

Usage:
Basic Echobot example, repeats messages.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""
# import all the required components
from telegram.ext import CommandHandler, Updater, Dispatcher, MessageHandler, Filters
import logging
import os
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)

logger = logging.getLogger(__name__)


# Defined the handler methods
def start(bot, update):
    # print('Update object: ', bot)
    # print('Context object: ',update)

    #chat_id or chat.id both can be used below 
    bot.send_message(chat_id=update.message.chat_id,text="Hello! what can I do for you ?")

def error(bot, update):
    # Log errors
    logger.warning('Update "%s" caused error "%s"', bot, update.error)

def reverse(bot,update):
    received_text =update.message.text
    return_text = update.message.text[::-1]
    bot.send_message(chat_id=update.message.chat_id,text=return_text)
    if (received_text == return_text):
        bot.send_message(chat_id=update.message.chat_id,text="Hey! that was a palindrome!!")

def main():
    # Initialize the updater and dispatcher
    tok = os.getenv("TOKEN")
#     testing start
    print('T:',tok)
#   testing end
    updater = Updater(token=tok)
    dispatcher = updater.dispatcher

    # Register the handlers
    start_handler = CommandHandler('start',start)
    dispatcher.add_handler(start_handler)

    dispatcher.add_handler(MessageHandler(Filters.text,reverse))

    dispatcher.add_error_handler(error)

    # Start polling for updates
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()

if __name__ == '__main__':
    main()
