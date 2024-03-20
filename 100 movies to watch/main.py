import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

# We get the response of the url

movies_response = requests.get(URL).text

soup = BeautifulSoup(movies_response, "html.parser")

# We use list comprehension to create a list of the html, and make it start from bottom to top so the movies are in
# order

movies_names = [movie_name.getText() for movie_name in soup.select(".article-title-description__text h3")][::-1]

# Put the movies in our movies.txt file

with open("movies.txt", mode="w", encoding="utf-8") as file:
    for movie in movies_names:
        file.write(f"{movie}\n")
