import requests
from bs4 import BeautifulSoup
import time
import datetime

listOfMenuItem = []


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


def getMenu(location):
    response = requests.get('https://myubcard.com/dining/menu?date=1482016038')
    html = response.content
    soup = BeautifulSoup(html, "html.parser")
    menuDiv = soup.find('div', attrs={'id': menuSelect(location)})
    stations = []
    for ul in menuDiv.find('ul', attrs={'class': 'menu-ul'}):
        for h5 in menuDiv.findAll('h5', attrs={'class': 'time-of-day dinner-bg'}):
            if h5.text not in stations:
                stations.append(h5.text)
    i = 0
    menu = ''
    for li in menuDiv.findAll('li', attrs={'class': 'menu-li dinner-li'}):
        menu += '\n<<<' + stations[i] + '>>>\n'
        i += 1
        for ul in li.findAll('ul', attrs={'class': 'menu-ul'}):
            for li in ul.findAll('li', attrs={'class': 'item-li dinner-border'}):
                menu += '-' + li.text + '\n'
                listOfMenuItem.append(li.text)

    return menu


def createMenu(location):

    menu = ''
    menu = '\nTonight, ' + dayOfWeek(datetime.datetime.today().weekday()) + ' ' + \
        time.strftime("%m/%d") + ' @ ' + locationSelect(location) + '\n'

    menu += getMenu(location)
    return menu
