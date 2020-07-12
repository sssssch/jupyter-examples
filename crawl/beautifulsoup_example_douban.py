# -*-coding:utf-8-*-
# --*-- coding: utf-8 --*--
# from Bilibili
import requests
from bs4 import BeautifulSoup


class Douban:

    def __init__(self):
        self.URL = 'https://movie.douban.com/top250'
        self.start_num = []
        for start_num in range(0, 251, 25):
            self.start_num.append(start_num)
        self.header = {
            "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"

        }

    def get_top250(self):
        for start in self.start_num:
            start = str(start)
            html = requests.get(
                self.URL,
                params={
                    'start': start},
                headers=self.header)
            soup = BeautifulSoup(html.text, 'html.parser')
            names = soup.select(
                '#content > div > div.article > ol > li > div > div.info > div.hd > a > span:nth-child(1)')
            for name in names:
                print(name.get_text())


if __name__ == '__main__':
    cls = Douban()
    cls.get_top250()
