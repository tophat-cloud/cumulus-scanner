from selenium import webdriver
from bs4 import BeautifulSoup

class make_page:

    def __init__(self, url, ostype):
        print("Start make page list => " + url)
        self.base_url = url
        self.list_url = [url]
        webdriver_options = webdriver.ChromeOptions()
        webdriver_options.add_argument('headless')
        webdriver_options.add_argument('disable-gpu')
        if ostype == "Windows":
            self.driver = webdriver.Chrome("./chromedriver_win.exe", options=webdriver_options)
        elif ostype == "Linux":
            self.driver = webdriver.Chrome("./chromedriver_linux", options = webdriver_options)
        elif ostype == "Darwin":
            self.driver = webdriver.Chrome("./chromedriver_mac64", options = webdriver_options)
        else:
            self.driver = webdriver.Chrome("./chromedriver_mac_m1", options = webdriver_options)
        self.find_href(url)

    def find_href(self, url):
        self.driver.get(url)
        self.driver.implicitly_wait(20)
        html = self.driver.page_source
        tag = BeautifulSoup(html, "html.parser")
        tag = tag.select("a")
        if tag == []:
            pass
        else:
            for dept1 in tag:
                tmp = dept1.get("href")
                if tmp != None:
                    if (tmp != "#" and ";" not in tmp) and tmp != "/":
                        if "http" not in tmp:
                            tmp = self.base_url + tmp
                            if tmp not in self.list_url:
                                self.list_url.append(tmp)
                                self.find_href(tmp)
                        elif self.base_url in tmp:
                            if tmp not in self.list_url:
                                self.list_url.append(tmp)
                                self.find_href(tmp)

    def get_url_list(self):
        self.driver.quit()
        return self.list_url
