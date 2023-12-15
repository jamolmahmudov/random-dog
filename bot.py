from settings import get_token
from telegram.ext import (
    Updater, 
    CommandHandler,
    MessageHandler,
    Filters,
)
from handlers import (
    start,
    # send_dog,
)


def main():
    TOKEN = get_token()

    # create udpater obj
    updater = Updater(TOKEN)
    
    # create dispatcher obj
    dispatcher = updater.dispatcher
    
    # add command handlers
    dispatcher.add_handler(handler=CommandHandler(command='start', callback=start))
    
    # add message handlers
    # dispatcher.add_handler(handler=MessageHandler(filters=Filters.text('ok'), callback=send_dog))

    # start polling
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
