from request_thunder_module import request_thunder
from bs4 import BeautifulSoup

def find_obfuscation_javascript(project_id, list_of_page, list_of_html_source):
    
    for page_html in list_of_html_source:
        java_script = BeautifulSoup(page_html, "lxml")
        java_script = java_script.select("script")
        body = ""
        num = 1
        if len(java_script) != 0 :
            
            for script in java_script:
                
                val = script.find("\n")
                if val == -1 or val == 0:
                    body += "Check please " +str(num) + "script\n"
                    body += "It seems to be Unobfuscated Java script code\n\n"
        request_thunder("Unobfuscated Java script", project_id, body, list_of_page[list_of_html_source.index(page_html)], 1)        

