import requests
from BeautifulSoup import BeautifulSoup
from pushetta import Pushetta

API_KEY = "464a8af42f2c4226dea589e8d7aff8e7a5dd8756"

response = requests.get('https://myubcard.com/dining/menu?date=1475088175')
html = response.content
soup = BeautifulSoup(html)
menuDiv = soup.find('div', attrs={'id': 'menu-56-dinner'})
dinnerItem = menuDiv.findAll('li', attrs={'class': 'item-li dinner-border'})

listOfDinner = []

for ul in menuDiv.find('ul'):
    for li in ul.findAll('li', attrs={'class': 'item-li dinner-border'}):
        print li.text
        listOfDinner.append(li.text)
