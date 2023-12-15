from telegram.ext import CallbackContext
from telegram import Update, ReplyKeyboardMarkup, KeyboardButton


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
