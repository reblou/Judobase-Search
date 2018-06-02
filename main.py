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
    data = json.loads(page.text)
    final = {}
    final["competitors"] = {}
    for i in range(1, 15):
        for n in range(0, 6):
            print("n:", n)
            cid = data["categories"][str(i)]["competitors"][n]["id_person"]
            final["competitors"][cid] = get_add_info(cid)

    return final

def get_add_info(str_id):
    page = requests.get(baseurl + str_id)
    return json.loads(page.text)

def print_to_file(d):
    with open("data.json", "w") as f:
        json.dump(d, f, ensure_ascii=False)

def read_from_file():
    with open("data.json", "r") as f:
        return json.loads(f.read())

if __name__ == "__main__":
    d = read_from_file()
    for i in d["competitors"]:
        print(d["competitors"][i])
    #d = get_top_judoka()
    #print_to_file(d)
