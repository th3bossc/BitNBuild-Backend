from django.urls import path
from .views import ProfileInfo, WatchListView, HistoryView, DeleteHIstoryView, DeleteWatchListView

app_name = 'users'
urlpatterns = [
    path('profile/', ProfileInfo.as_view(), name='profile'),
    path('watchlist/', WatchListView.as_view(), name='watchlist'),
    path('history/', HistoryView.as_view(), name='history'),
    path('watchlist/delete/', DeleteWatchListView.as_view(), name='delete_watchlist'),
    path('history/delete/', DeleteHIstoryView.as_view(), name='delete_history'),
]