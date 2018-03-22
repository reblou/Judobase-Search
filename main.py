#!/usr/bin/env python

from bs4 import BeautifulSoup
import requests
import json

baseurl = 'https://data.ijf.org/api/get_json?access_token=&params[action]=competitor.info&params[__ust]=&params[id_person]='
competitor = '#/competitor/profile/1540/basic_info'
wrl_url = 'https://judobase.ijf.org/#/wrl/f/simple'
competitors = "https://data.ijf.org/api/get_json?access_token=&params[action]=wrl.by_category&params[__ust]=&params[limit]=1000&params[gender]=&params[part]=info%2Cpoints"
num_judoka = 44735
api_url = "https://data.ijf.org/api/get_json?access_token="

url = 'https://data.ijf.org/api/get_json?access_token=&params[action]=competitor.info&params[__ust]=&params[id_person]=1540'

def get_top_judoka():
    page = requests.get(api_url + "&params[action]=wrl.by_category&params[__ust]=&params[limit]=1000&params[gender]=&params[part]=info%2Cpoints")
    print(page.text)
    data = json.loads(page.text)
    competitors = []
    for i in range(1, 15):
        for n in range(0, 71):
            print(data["categories"][str(i)]["competitors"][n]["family_name"], data["categories"][str(i)]["competitors"][n]["points"])
        competitors += data["categories"][str(i)]["competitors"]


    print(len(competitors))

if __name__ == "__main__":
    page = requests.get(url)
    print(page.text)
    data = json.loads(page.text)

    get_top_judoka()
