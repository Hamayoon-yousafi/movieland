from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Movie, MovieGenre
from .forms import MovieForm
from django.urls import reverse_lazy

class MoviesList(ListView):
    model = Movie
    context_object_name = 'movies'
    paginate_by = 20

class MovieDetails(DetailView):
    model = Movie
    context_object_name = 'movie'

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

# genre views
class GenreListCreate(CreateView):
    model = MovieGenre
    success_url = reverse_lazy('genre-list-create')
    template_name = 'movies/genre_list_create.html'
    fields = 'name',

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context.update({'genres': MovieGenre.objects.all()})
        return context

class GenreUpdate(UpdateView):
    model = MovieGenre
    success_url = reverse_lazy('genre-list-create')
    fields = 'name',

class GenreDelete(DeleteView):
    model = MovieGenre
    success_url = reverse_lazy('movie-list-create')
