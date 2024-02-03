from user.models import PreferedGenre
import requests
from typing import List


def get_prefered_genres(user):
        preferedGenres = PreferedGenre.objects.filter(user=user).order_by('search_count') 
        size = len(preferedGenres)
        return {
            "first" : size and preferedGenres[0].genre or None,
            "second" : (size > 1) and preferedGenres[1].genre or None,
            "third" : (size > 2) and preferedGenres[2].genre or None,
        }

def get_top_movies(api_key: str, genres: List[str]) -> dict:
    top_movies_by_genre = {}
    for genre in genres:
        url = f'https://api.themoviedb.org/3/discover/movie'
        print(genre)
        params = {
            'api_key': api_key,
            'with_genres': get_gid(api_key, genre),
            'sort_by': 'popularity.desc',
            'page': 1,
            'language': 'en-US',
        }

        response = requests.get(url, params=params)
        print(response)
        if response.status_code == 200:
            movies = response.json().get('results', [])[:10]
            top_movies_by_genre[genre] = movies
        else:
            top_movies_by_genre[genre] = {'error': f'Failed to fetch data for genre: {genre}'}
    print(top_movies_by_genre)
    return top_movies_by_genre

def get_gid(api_key: str, genre_name: str) -> int:
    url = f'https://api.themoviedb.org/3/genre/movie/list'
    params = {'api_key': api_key, 'language': 'en-US'}
    response = requests.get(url, params=params)
    if response.status_code == 200:
        genres = response.json().get('genres', [])
        print(genres)
        for genre in genres:
            if genre['name'] == genre_name:
                print(genre['name'], genre['id'])
                return genre['id']
    return -1
