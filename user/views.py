from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer, WatchListSerializer, HistorySerializer
from .models import WatchListView, HistoryView
import requests

# ProfileInfo, WatchList, History
# Create your views here.


class ProfileInfo(APIView):
    def get(self, request):
        user = request.user
        serializer = UserSerializer(user)
        return Response(serializer.data)

class WatchListView(APIView):
    def get(self, request):
        user = request.user
        watchlist = WatchListView.objects.filter(user=user)
        serializer = WatchListSerializer(watchlist, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        user = request.user
        movie = request.data['movie']
        watchlist = WatchListView.objects.create(user=user, movie=movie)
        watchlist.save()
        serializer = WatchListSerializer(watchlist)
        return Response(serializer.data)
    
class DeleteWatchListView(APIView):
    def delete(self, request):
        user = request.user
        movie = request.data['movie']
        watchlist = WatchListView.objects.filter(user=user, movie=movie)
        watchlist.delete()
        return Response('Deleted')
    

class HistoryView(APIView):
    def get(self, request):
        user = request.user
        history = HistoryView.objects.filter(user=user)
        serializer = HistorySerializer(history, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        user = request.user
        movie = request.data['movie']
        history = HistoryView.objects.create(user=user, movie=movie)
        history.save()
        serializer = HistorySerializer(history)
        return Response(serializer.data)


class DeleteHIstoryView(APIView):
    def delete(self, request):
        user = request.user
        movie = request.data['movie']
        history = HistoryView.objects.filter(user=user, movie=movie)
        history.delete()
        return Response('Deleted')
    

