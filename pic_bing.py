import requests
import time
import json
import random
from lxml import etree
from copyheaders import headers_raw_to_dict


def get_pic(keyword):
    pic_url_list = []
    to_headers = b"""
    accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
    accept-encoding: gzip, deflate, br
    accept-language: zh-CN,zh;q=0.9
    cache-control: max-age=0
    upgrade-insecure-requests: 1
    user-agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36
    """
    headers = headers_raw_to_dict(to_headers)
    first_url = f"https://cn.bing.com/images/search?q={keyword}"
    try:
        first_webdata = requests.get(first_url, headers=headers).text
        first_datas = etree.HTML(first_webdata)
        xpath_datas = first_datas.xpath("//a[@class='iusc']/@href")
        for data in xpath_datas:
            img_url = "https://cn.bing.com" + data
            pic_url_list.append(img_url)
    except Exception as e:
        print(e)
    for i in range(1, 30):
        try:
            url = "https://cn.bing.com/images/async?q=%E6%B1%BD%E8%BD%A6&first=71&count=35&relp=35&lostate=r&mmasync=1"
            web_data = requests.get(url, headers=headers).text
            datas = etree.HTML(web_data)
            xpath_datas = datas.xpath("//a[@class='iusc']/@href")
            for url in xpath_datas:
                img_url = "https://cn.bing.com" + url
                pic_url_list.append(img_url)
        except Exception as e:
            print(e)
        time.sleep(random.randint(1, 10) / 10)
    print(pic_url_list)
    pic_dict = {"关键词": keyword, "图片数量": len(pic_url_list), "图片链接列表": pic_url_list}
    with open(f"pic_bing_{keyword}.txt", "w", encoding='utf-8') as f:
        f.write(json.dumps(pic_dict, ensure_ascii=False))


keyword = "汽车"
get_pic(keyword)