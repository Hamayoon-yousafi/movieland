from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import UserPassesTestMixin
from ..models import Movie, Review
from ..forms import ReviewForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render


class CreateReview(LoginRequiredMixin, CreateView):
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
    

class DeleteReview(UserPassesTestMixin, LoginRequiredMixin, DeleteView):
    model = Review

    def test_func(self): 
        return self.get_object().user_id == self.request.user or self.request.user.is_superuser

    def get_success_url(self):
        return reverse_lazy('movie-details', kwargs={'pk': self.kwargs['movie_id']})