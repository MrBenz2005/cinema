from bs4 import BeautifulSoup as bf
import requests as req

class CinemaParser(object):
    def __init__(self):
            self.city = object

    
    def extract_raw_content(self,link):
            self.content = req.get("https://msk.subscity.ru/")
            self.soup = BeautifulSoup(self.content.text, 'lxml')


    def print_raw_content(self):
            right = self.soup.prettify()
            return right




spb_parser = CinemaParser('spb')
msk_parser = CinemaParser()