import selenium
from selenium import webdriver
from make_page_list import make_page_list
from bs4 import BeautifulSoup
import re
import requests


class mushroom_spores:

    def __init__(self, url):
        if url[-1] == "/":
            self.url = url[:-1]
        else:
            self.url = url
        self.list_of_page = []
        self.list_of_html_source = []
        webdriver_options = webdriver.ChromeOptions()
        webdriver_options.add_argument('headless')
        webdriver_options.add_argument('disable-gpu')
        self.driver = webdriver.Chrome("./chromedriver.exe", options=webdriver_options)  # in win10
        # self.driver = webdriver.Chrome("./chromedriver", options = webdriver_options) #in linux
        self.page_list(url)

    def page_list(self, url):

        page_list = make_page_list(url)
        self.list_of_page = page_list.get_url_list()

    def make_page_html_source(self):

        for page_url in self.list_of_page:
            self.driver.get(page_url)
            html_source = self.driver.page_source
            self.list_of_html_source.append(html_source)

    def check_unnecessary_comment(self):

        regex_html = re.compile(r'<--([^"]*)-->')
        regex_javascript = re.compile(r'/*')
        regex_javascript_one = re.compile(r'.?.?.?.?.?.?.?//')

        for page_html in self.list_of_html_source:

            if regex_html.search(page_html):
                # api 전송
                print("주석발견")
                pass

            if regex_javascript.search(page_html):
                # api 전송
                print("주석발견")
                pass

            maybe_comments = regex_javascript_one.findall(page_html)

            for maybe_comment in maybe_comments:
                if len(maybe_comment) == 2 or ("http:" not in maybe_comment or "href" not in maybe_comment):
                    # api 전송
                    print("주석발견")
                    pass

    def directory_travelser(self):
        url = self.url+"/"
        self.driver.get(url)
        main_code = self.driver.page_source
        directory_cheat_sheet = ["%2e%2e%2f", "%2e%2e/", "..%2f", "%2e%2e%5c", "%2e%2e\\", "..%5c", "%252e%252e%255c", "..%255c"]
        for cheat_value in directory_cheat_sheet:
            for num in range(1,5):
                new_url = url+cheat_value*num
                print(new_url)
                re = requests.get(new_url)
                if re.status_code == 200:
                    self.driver.get(new_url)
                    new_code = self.driver.page_source
                    if new_code == main_code:
                        # 취약점 발견
                        print("발견")



