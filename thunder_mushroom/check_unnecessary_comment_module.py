import re
from request_thunder_module import request_thunder

unnecessary_comment_regex_list = {
    'html comment':'<!--([^"]*)-->'
}

def fine_line(html_text, start_line):
    line_num = 0 
    for word_num in range(start_line):
        if html_text[word_num] == "\t":
            line_num+=1
    return line_num + 1

def Unnecessary_Comment(list_of_page, list_of_html_source, project_id, how):
    global unnecessary_comment_regex_list
    print("Start check unnecessary comment")
    
    for page_html in list_of_html_source:
        thunder_num = 0
        change_n_to_t = page_html.replace("<!DOCTYPE html>", "")
        change_n_to_t = change_n_to_t.replace("\n", "\t")
        body = ""
        print("Check unnecessary comment => " + list_of_page[list_of_html_source.index(page_html)])
        for regex in unnecessary_comment_regex_list.keys():
            check_regex = re.compile(unnecessary_comment_regex_list[regex])
            if check_regex.search(page_html):
                regex_group = check_regex.finditer(page_html)
                for regex_children in regex_group:
                    thunder_num += 1
                    line_num = fine_line(change_n_to_t, regex_children.start())
                    body += "Check please "+ str(line_num) +" line \n"
                    body += "It seems to be " + str(regex) + "\n\n"
        body = "Find "+str(thunder_num)+"unnecessary comments!" + body
        print(body)
        if thunder_num != 0:
            if how == 1:
                request_thunder("Unnecessary Comment", project_id, body, list_of_page[list_of_html_source.index(page_html)], 3)
    print("Finish check unnecessary comment")
