from django.urls import path
from .views import MovieSearchView, GenreSearchView, LatestMoviesView, PopularMoviesView

app_name = 'movie'
urlpatterns = [
    path('search/<str:query>/', MovieSearchView.as_view(), name='search'),
    path('genre/<str:genre>/', GenreSearchView.as_view(), name='genre'),
    path('latest/', LatestMoviesView.as_view(), name='latest_movies'),
    path('popular/', PopularMoviesView.as_view(), name='popular_movies'),
]