from django.urls import path
from . import views

urlpatterns = [
    path('', views.MoviesList.as_view(), name='movies'),
    path('movies/<int:pk>/', views.MovieDetails.as_view(), name='movie-details'),
    path('movies/create/', views.MovieCreate.as_view(), name='movie-create'),
    path('movies/<int:pk>/update/', views.MovieUpdate.as_view(), name='movie-update'),
    path('movies/<int:pk>/delete/', views.MovieDelete.as_view(), name='movie-delete'),
    path('movies/review/<int:movie_id>/', views.CreateReview.as_view(), name='review-create'),
    path('movies/genres/', views.GenreListCreate.as_view(), name='genre-list-create'),
    path('movies/genres/delete/<int:pk>/', views.GenreDelete.as_view(), name='genre-delete'),
    path('movies/genres/update/<int:pk>/', views.GenreUpdate.as_view(), name='genre-update'),
    path('movies/tags/', views.TagListCreate.as_view(), name='tag-list-create'),
    path('movies/tags/delete/<int:pk>/', views.TagDelete.as_view(), name='tag-delete'),
    path('movies/tags/update/<int:pk>/', views.TagUpdate.as_view(), name='tag-update'),
]
