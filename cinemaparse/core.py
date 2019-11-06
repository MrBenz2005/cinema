# some_module.py
"""Этот модуль содержит классы CinemaParser."""
from bs4 import BeautifulSoup as bf
import requests as req


class CinemaParser:
    """Класс, выполняющий действия над сайтами."""
    def __init__(self, city):
        """Город"""
        self.spicok = []
        self.town = city
        self.content = None
        self.soup = None
        self.LINK = "https://msk.subscity.ru/"

    def minimum(self, list):
        x = None
        a = 1
        for i in range(len(list)):
            if i == 0:
                x = list[i]
            if list[i] < x:
                x = list[i]
                a = i
        return a

    def extract_raw_content(self):
        """Метод берет код страници."""
        self.content = req.get(self.LINK)
        self.soup = bf(self.content.text, 'html.parser')


    def print_raw_content(self):
        """Метод преобразовывает и выводит код страницы"""
        self.right = self.soup.prettify()
        return self.right

    def get_films_list(self):
        self.films = []
        self.content = req.get(self.LINK)
        self.soup = bf(self.content.text, 'html.parser')
        film = self.soup
        film= film.find_all("div", class_='movie-plate')
        for i in film:
            self.films.append(i["attr-title"])
        return self.films

        """Метод который возвращает список всех названий фильмов с главной страницы сайта."""

    def get_film_nearest_session(self,name):
        self.extract_raw_content()
        self.get_films_list()
        for i in range(len(self.films)):
            if self.films[i] == name:
                x = i
                break
        link = self.soup
        all_films = link.find_all("div", class_='movie-plate')
        first_film = all_films[x]
        film_link_a_tag = first_film.find_all("a")[0]
        film_page_link = film_link_a_tag["href"]
        film_page_response = req.get(self.LINK + film_page_link)
        film_page_response = bf(film_page_response.text, 'html.parser')
        film1 = film_page_response.find_all("div", class_="cinema-name")
        film = film_page_response.find_all("td", class_="text-center cell-screenings")
        for j in film:
            self.spicok.append(j["attr-time"])
        b = min(self.spicok)
        print(b)
        c = self.minimum(self.spicok)
        print(c)
        self.spicok.clear()
        for item in film1:
            item1 = item.text
            self.spicok.append(item1)


        return self.spicok


MSK_PARSER = CinemaParser('msk')
a = 'Арахисовый сокол'
b = 'Zомбилэнд: Контрольный выстрел'
c = 'Бойцовский клуб'
print(MSK_PARSER.get_film_nearest_session(b))
