from django.urls import path
from . import views

urlpatterns = [
    path('', views.movie_views.MoviesList.as_view(), name='movies'),
    path('movies/<int:pk>/', views.movie_views.MovieDetails.as_view(), name='movie-details'),
    path('movies/create/', views.movie_views.MovieCreate.as_view(), name='movie-create'),
    path('movies/<int:pk>/update/', views.movie_views.MovieUpdate.as_view(), name='movie-update'),
    path('movies/<int:pk>/delete/', views.movie_views.MovieDelete.as_view(), name='movie-delete'),
    path('movies/review/<int:movie_id>/', views.review_views.CreateReview.as_view(), name='review-create'),
    path('movies/review/<int:movie_id>/<int:pk>', views.review_views.DeleteReview.as_view(), name='review-delete'),
    path('movies/genres/', views.genre_views.GenreListCreate.as_view(), name='genre-list-create'),
    path('movies/genres/delete/<int:pk>/', views.genre_views.GenreDelete.as_view(), name='genre-delete'),
    path('movies/genres/update/<int:pk>/', views.genre_views.GenreUpdate.as_view(), name='genre-update'),
    path('movies/tags/', views.tag_views.TagListCreate.as_view(), name='tag-list-create'),
    path('movies/tags/delete/<int:pk>/', views.tag_views.TagDelete.as_view(), name='tag-delete'),
    path('movies/tags/update/<int:pk>/', views.tag_views.TagUpdate.as_view(), name='tag-update'),
]
