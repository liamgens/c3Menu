import requests
from BeautifulSoup import BeautifulSoup
import boto3
import time
import datetime

# TODO set an automatic time to run
# TODO Notifications for certain food
# TODO Someone signs up after 4pm
# TODO Switch to new service -- Request Days


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
    return switcher.get(day, 'DAY_INVALID')


def topicSelect(location):
    switcher = {
        '0': 'arn:aws:sns:us-west-2:152022601810:C3_Menu',
        '1': 'arn:aws:sns:us-west-2:152022601810:MS_Menu',
        '2': 'arn:aws:sns:us-west-2:152022601810:GOV_Menu',
    }
    return switcher.get(location, 'arn:aws:sns:us-west-2:152022601810:C3_Menu')


def menuSelect(location):
    switcher = {
        '0': 'menu-56-dinner',
        '1': 'menu-9-dinner',
        '2': 'menu-29-dinner',
    }
    return switcher.get(location, 'menu-56-dinner')


def locationSelect(location):
    switcher = {
        '0': 'C3',
        '1': 'South',
        '2': 'Governor\'s',
    }
    return switcher.get(location, 'C3')


def getMenu():
    i = 0
    menu = ''
    for li in menuDiv.findAll('li', attrs={'class': 'menu-li dinner-li'}):
        # menu += '<<<' + stations[i] + '>>>\n'
        # i += 1
        for ul in li.findAll('ul', attrs={'class': 'menu-ul'}):
            for li in ul.findAll('li', attrs={'class': 'item-li dinner-border'}):
                menu += '-' + li.text + '\n'
    return menu


sns = boto3.client('sns')
loc = raw_input(
    '\n0 for Crossroads Culinary Center\n1 for Main Street Market Dining Center\n2 for Governors Dining Center\n\nWhich one? ')
arn = topicSelect(loc)

response = requests.get('https://myubcard.com/dining/menu')
html = response.content
soup = BeautifulSoup(html)
menuDiv = soup.find('div', attrs={'id': menuSelect(loc)})

menu = ''
# menu = '\nTonight, ' + dayOfWeek(datetime.datetime.today().weekday()) + ' ' + \
#     time.strftime("%m/%d") + ' @ ' + locationSelect(loc) + '\n\n'

stations = []
for ul in menuDiv.find('ul', attrs={'class': 'menu-ul'}):
    for h5 in menuDiv.findAll('h5', attrs={'class': 'time-of-day dinner-bg'}):
        if h5.text not in stations:
            stations.append(h5.text)

time.sleep(1)

menu += getMenu()

menu += '\nText "STOP" to unsubscribe\n'
# time.strftime("%m/%d/%Y") + ' ' + time.strftime("%I:%M:%S %p")

print menu

sns.publish(TopicArn=arn, Message=menu)
