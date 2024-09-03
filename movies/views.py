from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import Movie
# Create your views here.


def index(request):
    movies = Movie.objects.all()
    # movies = Movie.objects.filter(is_active=True)
    context = {
        "movies_show": movies
               }
    return render(request, 'movies/index.html', context)


def about(request):
    return render(request, 'movies/about.html', {})


def movie_detail(request, pk):
    movie_posting = get_object_or_404(Movie, pk=pk)
    context = {
        "posting": movie_posting
    }
    return render(request, "movies/details.html", context)





# for templates -> app/templates/app/index.html
# movies/templates/movies/index.html

