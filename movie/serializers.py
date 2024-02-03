from rest_framework import serializers
from .models import Movie
from dotenv import load_dotenv
import requests
import os

load_dotenv()

url = os.environ.get('URL')
token = os.environ.get('ACCESS_TOKEN')
api_key = os.environ.get("API_KEY")
headers = {
    "accept": "application/json",
    "Authorization" : "Bearer " + token,
}

class MovieSerializer(serializers.Serializer):
    title = serializers.CharField()
    overview = serializers.CharField(allow_blank=True)  
    release_date = serializers.DateField(format='%Y-%m-%d', required=False)  