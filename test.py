import mechanicalsoup

# 検索キーワードを入力する
id_name = "itagaki-k"
passcode1 = "Dwub7743?"
# Google検索ページにアクセスする
browser = mechanicalsoup.StatefulBrowser()
browser.open("https://sso.i.meitec.com/sso/UI/Login?service=DesktopSSO_login&goto=https%3A%2F%2Fportal.i.meitec.com%3A443%2Fgroup%2Ffiels%2FHOME")

# 検索フォームにキーワードを入力して検索する
id = browser.select_form()
id["IDToken1"] = id_name
passcode = browser.select_form()
passcode["IDToken2"] = passcode1
browser.submit_selected()

# 検索結果のタイトルとURLを取得する
for link in browser.links():
    print(link.text)
