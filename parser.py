from bs4 import BeautifulSoup
import requests
import openpyxl

class Rating:
    def __init__(self, number, movie_title, rating, date):
        self.number = number
        self.movie_title = movie_title
        self.rating = rating
        self.date = date

def get_user_ratings(user_id):

    user_url = f'https://www.kinopoisk.ru/user/{user_id}/votes/'
    response = requests.get(user_url)
    response.raise_for_status()  # Обработка ошибок HTTP

    soup = BeautifulSoup(response.content, 'html.parser')

    # Находим все элементы с оценками фильмов
    table = soup.find('div', class_='profileFilmsList')
    entries = table.find_all('div', class_='item')

    ratings = []
    for entry in entries:
        number = entry.find('div', class_='num').text.strip()
        movie_title = entry.find('div', class_='nameRus').text.strip()
        rating = entry.find('div', class_='vote').text.strip()
        date = entry.find('div', class_='date').text
        # Добавляем новую пару ключ-значение
        ratings.append(Rating(number, movie_title, rating, date))

    return ratings

#Запись и сохранение данных в Excel
def save_data_to_excel(data, filename):
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.append(['№','Название фильма', 'Рейтинг', 'Дата и время оценки'])
    for rating in data:
        ws.append([rating.number, rating.movie_title, rating.rating, rating.date])
    wb.save(filename)