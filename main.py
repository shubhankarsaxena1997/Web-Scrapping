from bs4 import BeautifulSoup
import requests

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
web_page_content = response.text
soup = BeautifulSoup(web_page_content, "html.parser")
all_movies = soup.find_all(name="h3", class_="title")
movies_name = []

for single_title in all_movies:
    movie_name = single_title.text
    movies_name.append(movie_name)

movies_name.reverse()

with open("movies.txt", "w") as file:
    for single_movie in movies_name:
        content = file.write("%s\n" % single_movie)
        
        
        
# this project will fetch the top 100 movuies all time from website www.empireonline.com and store it in a text file 
