import selenium
from selenium import webdriver
from bs4 import BeautifulSoup


class mushroom_spores():

    def __init__(self, url):
        self.url = url
        self.list_of_page = [url]
        webdriver_options = webdriver.ChromeOptions()
        webdriver_options.add_argument('headless')
        webdriver_options.add_argument('disable-gpu')
        self.driver = webdriver.Chrome("./chromedriver.exe", options = webdriver_options)  # in win10
        # self.driver = wevdriver.Chrome("./chromedriver", options = webdriver_options) #in linux
        self.search_page_map()

    def search_page_map(self):
        pass
