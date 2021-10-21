import time
import requests
import schedule
from mushroom_spores import mushroom_spore


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
    print("Check url list for mushroom")
    url_list = load_url_list()

    tmp = []
    for json in url_list:
        url = json["domain"]
        try:
            re = requests.get(url)
            if re.status_code == 200:
                tmp.append(json)
        except:
            print("Error in " + str(url))
    run(tmp)


def run(url_list):
    mushroom_list = []
    for json in url_list:
        try:
            url = json["domain"]
            pdi = json["id"]
            mushroom = mushroom_spore(url, pdi, 1)
            mushroom_list.append(mushroom)
        except:
            print("Error in " + str(json))

    for mushroom in mushroom_list:
        try:
            print("Start Scan for " + mushroom.url)
            mushroom.run_all()
        except:
            pass


schedule.every().day.at("21:10").do(check_url_list)
while True:
    schedule.run_pending()
    time.sleep(1)
