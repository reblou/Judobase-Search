#!/usr/bin/env python

from bs4 import BeautifulSoup
import requests
import json
import psycopg2

baseurl = 'https://data.ijf.org/api/get_json?access_token=&params[action]=competitor.info&params[__ust]=&params[id_person]='
competitor = '#/competitor/profile/1540/basic_info'
wrl_url = 'https://judobase.ijf.org/#/wrl/f/simple'
competitors = "https://data.ijf.org/api/get_json?access_token=&params[action]=wrl.by_category&params[__ust]=&params[limit]=1000&params[gender]=&params[part]=info%2Cpoints"
num_judoka = 44735
api_url = "https://data.ijf.org/api/get_json?access_token="

url = 'https://data.ijf.org/api/get_json?access_token=&params[action]=competitor.info&params[__ust]=&params[id_person]=1540'

def populate_database():
    conn = psycopg2.connect(database="judoka")
    c = conn.cursor()
    judoka = get_top_judoka()
    print("type judoka:", type(judoka))
    print(judoka)
    for j in judoka:
        categories = ""
        try:
            c.execute("""INSERT INTO judoka VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""",
            (int(j["id_person"]), j["family_name"], j["given_name"], j["gender"], j["ftechnique"], j["side"], int(j["height"]), int(j["age"]), j["country"], j["weight_name"])
            )
        except Exception as e:
            print("--error inserting: ", j, "--")
            print(e)
            conn.commit()
    print("Judoka added:", len(judoka))
    conn.commit()
    conn.close()
    return


def get_top_judoka():
    page = requests.get(api_url + "&params[action]=wrl.by_category&params[__ust]=&params[limit]=1000&params[gender]=&params[part]=info%2Cpoints")
    print(page.text)
    data = json.loads(page.text)
    competitors = []
    print(data)
    for key in data:
        print(key)
    """
    for i in range(1, 15):
        for n in range(0, 71):
            cid = data["categories"][str(i)]["competitors"][n]["id_person"]
            #data["categories"][str(i)]["competitors"][n].update(get_add_info(cid))

            #print(data["categories"][str(i)]["competitors"][n]["family_name"], data["categories"][str(i)]["competitors"][n]["points"], data["categories"][str(i)]["competitors"][n]["weight_name"], data["categories"][str(i)]["competitors"][n]["ftechnique"])
            #print(type(data["categories"][str(i)]["competitors"][n]))
            #competitors.append(data["categories"][str(i)]["competitors"][n])
    """


    print(len(competitors))
    print("------")
    return competitors

def get_add_info(str_id):
    page = requests.get(baseurl + str_id)
    data = json.loads(page.text)
    print(data)

    add_info = {}
    add_info["ftechnique"] = data["ftechique"]
    add_info["side"] = data["side"]
    add_info["height"] = data["height"]
    add_info["age"] = data["age"]
    return add_info


if __name__ == "__main__":
    get_top_judoka()
    #get_add_info("2239")
