import requests
import urllib3
import chardet
import time
import random
import json
from lxml import etree
from copyheaders import headers_raw_to_dict


def get_pic(keyword):
    pic_url_list = []
    headers = {"user-agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)"
                             "Chrome/67.0.3396.87 Safari/537.36"}
    first_url = f"https://www.google.com/search?&tbm=isch&q={keyword}"
    try:
        first_webdata = requests.get(first_url, headers=headers).text
        first_datas = etree.HTML(first_webdata)
        xpath_datas = first_datas.xpath("//div[@class='rg_meta notranslate']/text()")
        for data in xpath_datas:
            pic_url = json.loads(data)["ou"]
            pic_url_list.append(pic_url)
    except Exception as e:
        print(e)
    for i in range(1, 9):
        try:
            url = f"https://www.google.com/search?&q={keyword}&tbm=isch&ijn={i}&start={i*100}"
            web_data = requests.get(url, headers=headers).text
            datas = etree.HTML(web_data)
            xpath_datas = datas.xpath("//div[@class='rg_meta notranslate']/text()")
            for data in xpath_datas:
                pic_url = json.loads(data)["ou"]
                pic_url_list.append(pic_url)
        except Exception as e:
            print(e)
        time.sleep(random.randint(1, 10)/10)
    print(pic_url_list)
    pic_dict = {"关键词": keyword, "图片数量": len(pic_url_list), "图片链接列表": pic_url_list}
    with open(f"pic_google_{keyword}.txt", "w", encoding='utf-8') as f:
        f.write(json.dumps(pic_dict, ensure_ascii=False))


keyword = "汽车"
get_pic(keyword)