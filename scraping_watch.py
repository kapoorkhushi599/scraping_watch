import requests
from bs4 import BeautifulSoup
import pandas as pd

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36"
}

url = "https://www.flipkart.com/search?q=Watches%20for%20men%20under%202000&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, "html.parser")

products = []
prices = []
ratings = []

items = soup.find_all("div", {"class": "hCKiGj"})

for item in items:
    name_tag = item.find("div", {"class": "syl9yP"})
    if not name_tag:
        name_tag = item.find("a", {"class": "syl9yP"})

    price_tag = item.find("div", {"class": "Nx9bqj"})
    rating_tag = item.find("div", {"class": "_3LWZlK"})

    if name_tag and price_tag:
        products.append(name_tag.text.strip())
        prices.append(price_tag.text.strip())
        ratings.append(rating_tag.text.strip() if rating_tag else "No rating")

df = pd.DataFrame({
    "Product Name": products,
    "Price": prices,
    "Rating": ratings
})

df.to_excel("newflipkart_watches.xlsx", index=False)
print("Data saved to newflipkart_watches.xlsx")