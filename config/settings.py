# Import modules for environment variable loading and OS interaction
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the Telegram bot token from environment variables
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
# Raise an error if the token is not found
if not TELEGRAM_TOKEN:
    raise RuntimeError("TELEGRAM_TOKEN not found in environment variables")

# Base URL of the university website
KEMSU_URL = "https://kemsu.ru/"

# Default timeout for HTTP requests (in seconds)
REQUEST_TIMEOUT = 10
