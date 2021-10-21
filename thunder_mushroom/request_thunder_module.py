import requests
import json
def request_thunder(thunder_name, project_id, body, url, priority):
    js ={}
    if thunder_name == "Unnecessary Comment":
        js = {"description":"There are comments that can be dangerous.\nThe annotation might contain unobfuscated codes or sensitive content.",
              "suggestion":"Please remove unnecessary annotations from the code by minify or uglify.",
              "reference":"https://cwe.mitre.org/data/definitions/615.html"}
    elif thunder_name == "Unobfuscated Code":
        js = {
            "description": "In general, api addresses or sensitive information may be leaked if the verifiable page source code has an unobfuscated Java script code.",
            "suggestion": "You can find popular tools for Java bytecode obfuscation below, or simply enter java obfuscator in your favorite search engine."
                          "\nProGuard Java Optimizer is a very popular open source Java class file shrinker, optimizer, obfuscator, and preverifier."
                          "\nDashO Android & Java Obfuscator a Java, Kotlin and Android application hardening and obfuscation tool that provides passive and active protection."
                          "\nKlassMaster Heavy Duty Protection, shrinks and obfuscates both code and string constants."
                          "\n It can also translate stack traces back to readable form if you save the obfuscation log."
                          "\nJavaguard, a simple obfuscator without a lot of documentation."
                          "\nJObfuscator, Java source code obfuscator.",
            "reference": "https://owasp.org/www-community/controls/Bytecode_obfuscation"}
    elif thunder_name == "Directory Traversal":
        js = {
            "description": "Directory traversal (also known as file path traversal) is a web security vulnerability that allows an attacker to read arbitrary files on the server that is running an application.",
            "suggestion": "How to protect yourself\n"
                          "\nPrefer working without user input when using file system calls"
                          "\nUse indexes rather than actual portions of file names when templating or using language files (ie value 5 from the user submission = Czechoslovakian, rather than expecting the user to return “Czechoslovakian”)"
                          "\nEnsure the user cannot supply all parts of the path – surround it with your path code"
                          "\nValidate the user’s input by only accepting known good – do not sanitize the data",
            "reference": "https://portswigger.net/web-security/file-path-traversal"}
    elif thunder_name == "Guessing":
        js = {
            "description": "An attack in which an attacker performs repeated logon trials by guessing possible values of the authenticator output.",
            "suggestion": "The commonly known administrator page is not used."
                          "\nThe administrator's page or sensitive pages allow you to log in.",
            "reference": "https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/02-Configuration_and_Deployment_Management_Testing/05-Enumerate_Infrastructure_and_Application_Admin_Interfaces"}
    json_string = json.dumps(js)
    body = {"thunder_name": thunder_name,
            "priority": priority,
            "url": url,
            "project": project_id,
            "details" : json_string
            }
    request = requests.post(url="https://api.cumulus.tophat.cloud/thunder/create", json=body)

