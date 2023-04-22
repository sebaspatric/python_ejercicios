from django.shortcuts import render
from django.views.generic import DetailView, ListView
from .models import Director, Movie


# Create your views here.

def index(request):
    return render(request,'movies/index.html')

class DirectorListView(ListView):
    model = Director

class DirectorDetailView(DetailView):
    model = Director
    template_name = 'directores/director_detail.html'

class PeliculaListView(ListView):
    model = Movie

class PeliculaDetailView(DetailView):
    model = Movie
    template_name = 'peliculas/pelicula_detail.html'
