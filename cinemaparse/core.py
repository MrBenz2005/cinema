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
        self.soup = bf(self.content.text, 'html.parser')


    def print_raw_content(self):
        """Метод преобразовывает и выводит код страницы"""
        self.right = self.soup.prettify()
        return self.right

    def get_films_list(self,link):
        film = []
        self.content = req.get(link)
        self.soup = bf(self.content.text, 'html.parser')
        films = self.soup
        films= films.find_all("div", class_='movie-plate')
        for i in films:
            film.append(i["attr-title"])
        return film
        """Метод который возвращает список всех названий фильмов с главной страницы сайта."""


MSK_PARSER = CinemaParser('msk')
LINK = "https://msk.subscity.ru/"
MSK_PARSER.extract_raw_content(LINK)
print(MSK_PARSER.get_films_list(LINK))
