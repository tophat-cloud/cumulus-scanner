from request_thunder_module import request_thunder
import requests

admin_cheat_sheet = [
    "admin.php",
    "admin.html",
    "index.php",
    "login.php",
    "login.html",
    "administrator",
    "admin",
    "adminpanel",
    "cpanel",
    "login",
    "wp-login.php",
    "administrator",
    "admins",
    "logins",
    "admin.asp",
    "login.asp",
    "adm/",
    "admin/",
    "admin/account.html",
    "admin/login.html",
    "admin/login.htm",
    "admin/controlpanel.html",
    "admin/controlpanel.htm",
    "admin/adminLogin.html",
    "admin/adminLogin.htm",
    "admin.htm",
    "admin.html",
    "adminitem/",
    "adminitems/",
    "administrator/",
    "administrator/login.%EXT%",
    "administrator.%EXT%",
    "administration/",
    "administration.%EXT%",
    "adminLogin/",
    "adminlogin.%EXT%",
    "admin_area/admin.%EXT%",
    "admin_area/",
    "admin_area/login.%EXT%"
]

def guessing_admin(project_id, domain, list_of_page):
    global admin_cheat_sheet
    url = domain
    find_num = 0
    for admin_cheat in admin_cheat_sheet:
        check_url = url + admin_cheat
        if check_url not in list_of_page:
            requests_statis_code = requests.get(check_url).status_code
            if requests_statis_code == 200:
                find_num +=1
                body = "Check please " + str(check_url) + " \n"
                body +="It seems to be admin pages."
                request_thunder("guessing admin page", project_id, body, check_url, 2)
    print("Find " + str(find_num)+ " admin pages!")