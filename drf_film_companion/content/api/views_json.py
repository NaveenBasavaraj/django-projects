from content.models import Movie
from django.http import JsonResponse

def movie_list(request):
    movies = Movie.objects.all()
    data = {
        'movies':list(movies.values())
    }
    return JsonResponse(data)

def movie_details(request, pk):
    movie = Movie.objects.get(id=pk)
    data = {
        'movie':movie.title,
        'description':movie.description,
        'active':movie.active
    }
    return JsonResponse(data)