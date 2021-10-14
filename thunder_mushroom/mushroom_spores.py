from selenium import webdriver
from make_page_list import make_page
import re
import requests
from directory_travelser_module import directory_travelser
from check_unnecessary_comment_module import check_unnecessary_comment

class mushroom_spore:

    def __init__(self, url, project_id):
        if url[-1] == "/":
            self.url = url[:-1]
        else:
            self.url = url
        self.project_id = project_id
        self.list_of_page = []
        self.list_of_html_source = []
        webdriver_options = webdriver.ChromeOptions()
        webdriver_options.add_argument('headless')
        webdriver_options.add_argument('disable-gpu')
        #self.driver = webdriver.Chrome("./chromedriver.exe", options=webdriver_options)  # in win10
        self.driver = webdriver.Chrome("./chromedriver", options = webdriver_options) #in linux
        self.page_list(self.url)
        self.make_page_html_source()

    def page_list(self, url):

        page_list = make_page(url)
        self.list_of_page = page_list.get_url_list()

    def make_page_html_source(self):

        for page_url in self.list_of_page:
            self.driver.get(page_url)
            html_source = self.driver.page_source
            self.list_of_html_source.append(html_source)

    def run_all(self):
        directory_travelser(self.project_id, self.url)
        check_unnecessary_comment(self.list_of_page, self.list_of_html_source, self.project_id)
        print("Finish Scan url => " + self.url)
