import requests
import json

get_cast_crew_a = 'https://api.themoviedb.org/3/movie/'
get_cast_crew_b = '/credits?api_key=1ad88638edfc6353f76e904be8c2e02b&language=ko-KR'
poster_url = 'https://www.themoviedb.org/t/p/w1280'

TMDB_API_KEY = '1ad88638edfc6353f76e904be8c2e02b'
movie_ids = []

def get_movie_datas():
    global movie_ids
    total_data = []

    for i in range(1, 20):
        request_url = f"https://api.themoviedb.org/3/movie/top_rated?api_key={TMDB_API_KEY}&language=ko-KR&page={i}"
        movies = requests.get(request_url).json()

        for movie in movies['results']:
            if int(movie.get('release_date')[0:4]) >= 2010 and movie.get('backdrop_path'):
                for crew in requests.get(get_cast_crew_a + str(movie['id']) + get_cast_crew_b).json()['crew']:
                    if crew['job'] == 'Director':
                        director = crew['name']
                        break
                

                fields = {
                    # 'movie_id': movie['id'],
                    'backdrop_path': poster_url +  movie['backdrop_path'],
                    'title': movie['title'],
                    'release_date': movie['release_date'],
                    'popularity': movie['popularity'],
                    'vote_score': movie['vote_average'],
                    'vote_count': movie['vote_count'],
                    'overview': movie['overview'],
                    'poster_path': poster_url + movie['poster_path'],
                    'director' : director,
                    'genres': movie['genre_ids']
                }

                movie_ids.append(str(movie['id']))

                data = {
                    "pk": movie['id'],
                    "model": "movie.movie",
                    "fields": fields
                }

                total_data.append(data)

    with open("movie/fixtures/movie_data.json", "w", encoding="utf-8") as w:
        json.dump(total_data, w, indent=4, ensure_ascii=False)

def get_genre_data():
    total_data = []

    request_url = f"https://api.themoviedb.org/3/genre/movie/list?api_key={TMDB_API_KEY}&language=ko-KR"
    genres = requests.get(request_url).json()

    for genre in genres['genres']:
        fields = {
            # 'genre_id': genre['id'],
            'name': genre['name'],
        }

        data = {
            "pk": genre['id'],
            "model": "movie.genre",
            "fields": fields
        }
        total_data.append(data)

    with open("movie/fixtures/genre_data.json", "w", encoding="utf-8") as w:
        json.dump(total_data, w, indent=4, ensure_ascii=False)

def get_actor_data(movie_ids):
    register = []
    total_data = []
    cnt = 0
    for movie_id in movie_ids:
        request_url = get_cast_crew_a + movie_id + get_cast_crew_b
        actors = requests.get(request_url).json()['cast'][0:5]
        incnt = 0
        for actor in actors:
            if incnt > 5:
                break
            if actor['name'] not in register:
                register.append(actor['name'])
                fields = {
                    'movie': movie_id,
                    'name': actor['name']
                }
                data = {
                    "pk": cnt,
                    "model": "movie.actor",
                    "fields": fields
                }
                cnt += 1
                incnt += 1
                total_data.append(data)
    
    with open("movie/fixtures/actor_data.json", "w", encoding="utf-8") as w:
        json.dump(total_data, w, indent=4, ensure_ascii=False)


get_movie_datas()
# get_genre_data()
get_actor_data(movie_ids)