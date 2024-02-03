from rest_framework import serializers
from .models import User, WatchList, History


class UserSerializer(serializers.ModelSerializer):
    watchlist = serializers.SerializerMethodField()
    history = serializers.SerializerMethodField()
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'watchlist', 'history')
        read_only_fields = ('aadhar_no', 'license_no', 'vehicles')
        
    def get_history(self, obj):
        history = History.objects.filter(user=obj)
        data = HistorySerializer(history, many=True).data
        return data
    
    def get_watchlist(self, obj):
        watchlist = WatchList.objects.filter(user=obj)
        data = WatchListSerializer(watchlist, many=True).data
        return data
    
    
class WatchListSerializer(serializers.ModelSerializer):
    class Meta:
        model = WatchList
        fields = ('movie',)
        read_only_fields = ('user', 'movie')
        
class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = History
        fields = ('movie',)
        read_only_fields = ('user', 'movie')
 