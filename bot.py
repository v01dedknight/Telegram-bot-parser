from bs4 import BeautifulSoup
import requests

# Array to news from web. URL
newsFromUser = []
url = "https://kemsu.ru/"
userRequest = input("Пожалуйста, введите запрос на поиск: ")
countOfNews = 0

# Response from the server on GET 
response = requests.get(url)

# BS object with HTML text. Using html parser
soup = BeautifulSoup(response.text, "html.parser")

# Request from user
items = soup.find_all("a", string=lambda text: text and userRequest in text)

# Appending all founded results in news array
for item in items:
    countOfNews += 1
    newsFromUser.append(item.text)

# Output
print(f"\nПо вашему запросу найдено {countOfNews} постов.\n")
if countOfNews != 0:
    print("- - - - Доступные новости - - - -")
    for new in newsFromUser:
        print(new)
