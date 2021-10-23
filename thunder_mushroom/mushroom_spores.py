from selenium import webdriver
from make_page_list import make_page
import re
import requests
from directory_travelser_module import Directory_Traversal
from check_unnecessary_comment_module import Unnecessary_Comment
from guessing_module import Guessing
from find_unobfuscation_code_module import Unobfuscated_Code

class mushroom_spore:

    def __init__(self, url, ostype, project_id="", how = 0):
        self.how = how
        if url[-1] == "/":
            self.url = url[:-1]
        else:
            self.url = url
        self.project_id = project_id
        self.list_of_page = []
        self.list_of_html_source = []
        self.ostype = ostype
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
        self.page_list(self.url)
        self.make_page_html_source()
        

    def page_list(self, url):

        page_list = make_page(url, self.ostype)
        self.list_of_page = page_list.get_url_list()

    def make_page_html_source(self):

        for page_url in self.list_of_page:
            self.driver.get(page_url)
            html_source = self.driver.page_source
            self.list_of_html_source.append(html_source)

    def run_all(self):
        Directory_Traversal(self.project_id, self.url, self.how)
        Unnecessary_Comment(self.list_of_page, self.list_of_html_source, self.project_id, self.how)
        Guessing(self.project_id, self.url, self.list_of_page, self.how)
        Unobfuscated_Code(self.project_id, self.list_of_page, self.list_of_html_source, self.how)
        print("Finish Scan url => " + self.url)
    
    def directory(self):
        Directory_Traversal(self.project_id, self.url, self.how)
        print("Finish Scan url => " + self.url)

    def check(self):
        Unnecessary_Comment(self.list_of_page, self.list_of_html_source, self.project_id, self.how)
        print("Finish Scan url => " + self.url)
    
    def guessing(self):
        Guessing(self.project_id, self.url, self.list_of_page, self.how)
        print("Finish Scan url => " + self.url)

    def find(self):
        Unobfuscated_Code(self.project_id, self.list_of_page, self.list_of_html_source, self.how)
        print("Finish Scan url => " + self.url)