#!/usr/bin/env python

from bs4 import BeautifulSoup
import requests
import json

baseurl = 'https://judobase.ijf.org/'
competitor = '#/competitor/profile/1540/basic_info'

url = 'https://data.ijf.org/api/get_json?access_token=&params[action]=competitor.info&params[__ust]=&params[id_person]=1540'


if __name__ == "__main__":
    page = requests.get(url)
    print(page.text)
    data = json.loads(page.text)
