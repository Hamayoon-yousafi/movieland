from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView
from .forms import UserRegistrationForm
from django.contrib.auth import login


class Login(LoginView):
    template_name = 'user/login.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        next_page = self.request.GET.get('next')
        if next_page:
            return next_page
        return reverse_lazy('movies')
    

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