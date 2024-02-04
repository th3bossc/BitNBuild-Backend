import requests
from typing import List

def get_top_movies_by_genres(api_key: str, genres: List[str]) -> dict:
    top_movies_by_genre = {}
    for genre in genres:
        print(genre)
        url = f'https://api.themoviedb.org/3/discover/movie'
        params = {
            'api_key': api_key,
            'with_genres': get_genre_id(api_key, genre),
            'sort_by': 'popularity.desc',
            'page': 1,
            'language': 'en-US',
        }
        response = requests.get(url, params=params)
        if response.status_code == 200:
            movies = response.json().get('results', [])[:10]
            top_movies_by_genre[genre] = movies
        else:
            top_movies_by_genre[genre] = {'error': f'Failed to fetch data for genre: {genre}'}

    return top_movies_by_genre

def get_genre_id(api_key: str, genre_name: str) -> int:
    url = f'https://api.themoviedb.org/3/genre/movie/list'
    params = {'api_key': api_key, 'language': 'en-US'}
    response = requests.get(url, params=params)

    if response.status_code == 200:
        genres = response.json().get('genres', [])
        for genre in genres:
            if genre['name'] == genre_name:
                return genre['id']

    return -1

api_key = 'd75594ae2460bc105fa1ebbf86900cfb'
genres_to_search = ['Action', 'Comedy', 'Drama']
result = get_top_movies_by_genres(api_key, genres_to_search)

for genre, movies in result.items():
    if 'error' in movies:
        print(f'Error: {movies["error"]}')
    else:
        for movie in movies:
            print(f'- {movie["title"]}')
    print('\n')
