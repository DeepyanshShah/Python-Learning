import requests

# response = requests.get("https://google.com")
# print(response.text)

url = "https://jsonplaceholder.typicode.com/posts"

data = {
    "title" : "amazon",
    "body" : "search",
    "userId" : "50"
}

headers = {
    'Content-type': 'application/json; charset=UTF-8',
}

response = requests.post(url, headers=headers, json=data)
print(response.text)

# Beautiful soup for web scraping

from bs4 import BeautifulSoup

url = ""
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')
print(soup.prettify())
 
for heading in soup.find_all("h2"):
    print(heading.text)

