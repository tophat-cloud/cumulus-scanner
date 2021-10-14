
def request_thunder(thunder_name, project_id, body, url, priority):
    
    body = {"thunder_name": thunder_name,
            "priority": priority,
            "url": url,
            "project": project_id,
            "details" : body
            }
    request = requests.post(url="https://api.cumulus.tophat.cloud/thunder/create", json=body)

