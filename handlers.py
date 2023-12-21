from telegram.ext import CallbackContext
from telegram import Update, ReplyKeyboardMarkup, KeyboardButton
from dog import get_dog_image
from cat import get_cat_image



def start(update: Update, context: CallbackContext):
    user = update.message.from_user

    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text='🐶'), KeyboardButton(text='🐈')]
        ]
    )
    update.message.reply_html(
        text=f'Hello, {user.full_name}! Press one of the buttons.',
        reply_markup=keyboard
    )

def send_dog(update: Update, context: CallbackContext):
    
    update.message.reply_photo(
        photo=get_dog_image(),
        caption='<b><i>a random dog image.</i></b>',
        parse_mode='HTML'
    )

def send_cat(update: Update, context: CallbackContext):
    
    update.message.reply_photo(
        photo=get_cat_image(),
        caption='<b><i>a random cat image.</i></b>',
        parse_mode='HTML'
    )
