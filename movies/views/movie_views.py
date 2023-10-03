from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from ..models import Movie, MovieGenre
from ..forms import MovieForm, ReviewForm
from django.urls import reverse_lazy
from django.db.models import Q, Count
from datetime import date
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from datetime import datetime


class MoviesHomePage(TemplateView):
    template_name = 'movies/home_page.html'

    def get_context_data(self, **kwargs):
        movies = Movie.objects.all()
        context =  super().get_context_data(**kwargs)
        context.update({
            'current_date': date.today(),
            'upcoming_movies': movies.filter(release_date__gt=date.today()).order_by('release_date'),
            'top_this_month': movies.filter(release_date__year=datetime.now().year, release_date__month=datetime.now().month).order_by('-total_positive_votes')[:3],
            'movies_for_you': movies.filter(genre_ids__name=self.request.user.profile.favorite_genre.name).order_by('-release_date')[:20] 
                if self.request.user.is_authenticated and self.request.user.profile.favorite_genre else None,
            'being_discussed': Movie.objects.annotate(num_reviews=Count('review')).order_by('-num_reviews', '-release_date')[:20],
            'popular': movies.order_by('-total_positive_votes', '-release_date')[:20],
            'genres': MovieGenre.objects.all(),
            'movies_count': movies.count
        })
        return context

class MoviesList(ListView):
    model = Movie
    context_object_name = 'movies'
    paginate_by = 12

    def get_context_data(self, **kwargs):
        context = super(MoviesList, self).get_context_data(**kwargs)
        context.update({
            'search': self.search,
            'decade': self.decade,
            'upcoming': self.upcoming,
            'current_month': self.current_month,
        })
        return context

    def get_queryset(self):
        self.search = self.request.GET.get('search', '').strip()
        self.upcoming = self.request.GET.get('upcoming', '').strip()
        self.decade = self.request.GET.get('decade', '').strip()
        self.current_month = self.request.GET.get('current_month', '').strip()
        self.upcoming = True if self.upcoming == 'true' else False
        self.current_month = True if self.current_month == 'true' else False
        
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
        if self.decade:
            self.decade = int(self.decade)
            query = query.filter(release_date__year__range=[self.decade, self.decade + 9])
        if self.current_month:
            query = query.filter(release_date__year=datetime.now().year, release_date__month=datetime.now().month)
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