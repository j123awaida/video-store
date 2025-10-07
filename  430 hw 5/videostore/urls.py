from django.urls import path
from .views import (
    MovieListView, MovieDetailView, MovieCreateView,
    MovieUpdateView, MovieDeleteView,
)

urlpatterns = [
    path('', MovieListView.as_view(), name='movie-list'),
    path('movie/add/', MovieCreateView.as_view(), name='movie-add'),
    path('movie/<int:pk>/', MovieDetailView.as_view(), name='movie-detail'),
    path('movie/<int:pk>/edit/', MovieUpdateView.as_view(), name='movie-edit'),
    path('movie/<int:pk>/delete/', MovieDeleteView.as_view(), name='movie-delete'),
]
