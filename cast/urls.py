from django.urls import path
from . import views

urlpatterns = [
    path('', views.CastList.as_view(), name='cast-list'),
    path('<int:pk>/', views.CastDetails.as_view(), name='cast-details'),
    path('create/', views.CastCreate.as_view(), name='cast-create'),
    path('<int:pk>/update/', views.CastUpdate.as_view(), name='cast-update'),
    path('<int:pk>/delete/', views.CastDelete.as_view(), name='cast-delete'),
]