import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.bahria.edu.pk/page/PageTemplate4?pageContentId=4603&WebsiteID=5"
response = requests.get(url)
response = response.content

soup = BeautifulSoup(response, 'html.parser')

books = []

ol = soup.find('ol')
articles = ol.find_all('article', class_='product_pod')

for article in articles:
    titles = article.find('img')
    titles = titles.attrs['alt']

    star = article.find('p')
    star = star['class'][1]

    price = article.find('p', class_='price_color').text

    image = article.find('img')
    image_url = image["src"]

    books.append([titles, star, price, image_url])

df = pd.DataFrame(books, columns=['title', 'rating', 'price', 'image_url'])
print(df)
df.to_csv('books.csv', index=False)