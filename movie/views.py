# movie/views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import MovieSerializer
from .models import Movie
import requests
from .utils import get_top_movies

class MovieSearchView(APIView):
    def get(self, request, query):
        if not query:
            return Response({'error': 'Please provide a query parameter'}, status=status.HTTP_400_BAD_REQUEST)

        api_key = 'd75594ae2460bc105fa1ebbf86900cfb'
        url = f'https://api.themoviedb.org/3/search/movie'
        params = {'api_key': api_key, 'query': query}
        response = requests.get(url, params=params)

        if response.status_code == 200:
            data = response.json().get('results', [])
            cleaned_data = [entry for entry in data if entry.get('overview') and entry.get('release_date')]
            serializer = MovieSerializer(data=cleaned_data, many=True)
            if serializer.is_valid():
                return Response(serializer.data)
            else:
                return Response({'error': 'Invalid data', 'validation_errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': 'Failed to fetch data from MovieDB API'}, status=response.status_code)

class GenreSearchView(APIView):
    def post(self, request, genre):
        if not genre:
            return Response({'error': 'Please provide a genre in the request data'}, status=status.HTTP_400_BAD_REQUEST)

        api_key = 'your_tmdb_api_key'
        genres_to_search = [genre]
        top_movies = get_top_movies(api_key, genres_to_search)
        print(top_movies)
        return Response(top_movies.get(genre, []))
