# Import the search_news function from the parser module
from parser.kemsu_parser import search_news

# Retrieve news for the user and limit the number of results
def get_news_for_user(query: str, limit: int = 5) -> list[str]:
    # Perform a news search using the parser
    results = search_news(query)

    # Return only up to 'limit' number of results
    return results[:limit]
