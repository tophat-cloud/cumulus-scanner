from request_thunder_module import request_thunder
from selenium import webdriver
import requests

directory_cheat_sheet = ["%2e%2e%2f", "%2e%2e/",
                         "..%2f", "%2e%2e%5c", 
                         "%2e%2e\\", "..%5c", 
                         "%252e%252e%255c", "..%255c"
                         ]

def directory_travelser(domain, project_id):
    webdriver_options = webdriver.ChromeOptions()
    webdriver_options.add_argument('headless')
    webdriver_options.add_argument('disable-gpu')
    driver = webdriver.Chrome("./chromedriver", options = webdriver_options)
    url = domain+"/"
    print("Check directory travelser => " + url)
    driver.get(url)
    main_code = driver.page_source

    for cheat_value in directory_cheat_sheet:
        for num in range(1,5):
            new_url = url+cheat_value*num
            re = requests.get(new_url)
            if re.status_code == 200:
                driver.get(new_url)
                new_code = driver.page_source
                if new_code != main_code:
                    body = "Find directory travelser !!\n"
                    body += new_url +"\n"
                    request_thunder("directory travelser", project_id, body, domain, 3)