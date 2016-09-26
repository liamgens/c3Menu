import requests
from BeautifulSoup import BeautifulSoup
import boto3
import time
import datetime

# TODO add the date in the heading
# TODO set an automatic time to run
# TODO add multiple dining centers
# TODO add headings


def dayOfWeek(day):
    switcher = {
        0: 'Monday',
        1: 'Tuesday',
        2: 'Wednesday',
        3: 'Thursday',
        4: 'Friday',
        5: 'Saturday',
        6: 'Sunday',
    }
    return switcher.get(day, "DAY_INVALID")

sns = boto3.client('sns')
arn = 'arn:aws:sns:us-west-2:152022601810:C3_Menu'

response = requests.get('https://myubcard.com/dining/menu')
html = response.content
soup = BeautifulSoup(html)
menuDiv = soup.find('div', attrs={'id': 'menu-56-dinner'})

menu = '\n\nTonight, ' + dayOfWeek(datetime.datetime.today().weekday()) + ' ' + \
    time.strftime("%m/%d") + ' @ C3\n'

for ul in menuDiv.find('ul'):
    for li in ul.findAll('li', attrs={'class': 'item-li dinner-border'}):
        menu += '-' + li.text + '\n'
menu += '\n' + time.strftime("%m/%d/%Y") + ' ' + time.strftime("%I:%M:%S %p")
print menu
sns.publish(TopicArn=arn, Message=menu)