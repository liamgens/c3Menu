import menu
from groupy import Bot, Group
import json
import urllib.parse

BASE_URL = 'https://api.groupme.com/v3/groups'
TOKEN = '04VZXqz6exVIOBqP6PQATSE1LBISUsGtbnRGn3TR'
params = {
    'token': TOKEN
}
FOOD_ITEMS_KEYWORDS = set(['corndogs', 'wings'])
menu.getMenu(0)

print (menu.listOfMenuItem)
