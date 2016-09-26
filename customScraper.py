import requests
from BeautifulSoup import BeautifulSoup
import boto3

response = requests.get('https://myubcard.com/dining/menu')
html = response.content
soup = BeautifulSoup(html)
menuDiv = soup.find('div', attrs={'id': 'menu-56-dinner'})
dinnerItem = menuDiv.findAll('li', attrs={'class': 'item-li dinner-border'})

listOfDinner = []

for ul in menuDiv.find('ul'):
    for li in ul.findAll('li', attrs={'class': 'item-li dinner-border'}):
        print li.text
        listOfDinner.append(li.text)

publishAmazonSnsMsg('Dinner', 'arn:aws:sns:us-west-2:152022601810:C3_Menu',
                    'Ass for Days', 'AKIAI4X4J46SHFPQ6QWQ', 'vafJzXS9xmPmV8T6P/jZVYVhtra7acRC3EOdpRLE')
