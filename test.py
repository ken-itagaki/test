from bs4 import BeautifulSoup
import requests
from lxml import html
import mechanicalsoup

url_list = ["https://www.python.jp/",
            "https://www.ruby-lang.org/ja/",
            "https://github.com/login"]

a=0
username = "ken-itagaki"
password = "Kenken99ken"

for url in url_list:
    
    response = requests.get(url)

    tree = html.fromstring(response.content)

    if url == "https://www.python.jp/":

        text = tree.xpath('//*[@id="content-base"]/div/div/div[2]/div[1]/div/div[1]/h2/text()')[0]
        if text != "Python3 ドキュメント":
            print("コンフルの値1 is wrong")
            a=1

        text = tree.xpath('//*[@id="1geNZn"]/a[1]/text()')[0]
        if text != "Discordサーバ":
            print("コンフルの値2 is wrong")
            a=1
        
    
    elif url == "https://www.ruby-lang.org/ja/":

        text = tree.xpath('//*[@id="sidebar"]/div[1]/h3/strong/text()')[0]
        if text !=  "はじめよう!":
            print("コンフルの値3 is wrong")
            a=1

        text = tree.xpath('//*[@id="content"]/div[2]/p[1]/text()')[0]
        if text !=  "Ruby 3.1.4 がリリースされました。":
            print(url, "コンフルの値4 is wrong")
            a=1

    elif url == "https://github.com/login":

        page_url = "https://github.com/settings/profile"
        browser = mechanicalsoup.Browser()

        login_page = browser.get("https://github.com/login")

        login_form = login_page.soup.select("form")[0]
        username_field = login_form.select("#login_field")[0]
        password_field = login_form.select("#password")[0]
        username_field["value"] = username
        password_field["value"] = password

        browser.submit(login_form, login_page.url)

        response = requests.get(page_url)
        soup = BeautifulSoup(response.content, "html.parser")
        text = soup.get_text()
        #tree = html.fromstring(response.content)
        #text = tree.xpath('/html/body/div[1]/div[6]/main/div/div[1]/div/div/h1/a/text()')[0]
        print(text)


if a == 0:
    print("ok")