import requests
import json
import time
import random


def get_pic(keyword):
    pic_url_list = []
    for i in range(1, 30):
        try:
            url = "http://pic.sogou.com/pics?query={}&policyType=1&mode=1&start={}&reqType=ajax&reqFrom=result&tn=0".format(keyword, 48*i)
            web_data = requests.get(url).text
            datas = json.loads(web_data)
            for data in datas["items"]:
                pic_url_list.append(data["pic_url_noredirect"])
        except Exception as e:
            print(e)
        time.sleep(random.randint(1, 10)/10)
    print(pic_url_list)
    pic_dict = {"关键词": keyword, "图片数量": len(pic_url_list), "图片链接列表": pic_url_list}
    with open(f"pic_sogou_{keyword}.txt", "w", encoding='utf-8') as f:
        f.write(json.dumps(pic_dict, ensure_ascii=False))


keyword = "汽车"
get_pic(keyword)
