from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Movie, MovieGenre, MovieTag, Review
from .forms import MovieForm, ReviewForm
from django.urls import reverse_lazy
from django.shortcuts import render, redirect

class MoviesList(ListView):
    model = Movie
    context_object_name = 'movies'
    paginate_by = 20 


class MovieDetails(DetailView):
    model = Movie
    context_object_name = 'movie'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        reviews = self.object.review_set.all()
        context.update({'review_form': ReviewForm(), 'reviews': reviews, 'reviewers': reviews.values_list('user_id', flat=True)})
        return context

class MovieCreate(CreateView):
    model = Movie
    form_class = MovieForm
    success_url = reverse_lazy('movies')

class MovieUpdate(UpdateView):
    model = Movie
    form_class = MovieForm

    def get_success_url(self):
        return reverse_lazy('movie-details', kwargs={'pk': self.object.pk})

class MovieDelete(DeleteView):
    model = Movie
    success_url = reverse_lazy('movies')


# Review Views
class CreateReview(CreateView):
    model = Review
    form_class = ReviewForm
    
    def get_success_url(self):
        return reverse_lazy('movie-details', kwargs={'pk': self.kwargs['movie_id']})
    
    def form_valid(self, form):
        form.instance.movie_id = Movie.objects.get(pk=self.kwargs['movie_id'])
        form.instance.user_id = self.request.user
        return super().form_valid(form)
    
    def form_invalid(self, form):
        movie = Movie.objects.get(pk=self.kwargs['movie_id'])
        reviews = movie.review_set.all()
        return render(self.request, 'movies/movie_detail.html', {
            'review_form': form,
            'movie': movie,
            'reviews': movie.review_set.all(),
            'reviewers': reviews.values_list('user_id', flat=True)
        })


# genre views
class GenreListCreate(CreateView):
    model = MovieGenre
    success_url = reverse_lazy('genre-list-create')
    template_name = 'movies/configuration_list_create.html'
    fields = 'name',

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs) 
        context.update({'objects': MovieGenre.objects.all(), 'configuration': 'Genres'})
        return context
    
class GenreUpdate(UpdateView):
    model = MovieGenre
    success_url = reverse_lazy('genre-list-create')
    template_name = 'movies/configuration_list_create.html'
    fields = 'name',

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context.update({'objects': MovieGenre.objects.all(), 'configuration': 'Genres'})
        return context
    
class GenreDelete(DeleteView):
    model = MovieGenre
    success_url = reverse_lazy('genre-list-create')


# tag views
class TagListCreate(CreateView):
    model = MovieTag
    success_url = reverse_lazy('tag-list-create')
    template_name = 'movies/configuration_list_create.html'
    fields = 'name',

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context.update({'objects': MovieTag.objects.all(), 'configuration': 'Tags'})
        return context

class TagUpdate(UpdateView):
    model = MovieTag
    success_url = reverse_lazy('tag-list-create')
    template_name = 'movies/configuration_list_create.html'
    fields = 'name',

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context.update({'objects': MovieTag.objects.all(), 'configuration': 'Tags'})
        return context

class TagDelete(DeleteView):
    model = MovieTag
    success_url = reverse_lazy('tag-list-create')
