# Import necessary components from aiogram
from aiogram import Router, F
from aiogram.types import Message

# Import the news search function and main menu keyboard
from services.search import get_news_for_user
from bot.keyboards import main_menu_keyboard

# Create a router instance to handle incoming messages
router = Router()

# Handle the /start command
@router.message(F.text == "/start")
async def start_handler(message: Message):
    # Send a greeting message with the main menu keyboard
    await message.answer(
        "Привет! Я помощник КемГУ.\nВведите запрос для поиска новостей.",
        reply_markup=main_menu_keyboard()
    )

# Handle all text messages
@router.message(F.text)
async def text_handler(message: Message):
    # Strip extra spaces from the user input
    query = message.text.strip()

    # Search for news using the service function
    news = get_news_for_user(query)

    # Inform the user if no news is found
    if not news:
        await message.answer("По вашему запросу ничего не найдено.")
        return

    # Build a response string with found news
    response = "Найденные новости:\n\n"
    for item in news:
        response += f"• {item}\n"

    # Send the list of news to the user
    await message.answer(response)