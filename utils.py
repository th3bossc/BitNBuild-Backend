from user.models import PreferedGenre

def get_prefered_genres(user):
        preferedGenres = PreferedGenre.objects.filter(user=user).order_by('search_count') 
        size = len(preferedGenres)
        return {
            "first" : size and preferedGenres[0].genre or None,
            "second" : (size > 1) and preferedGenres[1].genre or None,
            "third" : (size > 2) and preferedGenres[2].genre or None,
        }