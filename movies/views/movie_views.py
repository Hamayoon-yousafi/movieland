from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from ..models import Movie
from ..forms import MovieForm, ReviewForm
from django.urls import reverse_lazy
from django.db.models import Q, Count
from datetime import date
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from datetime import datetime


class MoviesList(ListView):
    model = Movie
    context_object_name = 'movies'
    paginate_by = 20

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context.update({
            'search': self.search,
            'current_date': date.today(),
            'upcoming': self.upcoming,
            'upcoming_movies': self.get_queryset().filter(release_date__gt=date.today()).order_by('release_date'),
            'top_this_month': self.get_queryset().filter(release_date__year=datetime.now().year, release_date__month=datetime.now().month).order_by('-total_positive_votes')[:3],
            'movies_for_you': self.get_queryset().filter(genre_ids__name=self.request.user.profile.favorite_genre.name).order_by('-release_date')[:20] if self.request.user.profile.favorite_genre else None,
            'being_discussed': Movie.objects.annotate(num_reviews=Count('review')).order_by('-num_reviews', '-release_date')[:20],
            'popular': self.get_queryset().order_by('-total_positive_votes', '-release_date')[:20],
        })
        return context

    def get_queryset(self):
        self.search = self.request.GET.get('search', '').strip()
        self.upcoming = self.request.GET.get('upcoming', '').strip()
        
        query = super().get_queryset()
        if self.search:
            query = query.distinct().filter(
                Q(title__icontains=self.search) | 
                Q(story__icontains=self.search) | 
                Q(cast_ids__name__icontains=self.search) |
                Q(tag_ids__name__icontains=self.search) |
                Q(genre_ids__name__icontains=self.search)
            )
        if self.upcoming:
            query = query.filter(release_date__gt=date.today())
        return query


class MovieDetails(DetailView):
    model = Movie
    context_object_name = 'movie'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        reviews = self.object.review_set.all()
        context.update({'review_form': ReviewForm(), 'reviews': reviews, 'reviewers': reviews.values_list('user_id', flat=True)})
        return context

class MovieCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Movie
    form_class = MovieForm
    success_url = reverse_lazy('movies')
    permission_required = 'movies.add_movie' 

class MovieUpdate(LoginRequiredMixin, UpdateView):
    model = Movie
    form_class = MovieForm

    def get_success_url(self):
        return reverse_lazy('movie-details', kwargs={'pk': self.object.pk})

class MovieDelete(DeleteView):
    model = Movie
    success_url = reverse_lazy('movies')