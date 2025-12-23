# Import modules for HTTP requests and HTML parsing
import requests
from bs4 import BeautifulSoup

# Import configuration constants
from config.settings import KEMSU_URL, REQUEST_TIMEOUT

# Search for news on the Kemerovo State University website based on a query string
def search_news(query: str) -> list[str]:
    # Return empty list if query is empty
    if not query:
        return []

    try:
        # Send a GET request to the university website with a timeout
        response = requests.get(KEMSU_URL, timeout=REQUEST_TIMEOUT)
        # Raise an exception for HTTP errors
        response.raise_for_status()
    except requests.RequestException:
        # Return empty list if request fails
        return []

    # Parse the HTML response
    soup = BeautifulSoup(response.text, "html.parser")

    # Find all <a> tags containing the query text (case-insensitive)
    items = soup.find_all(
        "a",
        string=lambda text: text and query.lower() in text.lower()
    )

    # Return a list of cleaned text from the found elements
    return [item.text.strip() for item in items]


if __name__ == "__main__":
    # Simple module test without Telegram
    results = search_news("расписание")
    for r in results:
        print(r)
