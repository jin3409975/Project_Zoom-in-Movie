import urllib.request
import json
from django.conf import settings
import django
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'final_pjt_back.settings')
django.setup()


API_KEY = settings.API_KEY
HOST = "https://api.themoviedb.org"
MOVIE_LIST_URI = "/3/movie/popular"
MOVIE_INFO_URI = "/3/movie/"
GENRE_LIST_URI = "/3/genre/movie/list"

movie_list = []
movie_Ids = []
genre_list = []

genre_request = (f'{HOST}{GENRE_LIST_URI}?api_key={API_KEY}&language=ko')
response = urllib.request.urlopen(genre_request)
json_str = response.read().decode('utf-8')
json_object = json.loads(json_str)

genre_data = json_object.get("genres")

for data in genre_data:

    my_data = {
        "genre_id": data.get("id"),
        "genre_name": data.get("name")
    }

    my_genre = {
        "model": "movies.genre",
        "pk": my_data.get("genre_id"),
        "fields": {
            "genre_name": my_data.get("genre_name")
        },
    }
    genre_list.append(my_genre)

for i in range(1, 5):
    request = (f'{HOST}{MOVIE_LIST_URI}?api_key={API_KEY}&language=ko&page={i}')
    response = urllib.request.urlopen(request)
    json_str = response.read().decode('utf-8')
    json_object = json.loads(json_str)

    data_movies = (json_object.get("results"))

    for movie in data_movies:
        movie_Ids.append(movie.get("id"))
    
print(data_movies)

for idx, movie_Id in enumerate(movie_Ids):
    movie_request = (f'{HOST}{MOVIE_INFO_URI}{movie_Id}?api_key={API_KEY}&language=ko&')
    response = urllib.request.urlopen(movie_request)
    json_str = response.read().decode('utf-8')
    json_object = json.loads(json_str)
 
    if json_object.get("poster_path") and json_object.get("backdrop_path"):
        if json_object.get("genres"):
            
            my_object = {
                "model": "movies.movie",
                "pk": idx+1,
                "fields": {
                    "movie_id": json_object.get("id"),
                    "title": json_object.get("title"),
                    "original_title": json_object.get("original_title"),
                    "overview": json_object.get("overview"),
                    "poster_path": json_object.get("poster_path"),
                    "rating": json_object.get("vote_average"),
                    "release_date": json_object.get("release_date"),
                    "runtime": json_object.get("runtime"),
                    "popularity": json_object.get("popularity"),
                    "adult": json_object.get("adult"),
                    "backdrop_path": json_object.get("backdrop_path"),
                    "genres": [json_object.get("genres")[0].get("id")],
                }  
            }
        else:
            my_object = {
                "model": "movies.movie",
                "pk": idx+1,
                "fields": {
                    "movie_id": json_object.get("id"),
                    "title": json_object.get("title"),
                    "adult": json_object.get("adult"),
                    "popularity": json_object.get("popularity"),
                    "poster_path": json_object.get("poster_path"),
                    "release_date": json_object.get("release_date"),
                    "runtime": json_object.get("runtime"),
                    "rating": json_object.get("vote_average"),
                    "overview": json_object.get("overview"),
                    "genres": json_object.get("genres"),
                    "original_title": json_object.get("original_title"),
                    "backdrop_path": json_object.get("backdrop_path"),
                }
            }
        movie_list.append(my_object)


with open('movies/fixtures/movies.json', 'w', encoding='UTF-8') as file:
    file.write(json.dumps(movie_list, ensure_ascii=False))

with open('movies/fixtures/genres.json', 'w', encoding='UTF-8') as file:
    file.write(json.dumps(genre_list, ensure_ascii=False))


'''
movies/fixtures/ 만들고 

python init.py 

python manage.py migrate

python manage.py loaddata genres.json movies.json

'''