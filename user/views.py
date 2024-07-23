from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import UpdateView
from django.views.generic import CreateView
from .forms import UserRegistrationForm
from django.contrib.auth import login
from django.shortcuts import redirect
from movies.models import MovieGenre
from .models import Profile
from .forms import CustomLoginForm, ProfileUpdateForm

class Login(LoginView):
    template_name = 'user/login.html'
    redirect_authenticated_user = True
    form_class = CustomLoginForm

    def get_success_url(self):
        next_page = self.request.GET.get('next')
        if next_page:
            return next_page
        return reverse_lazy('home-page')
    

class Logout(LogoutView):
    next_page = reverse_lazy('movies')


class RegistrationView(CreateView):
    form_class = UserRegistrationForm
    template_name = 'user/registration.html'

    def get_success_url(self):
        return reverse_lazy('movies')
    
    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)
        return response
    

class UpdateProfile(UpdateView):
    model = Profile
    form_class = ProfileUpdateForm
    template_name = 'user/profile.html' 
    success_url = '/user/profile'

    def get_object(self):
        return Profile.objects.get(user=self.request.user)

def update_user_genre(request):
    if request.method == 'POST':
        profile = request.user.profile
        profile.favorite_genre = MovieGenre.objects.get(id=request.POST.get('favorite_genre'))
        profile.save()
    return redirect('home-page')