from django.urls import path
from .views import MovieSearchView, GenreSearchView

app_name = 'movie'
urlpatterns = [
    path('search/<str:query>/', MovieSearchView.as_view(), name='search'),
    path('genre/<str:genre>/', GenreSearchView.as_view(), name='genre'),
]