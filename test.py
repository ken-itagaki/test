from bs4 import BeautifulSoup
import requests

url_list = ["https://url1", 
            "https://url2", 
            "https://url3"]

for url in url_list:
    
    response = requests.get(url)

    soup = BeautifulSoup(response.content, "html.parser")

    if url == "https://url1":

        text = soup.select('コンフルの値のパス/text()')[0]
        if text != "コンフルの値":
            print("コンフルの値 is wrong")

        text = soup.select('コンフルの値のパス/text()')[0]
        if text != "コンフルの値":
            print("コンフルの値 is wrong")
        
    
    elif url == "https://url2":

        text = soup.select('コンフルの値のパス/text()')[0]
        if text !=  "コンフルの値":
            print("コンフルの値 is wrong")

        text = soup.select('コンフルの値のパス/text()')[0]
        if text !=  "コンフルの値":
            print("コンフルの値 is wrong")