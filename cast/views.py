from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from .models import Cast
from django.urls import reverse_lazy
from .forms import CastForm


class CastList(ListView):
    model = Cast
    pasginate_by = 20
    context_object_name = 'casts'


class CastCreate(CreateView):
    model = Cast
    form_class = CastForm
    success_url = reverse_lazy('cast-list')

class CastUpdate(UpdateView):
    model = Cast
    form_class = CastForm

    def get_success_url(self):
        return reverse_lazy('cast-details', kwargs={'pk': self.object.pk})


class CastDetails(DetailView):
    model = Cast
    context_object_name = 'cast'

class CastDelete(DeleteView):
    model = Cast
    success_url = reverse_lazy('cast-list')