import requests
import json
import time
import random
import re
from lxml import etree


def get_pic(keyword):
    pic_url_list = []
    first_url = f"http://image.so.com/i?q={keyword}&src=tab_www"
    try:
        first_webdata = requests.get(first_url).text
        first_datas = etree.HTML(first_webdata)
        xpath_datas = json.loads(first_datas.xpath("//script[@id='initData']/text()")[0])
        for data in xpath_datas["list"]:
            pic_url_list.append(data["img"])
    except Exception as e:
        print(e)
    for i in range(1, 20):
        url = f"http://image.so.com/j?q={keyword}&src=tab_www&correct={keyword}&pn=60" \
              f"&ch=&sn={50+60*i}&ran=0&ras=6&cn=0&gn=0&kn=50"
        try:
            web_data = requests.get(url).text
            datas = json.loads(web_data)
            for data in datas["list"]:
                pic_url_list.append(data["img"])
        except Exception as e:
            print(e)
        time.sleep(random.randint(1, 10)/10)
    pic_dict = {"关键词": keyword, "图片数量": len(pic_url_list), "图片链接列表": pic_url_list}
    with open(f"pic_360_{keyword}.txt", "w", encoding='utf-8') as f:
        f.write(json.dumps(pic_dict, ensure_ascii=False))


if __name__ == "__main__":
    keyword = "汽车"
    get_pic(keyword)
