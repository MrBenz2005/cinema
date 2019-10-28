from bs4 import BeautifulSoup as bf
import requests as req

class CinemaParser(object):
    def __init__(self,object):
            self.city = object

    
    def extract_raw_content(self,link):
            self.content = req.get(link)
            self.soup = bf(self.content.text, 'html')


    def print_raw_content(self):
            right = self.soup.prettify()
            return right




msk_parser = CinemaParser('msk')
link = "https://msk.subscity.ru/"
msk_parser.extract_raw_content(link)
print(msk_parser.print_raw_content())