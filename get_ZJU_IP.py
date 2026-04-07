import requests
import json
import time
import random

# please use python environment with requests module installed, and set your ServerChan3 URL below
push_url = "<YOUR_SERVER_CHAN3_URL>"
check_url = "https://zjuwlan.intl.zju.edu.cn/cgi-bin/rad_user_info?"

def sc_send(title, desp='', tags=''):
    params = {
        'title': title,
        'desp': desp,
        'tags': tags
    }
    headers = {
        'Content-Type': 'application/json;charset=utf-8'
    }
    response = requests.post(url=push_url, json=params, headers=headers)
    result = response.json()
    return result


if __name__ == "__main__":
    ip = ""
    for _ in range(20):
        try:
            response = requests.get(check_url,params={
                "callback": "jQuery" + str(random.randint(1, 1234567890123456789012)) + "_" + str(int(time.time() * 1000)),
                "_": int(time.time() * 1000),
            })
            data = json.loads(response.text[response.text.find("(") + 1:response.text.rfind(")")])
            ip = data.get("online_ip")
            if ip != "":
                break
            time.sleep(2)
        except Exception as e:
            print("Error:", e)
            time.sleep(5)
            continue
    sc_send("Lab's ZJU IPs @ " + time.strftime("%Y-%m-%d %H:%M:%S"), ip,tags="LAB|IP")
    
        
