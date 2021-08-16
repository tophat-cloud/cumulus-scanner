import selenium
from selenium import webdriver
from make_page_list import make_page_list
from bs4 import BeautifulSoup
import re
import requests


class mushroom_spores:

    def __init__(self, url):
        self.url = url
        self.list_of_page = []
        self.list_of_html_source = []
        webdriver_options = webdriver.ChromeOptions()
        webdriver_options.add_argument('headless')
        webdriver_options.add_argument('disable-gpu')
        self.driver = webdriver.Chrome("./chromedriver.exe", options=webdriver_options)  # in win10
        # self.driver = wevdriver.Chrome("./chromedriver", options = webdriver_options) #in linux
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
                pass

            if regex_javascript.search(page_html):
                # api 전송
                pass

            maybe_comments = regex_javascript_one.findall(page_html)

            for maybe_comment in maybe_comments:
                if len(maybe_comment) == 2 or ("http:" not in maybe_comment or "href" not in maybe_comment):
                    # api 전송
                    pass


a = mushroom_spores("http://tophatplayground.wookingwoo.com/")
print(a.list_of_page)
