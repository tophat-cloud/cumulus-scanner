from selenium import webdriver
from bs4 import BeautifulSoup

class make_page_list:

    def __init__(self, url):
        self.base_url = url
        self.list_url = [url]
        webdriver_options = webdriver.ChromeOptions()
        webdriver_options.add_argument('headless')
        webdriver_options.add_argument('disable-gpu')
        self.driver = webdriver.Chrome("./chromedriver.exe", options = webdriver_options)
        # self.driver = wevdriver.Chrome("./chromedriver", options = webdriver_options)
        self.find_href(url)

    def find_href(self, url):
        self.driver.get(url)
        self.driver.implicitly_wait(3)
        html = self.driver.page_source
        tag = BeautifulSoup(html, "html.parser")
        tag = tag.select("a")
        if tag == []:
            pass
        else:
            for dept1 in tag:
                tmp = dept1.get("href")
                if tmp != None:
                    if tmp != "#" and ";" not in tmp:
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