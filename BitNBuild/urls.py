"""
URL configuration for BitNBuild project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

admin.site.site_header = 'BitnBuild Admin Portal'
admin.site.site_title = 'Admin Portal'
admin.site.index_title = 'Welcome to BitNBuild Portal'


urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('user.urls', namespace='users')),
    path('movie/', include('movie.urls', namespace='movies')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'), # new
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]