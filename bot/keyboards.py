# Import necessary components for creating custom keyboards
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# Create the main menu keyboard
def main_menu_keyboard() -> ReplyKeyboardMarkup:
    # Define a keyboard with two buttons: "Новости" and "Расписание"
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Новости")],
            [KeyboardButton(text="Расписание")],
        ],
        resize_keyboard=True  # Automatically resize keyboard to fit buttons
    )

# Create a back button keyboard
def back_keyboard() -> ReplyKeyboardMarkup:
    # Define a keyboard with a single "Back" button
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Назад")]
        ],
        resize_keyboard=True
    )