from django.views.generic import CreateView, UpdateView, DeleteView
from ..models import MovieTag
from django.urls import reverse_lazy
from django.contrib.auth.mixins import PermissionRequiredMixin


class TagListCreate(PermissionRequiredMixin, CreateView):
    model = MovieTag
    success_url = reverse_lazy('tag-list-create')
    template_name = 'movies/configuration_list_create.html'
    fields = 'name',
    permission_required = ['movies.view_tag', 'movies.add_tag']

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context.update({'objects': MovieTag.objects.all(), 'configuration': 'Tags'})
        return context


class TagUpdate(PermissionRequiredMixin, UpdateView):
    model = MovieTag
    success_url = reverse_lazy('tag-list-create')
    template_name = 'movies/configuration_list_create.html'
    fields = 'name',
    permission_required = 'movies.change_tag' 

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context.update({'objects': MovieTag.objects.all(), 'configuration': 'Tags'})
        return context


class TagDelete(PermissionRequiredMixin, DeleteView):
    model = MovieTag
    success_url = reverse_lazy('tag-list-create')
    permission_required = 'movies.delete_tag'

    # def get_permission_required(self):
    #     # Define the required permission(s) as a list
    #     return ['movies.delete_tag']