# movie/views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# from .serializers import MovieSerializer
from user.serializers import MovieSerializer
from .models import Movie
import requests
from .utils import get_top_movies
from dotenv import load_dotenv
import os

load_dotenv()

class MovieSearchView(APIView):
    def get(self, request, query):
        if not query:
            return Response({'error': 'Please provide a query parameter'}, status=status.HTTP_400_BAD_REQUEST)

        url = os.environ.get('URL') + '/search/movie'
        params = {'api_key': os.environ.get('API_KEY'), 'query': query}
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

        url = os.environ.get('URL') + '/discover/movie'
        api_key = os.environ.get('API_KEY')
        genres_to_search = [genre]
        top_movies = get_top_movies(api_key, genres_to_search)
        return Response(top_movies.get(genre, []))


class LatestMoviesView(APIView):
    def get(self, request):
        url = os.environ.get('URL') + '/movie/upcoming'
        api_key = os.environ.get('API_KEY')
        params = {'api_key': api_key, 'language': 'en-US', 'page': 1}
        
        response = requests.get(url, params=params)
        # print(response.json())

        if response.status_code == 200:
            data = response.json().get('results', [])
            serializer = MovieSerializer(data=data, many=True)
            # print(data)
            if serializer.is_valid():
                return Response(serializer.data)
            else:
                return Response({'error': 'Invalid data', 'validation_errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': 'Failed to fetch latest movies from MovieDB API'}, status=response.status_code)
        


class PopularMoviesView(APIView):
    def get(self, request):
        url = os.environ.get('URL') + '/movie/popular'
        api_key = os.environ.get('API_KEY')
        params = {'api_key': api_key, 'language': 'en-US', 'page': 1}
        
        response = requests.get(url, params=params)

        if response.status_code == 200:
            data = response.json().get('results', [])
            serializer = MovieSerializer(data=data, many=True)
            
            if serializer.is_valid():
                return Response(serializer.data)
            else:
                return Response({'error': 'Invalid data', 'validation_errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': 'Failed to fetch popular movies from MovieDB API'}, status=response.status_code)
        


