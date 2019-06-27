'''
批量增加岗位
岗位名即自增的整数
'''
import requests


def create_position():
    data = {
        "request": {
            "c": "",
            "m": "",
            "p": {
                "session": "eyJmcm9tIjoiQiIsInNyY19pZCI6MSwibWFuYWdlcl9pZCI6ODAsImNvbXBhbnlfaW****gwLCJ1c2VyX2lkIjo3NCwiZXhwaXJlIjoxNTYyMTU2NTA0LCJzaWduYXR1cmUiOiJiM2U5ZWZhMmIzMzIwN2M3ZWI1ZjRjMGEyMTdiYmMxZjhlMzIzNDdiIiwidXNlcl90eXBlIjoxfQ==",
                "name": i
            }
        }
    }

    url = 'https://bot.****.ifchange.com/api/dhr_manager/positions/create'
    r = requests.post(url, json=data, verify=False)   #verify=False不一定需要
    print(r.text)


for i in range(1, 1001):
    create_position()
