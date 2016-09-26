import requests
from BeautifulSoup import BeautifulSoup
import boto3
import time

# TODO add the date in the heading
# TODO set an automatic time to run
# TODO add multiple dining centers
# TODO add headings

sns = boto3.client('sns')
arn = 'arn:aws:sns:us-west-2:152022601810:C3_Menu'

response = requests.get('https://myubcard.com/dining/menu')
html = response.content
soup = BeautifulSoup(html)
menuDiv = soup.find('div', attrs={'id': 'menu-56-dinner'})

menu = '\n\n'

for ul in menuDiv.find('ul'):
    for li in ul.findAll('li', attrs={'class': 'item-li dinner-border'}):
        menu += '-' + li.text + '\n'
menu += '\n' + time.strftime("%m/%d/%Y") + ' ' + time.strftime("%I:%M:%S %p")
print menu
sns.publish(TopicArn=arn, Message=menu)
