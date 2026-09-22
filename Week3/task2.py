import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.bahria.edu.pk/page/PageTemplate4?pageContentId=4603&WebsiteID=5"
response = requests.get(url)
response = response.content

soup = BeautifulSoup(response, 'html.parser')

teachers = []

tables = soup.find_all('table')

for table in tables:
    rows = table.find_all('tr')
    for row in rows:
        cols = row.find_all('td')
        if len(cols) == 2:
            name = cols[0].text.strip()
            designation = cols[1].text.strip()
            print(name, designation)
            teachers.append([name, designation])

df = pd.DataFrame(teachers)
df.to_csv('teachers.csv')