# -*- coding:utf-8
import requests
from html.parser import HTMLParser
import os
from user import Users
class KifParser(HTMLParser):

    def __init__(self):
        HTMLParser.__init__(self)
        self.links = []
        self.url = ""
        self.text = ""

    def handle_starttag(self, tag, attrs): # 開始タグを見つけた場合の処理
        if tag == "a":          # タグ、属性名は全て小文字
            attrs = dict(attrs) # ((属性名, 値), ...) => {属性名:値, ...}
            if "href" in attrs:
                self.url = attrs["href"]

    def handle_endtag(self, tag): # 終了タグを見つけた場合の処理
        if tag == "a":
            if self.text:
                self.links.append((self.url, self.text))
            self.url = self.text = ""

    def handle_data(self, data): # 開始・終了タグに囲まれた中身の処理
        if self.url:
            self.text += data

def get_kif():
    login_url = "http://web.shogidojo.net/kifu/srv/login"
    kifs_url = "http://web.shogidojo.net/kifu/srv/search"

    if not os.path.exists("user_pass.json"):
        pass
    else:
        users = Users().get_users()
        for user, password in users.items():

            response = requests.post(login_url, data={'name':user,'pwd':password})
            cook = response.cookies
            kif_file_list = requests.post(kifs_url, cookies=cook.get_dict(), data={'from_date':'2000-1-1',"to_date":"2030-1-1","sub":"a"})
            response.text
            parser = KifParser()
            parser.feed(kif_file_list.text)
            parser.close()

            for kif_url, filename in parser.links:
                if not os.path.exists("static/kif"):
                    os.mkdir("static/kif")
                f = open("./static/kif/"+filename+'.kif', 'w')
                kif_file = requests.post(kif_url, cookies=cook.get_dict())
                f.write(kif_file.text)
                f.close()
