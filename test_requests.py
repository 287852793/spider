#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/6/6 15:36
# @Author  : pyf
# @File    : test.py
# @Description : scrape test
import requests
from bs4 import BeautifulSoup

# response = requests.get("http://books.toscrape.com")
res = []
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 Core/1.94.199.400 QQBrowser/11.8.5300.400"
}
for start in range(0, 250, 25):
    response = requests.get(f'https://movie.douban.com/top250?start={start}', headers=headers)
    if response.ok:
        content = response.text
        # print(content)
        soup = BeautifulSoup(content, "html.parser")

        all_titles = soup.findAll('span', attrs={"class": "title"})
        for title in all_titles:
            title_string = title.string
            if "/" not in title_string:
                # print(title_string)
                res.append(title_string)
    else:
        print(response.status_code)

for i in range(0, len(res)):
    print(res[i], end="\t")
    if i % 10 == 0:
        print("")
print("")
print("共：" + str(len(res)))
