import urllib.request
from pandas import DataFrame
from bs4 import BeautifulSoup

html = urllib.request.urlopen('http://movie.naver.com/movie/sdb/rank/rmovie.nhn')
soup = BeautifulSoup(html,'html.parser')

tags = soup.findAll('div', attrs={'class':'tit3'})
tags_range = soup.findAll('td', attrs={'class':'range ac'})

name = []
for tags_list in tags:
    name_list = list(tags_list.strings)
    movie_name = name_list[1]
    name.append([movie_name])

number = []
for movie_number in tags_range:
    movie_number = list(movie_number)
    movie_range = movie_number[0]
    number.append([movie_range])

ranking_list = []
for j in range(len(name)):
    ranking_list.append([j+1]+name[j]+number[j])

movie_table = DataFrame(ranking_list, columns = ('순위','영화명','변동폭'))
movie_table.to_csv("movie.csv",encoding="cp949",mode='w',index=False)

print("End")