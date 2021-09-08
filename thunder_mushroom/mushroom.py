import time
import requests
import schedule
from mushroom_spores import mushroom_spore

url_list = ["http://tophatplayground.wookingwoo.com/"]

def load_url_list():
    #제작 예정
    pass

def check_url_list():
    print("Periodic inspection starta at 00:00")
    print("Check url list for mushroom")
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

        mushroom = mushroom_spore(url)
        mushroom_list.append(mushroom)

    for mushroom in mushroom_list:
        print("Start Scan for " + mushroom.url)
        mushroom.run_all()

schedule.every().day.at("00:00").do(check_url_list)
while True:
    schedule.run_pending()
    time.sleep(1)

