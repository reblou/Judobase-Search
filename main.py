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
            cid = data["categories"][str(i)]["competitors"][n]["id_person"]
            data["categories"][str(i)]["competitors"][n].update(get_add_info(cid))
            print(data["categories"][str(i)]["competitors"][n]["family_name"], data["categories"][str(i)]["competitors"][n]["points"], data["categories"][str(i)]["competitors"][n]["weight_name"], data["categories"][str(i)]["competitors"][n]["ftechnique"])
            #print(type(data["categories"][str(i)]["competitors"][n]))
        competitors += data["categories"][str(i)]["competitors"]


    print(len(competitors))
    return competitors

def get_add_info(str_id):
    page = requests.get(baseurl + str_id)
    data = json.loads(page.text)

    add_info = {}
    add_info["ftechnique"] = data["ftechique"]
    add_info["side"] = data["side"]
    add_info["height"] = data["height"]
    return add_info


if __name__ == "__main__":
    page = requests.get(url)
    print(page.text)
    data = json.loads(page.text)


    get_top_judoka()
    get_add_info("2239")
