from django.urls import path
from .views import Login, Logout, RegistrationView, update_user_genre

urlpatterns = [
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
    path('register/', RegistrationView.as_view(), name='register'),
    path('update-profile/', update_user_genre, name='update-profile'),
]