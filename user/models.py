from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
# Create your models here.

class CustomAccountManager(BaseUserManager):
    def create_superuser(self, first_name, last_name, email, password, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)
        
        if other_fields.get('is_staff') is not True:
            raise ValueError('Superuser must be assigned to is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must be assigned to is_superuser=True.')
        
        return self.create_user(first_name, last_name, email, password, **other_fields)
    
    def create_user(self, first_name, last_name, email, password, **other_fields):
        if email is None:
            raise ValueError('Users must have an email address')
        email = self.normalize_email(email)
        user = self.model(first_name=first_name, last_name=last_name, email=email, **other_fields)
        user.set_password(password)
        user.save()
        return user
    
    
class User(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    start_date = models.DateTimeField(default=timezone.now)
    email = models.EmailField(_("Email address"), blank=True, unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    objects = CustomAccountManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']
    
    def get_full_name(self):
        return self.first_name + ' ' + self.last_name
    
    def get_short_name(self):
        return self.first_name
    
    class Meta:
        db_table = 'user'
        verbose_name = 'user'
        verbose_name_plural = 'users'
        
        
class WatchListView(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.CharField(max_length=100)
    
    class Meta:
        db_table = 'watchlist'
        verbose_name = 'watchlist'
        verbose_name_plural = 'watchlists'

class HistoryView(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.CharField(max_length=100)
    
    class Meta:
        db_table = 'history'
        verbose_name = 'history'
        verbose_name_plural = 'histories'
        
class PreferedGenre(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    genre = models.CharField(max_length=100) # genreId
    search_count = models.IntegerField(default=0)
    
    class Meta:
        db_table = 'prefered_genre'
        verbose_name = 'prefered_genre'
        verbose_name_plural = 'prefered_genres'