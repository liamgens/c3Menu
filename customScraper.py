import requests
from BeautifulSoup import BeautifulSoup
import boto3

sns = boto3.client('sns')
arn = 'arn:aws:sns:us-west-2:152022601810:C3_Menu'

response = requests.get('https://myubcard.com/dining/menu')
html = response.content
soup = BeautifulSoup(html)
menuDiv = soup.find('div', attrs={'id': 'menu-56-dinner'})
dinnerItem = menuDiv.findAll('li', attrs={'class': 'item-li dinner-border'})

listOfDinner = []
menu = ''

for ul in menuDiv.find('ul'):
    for li in ul.findAll('li', attrs={'class': 'item-li dinner-border'}):
        print li.text
        listOfDinner.append(li.text)
        menu += li.text + '\n'

sns.publish(TopicArn=arn, Message=menu)
