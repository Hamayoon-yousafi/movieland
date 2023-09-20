from django.views.generic import CreateView, UpdateView, DeleteView
from ..models import MovieGenre
from django.urls import reverse_lazy
from django.contrib.auth.mixins import PermissionRequiredMixin



class GenreListCreate(PermissionRequiredMixin, CreateView):
    model = MovieGenre
    success_url = reverse_lazy('genre-list-create')
    template_name = 'movies/configuration_list_create.html'
    fields = 'name',
    permission_required = ['movies.view_genre', 'movies.add_genre']

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs) 
        context.update({'objects': MovieGenre.objects.all(), 'configuration': 'Genres'})
        return context
    
class GenreUpdate(UpdateView):
    model = MovieGenre
    success_url = reverse_lazy('genre-list-create')
    template_name = 'movies/configuration_list_create.html'
    fields = 'name',
    permission_required = 'movies.change_genre'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context.update({'objects': MovieGenre.objects.all(), 'configuration': 'Genres'})
        return context
    
class GenreDelete(DeleteView):
    model = MovieGenre
    success_url = reverse_lazy('genre-list-create')
    permission_required = 'movies.delete_genre'