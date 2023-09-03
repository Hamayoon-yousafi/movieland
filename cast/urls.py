from django.urls import path
from . import views

urlpatterns = [
    path('', views.CastList.as_view(), name='cast-list'),
    path('cast/<int:pk>/', views.CastDetails.as_view(), name='cast-details'),
    path('cast/create/', views.CastCreate.as_view(), name='cast-create'),
    path('cast/<int:pk>/update/', views.CastUpdate.as_view(), name='cast-update'),
    path('cast/<int:pk>/delete/', views.CastDelete.as_view(), name='cast-delete'),
]