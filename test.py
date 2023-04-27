from bs4 import BeautifulSoup
import requests
from lxml import html

url_list = ["https://www.python.jp/",
            "https://www.ruby-lang.org/ja/"]

for url in url_list:
    
    response = requests.get(url)

    tree = html.fromstring(response.content)

    if url == "https://www.python.jp/":

        text = tree.xpath('//*[@id="content-base"]/div/div/div[2]/div[1]/div/div[1]/h2/text()')[0]
        print(text)
        if text != "Python3 ドキュメント":
            print("コンフルの値1 is wrong")

        text = tree.xpath('//*[@id="1geNZn"]/a[1]/text()')[0]
        print(text)
        if text != "Discordサーバ":
            print("コンフルの値2 is wrong")
        
    
    elif url == "https://www.ruby-lang.org/ja/":

        text = tree.xpath('//*[@id="sidebar"]/div[1]/h3/strong/text()')[0]
        print(text)
        if text !=  "はじめよう!":
            print("コンフルの値3 is wrong")

        text = tree.xpath('//*[@id="content"]/div[2]/p[1]/text()')[0]
        if text !=  "コンフルの値":
            print("コンフルの値4 is wrong")