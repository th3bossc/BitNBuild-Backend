from rest_framework import serializers
from .models import User, WatchListView, HistoryView
import requests
import os
from dotenv import load_dotenv

load_dotenv()

url = os.environ.get('URL')
token = os.environ.get('ACCESS_TOKEN')
api_key = os.environ.get("API_KEY")
headers = {
    "accept": "application/json",
    "Authorization" : "Bearer " + token,
}


class GenreSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=100)
    

class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    adult = serializers.BooleanField()
    title = serializers.CharField(max_length=100)
    original_language= serializers.CharField(max_length=100)
    poster_path = serializers.CharField(max_length=100)
    genres = serializers.ListField(child=GenreSerializer())
    popularity = serializers.FloatField()
    release_date = serializers.DateField(format='%Y-%m-%d', required=False)
    overview = serializers.CharField(max_length=1000)
    
    

class UserSerializer(serializers.ModelSerializer):
    watchlist = serializers.SerializerMethodField()
    history = serializers.SerializerMethodField()
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'watchlist', 'history')
        read_only_fields = ('aadhar_no', 'license_no', 'vehicles')
        
    def get_history(self, obj):
        history = HistoryView.objects.filter(user=obj)
        movies = []
        for movie in history:
            response = requests.get(f"{url}/find/{movie.movie}", headers=headers)
            movies.append(response.json())
            
        data = MovieSerializer(movies, many=True).data
        return data
    
    def get_watchlist(self, obj):
        watchlist = WatchListView.objects.filter(user=obj)
        movies = []
        for movie in watchlist:
            response = requests.get(f"{url}/find/{movie.movie}", headers=headers)
            movies.append(response.json())
        data = MovieSerializer(movies, many=True).data
        return data
    
    
class WatchListSerializer(serializers.ModelSerializer):
    movie_details = serializers.SerializerMethodField()
    class Meta:
        model = WatchListView
        fields = ('movie_details',)
        read_only_fields = ('user', 'movie')
        
    def get_movie_details(self, obj):
        response = requests.get(f"{url}/movie/{obj.movie}", headers=headers)
        return MovieSerializer(response.json())
        
class HistorySerializer(serializers.ModelSerializer):
    movie_details = serializers.SerializerMethodField()
    class Meta:
        model = HistoryView
        fields = ('movie',)
        read_only_fields = ('user', 'movie')
        
    def get_movie_details(self, obj):
        response = requests.get(f"{url}/movie/{obj.movie}", headers=headers)
        return MovieSerializer(response.json())
 