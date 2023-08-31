from django.urls import path
from . import views

urlpatterns = [
    path('', views.MoviesList.as_view(), name='movies'),
    path('movies/<int:pk>/', views.MovieDetails.as_view(), name='movie-details'),
    path('movies/create/', views.MovieCreate.as_view(), name='movie-create'),
    path('movies/<int:pk>/update/', views.MovieUpdate.as_view(), name='movie-update'),
    path('movies/<int:pk>/delete/', views.MovieDelete.as_view(), name='movie-delete'),
    path('movies/genre/', views.GenreListCreate.as_view(), name='genre-list-create'),
    path('movies/genre/delete/<int:pk>/', views.GenreDelete.as_view(), name='genre-delete'),
    path('movies/genre/update/<int:pk>/', views.GenreUpdate.as_view(), name='genre-update'),
]
