from django.urls import path

from .views import index, DirectorListView, DirectorDetailView, PeliculaListView, PeliculaDetailView

urlpatterns = [
    path('', index, name='index'),
    path('peliculas/', PeliculaListView.as_view(), name='pelicula_list'),
    path('peliculas/<pk>', PeliculaDetailView.as_view(), name='pelicula_detail'),
    path('directores/', DirectorListView.as_view(), name='director_list'),
    path('directores/<pk>', DirectorDetailView.as_view(), name='director_detail'),
]
'''
urlpatterns = [
  path('', index, name='index'),
  path('<pk>', views.DirectorView.as_view(), name='detalle_director'),
  path('pelicula/<pk>', views.PeliculaView.as_view(), name='detalle_pelicula'),
]

'''
