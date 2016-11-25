#!/usr/local/bin/env python

import requests
from BeautifulSoup import BeautifulSoup
import boto3
import time
import datetime
import Tkinter
from Tkinter import *


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


# def topicSelect(location):
#     switcher = {
#         '0': 'arn:aws:sns:us-west-2:152022601810:C3_Menu',
#         '1': 'arn:aws:sns:us-west-2:152022601810:MS_Menu',
#         '2': 'arn:aws:sns:us-west-2:152022601810:GOV_Menu',
#     }
# return switcher.get(location,
# 'arn:aws:sns:us-west-2:152022601810:C3_Menu')


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
    response = requests.get('https://myubcard.com/dining/menu')
    html = response.content
    soup = BeautifulSoup(html)
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
    return menu


def createMenu(location):

    menu = ''
    menu = '\nTonight, ' + dayOfWeek(datetime.datetime.today().weekday()) + ' ' + \
        time.strftime("%m/%d") + ' @ ' + locationSelect(location) + '\n'

    menu += getMenu(location)
    return menu


def setMenuArea():
    enter = str(ButtonLocation.get())
    menuText.set(createMenu(enter))

root = Tkinter.Tk()
root.title("UB Dinner")
root.minsize(300, 700)


ButtonLocation = IntVar()
ButtonLocation.set(0)

menuText = StringVar()
setMenuArea()
menuView = Label(root, textvariable=menuText)

c3Button = Radiobutton(root, text="C3", value=0,
                       command=setMenuArea, variable=ButtonLocation)
c3Button.pack(anchor=W)
southButton = Radiobutton(root, text="South", value=1,
                          command=setMenuArea, variable=ButtonLocation)
southButton.pack(anchor=W)
govButton = Radiobutton(root, text="Governors", value=2,
                        command=setMenuArea, variable=ButtonLocation)
govButton.pack(anchor=W)
menuView.pack()

c3Button.select()

root.mainloop()
