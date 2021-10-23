import time
import requests
import schedule
import traceback
from mushroom_spores import mushroom_spore
from slacker import Slacker
from datetime import datetime

def post_message(text):
    url = "" #use your slack webhook url
    response = requests.post(url,
        json={"text" : text}
    )

def load_url_list():
    re = requests.post("https://api.cumulus.tophat.cloud/project/domains")
    try:
        if re.status_code != 200:
            return {}
    except:
        print("Error in url server")
    return re.json()


def check_url_list():
    print("Periodic inspection starta at 00:00")
    post_message("Periodic inspection starta at 00:00")
    post_message("Check url list for mushroom")
    print("Check url list for mushroom")
    url_list = load_url_list()

    tmp = []
    for json in url_list:
        url = json["domain"]
        try:
            re = requests.get(url)
            print(url)
            if re.status_code == 200:
                tmp.append(json)
        except:
            print("Error in " + str(url))
            post_message("Error in " + str(url))
    run(tmp)
    print("Finish Scan")
    post_message("Finish Scan")


def run(url_list):
    mushroom_list = []
    for json in url_list:
        try:
            url = json["domain"]
            pdi = json["id"]
            mushroom = mushroom_spore(url, "Linux", pdi, 1)
            mushroom_list.append(mushroom)
        except:
            print("Error in " + str(json))
            post_message("Error in " + str(json))
            traceback.print_exc()

    for mushroom in mushroom_list:
        try:
            print("Start Scan for " + mushroom.url)
            post_message("Start Scan for " + mushroom.url)
            mushroom.run_all()
            post_message("Finish Scan for " + mushroom.url) 
        except:
            pass


schedule.every().day.at("00:00").do(check_url_list)
while True:
    schedule.run_pending()
    time.sleep(1)
