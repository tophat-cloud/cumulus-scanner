import time
import requests
import schedule
from thunder_mushroom.mushroom_spores import mushroom_spores

url_list = ["http://tophatplayground.wookingwoo.com/"]

def load_url_list():
    #제작 예정
    pass

def check_url_list():
    global url_list
    tmp = []
    for url in url_list:
        re = requests.get(url)
        if re.status_code == 200:
            tmp.append(url)
    url_list = tmp
    run()

def run():
    global url_list
    mushroom_list = []
    for url in url_list:
        mushroom = mushroom_spores(url)
        mushroom_list.append(mushroom)

    for mushroom in mushroom_list:
        mushroom.run_all()

schedule.every().day.at("00:00").do(check_url_list)
while True:
    schedule.run_pending()
    time.sleep(1)

