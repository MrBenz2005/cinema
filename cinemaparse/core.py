# some_module.py
"""Этот модуль содержит классы CinemaParser."""
from bs4 import BeautifulSoup as bf
import requests as req
class CinemaParser:
    """Класс, выполняющий действия над сайтами."""
    def __init__(self, city):
        """Город"""
        self.town = city
        self.content = None
        self.soup = None

    def extract_raw_content(self, link):
        """Метод берет код страници."""
        self.content = req.get(link)
        self.soup = bf(self.content.text, 'html')


    def print_raw_content(self):
        """Метод преобразовывает и выводит код страницы"""
        right = self.soup.prettify()
        return right

    def get_films_list():
        """Метод который возвращает список всех названий фильмов с главной страницы сайта."""


MSK_PARSER = CinemaParser('msk')
LINK = "https://msk.subscity.ru/"
MSK_PARSER.extract_raw_content(LINK)
print(MSK_PARSER.print_raw_content())
