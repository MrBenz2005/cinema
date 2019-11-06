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
        self.LINK = "https://msk.subscity.ru/"

    def extract_raw_content(self):
        """Метод берет код страници."""
        self.content = req.get(self.LINK)
        self.soup = bf(self.content.text, 'html.parser')


    def print_raw_content(self):
        """Метод преобразовывает и выводит код страницы"""
        self.right = self.soup.prettify()
        return self.right

    def get_films_list(self):
        film = []
        self.content = req.get(self.LINK)
        self.soup = bf(self.content.text, 'html.parser')
        films = self.soup
        films= films.find_all("div", class_='movie-plate')
        for i in films:
            film.append(i["attr-title"])
        return film
        """Метод который возвращает список всех названий фильмов с главной страницы сайта."""

    def get_film_nearest_session(self):
        self.extract_raw_content()
        link = self.soup
        all_films = link.find_all("div", class_='movie-plate')
        first_film = all_films[0]
        film_link_a_tag = first_film.find_all("a")[0]
        film_page_link = film_link_a_tag["href"]
        film_page_response = req.get(self.LINK + film_page_link)
        film = film_page_response.find_all("td", class_='attr-time')
        return film


MSK_PARSER = CinemaParser('msk')
print(MSK_PARSER.get_film_nearest_session())

