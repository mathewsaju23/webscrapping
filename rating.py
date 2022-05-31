from numpy import source
import pandas as pd
from bs4 import BeautifulSoup
import requests
import openpyxl
excel = openpyxl.Workbook()
sheet = excel.active
sheet.title = 'topmovies'
print(excel.sheetnames)
sheet.append(['Rank', 'Name', 'Year', 'Rating'])

try:
    source = requests.get("https://www.imdb.com/chart/top/")
    source.raise_for_status()
    soup = BeautifulSoup(source.text, "lxml")
    movies = soup.find('tbody', class_="lister-list").find_all('tr')
    # print(len(movies))
    for movie in movies:
        name = movie.find('td', class_="titleColumn").a.text
        rank = movie.find('td', class_="titleColumn").get_text(
            strip=True).split('.')[0]
        year = movie.find('td', class_="titleColumn").span.text.strip('()')
        rating = movie.find('td', class_="ratingColumn").strong.text
        sheet.append([rank, name, year, rating])

except Exception as e:
    print(e)
excel.save('movieratings.xlsx')
