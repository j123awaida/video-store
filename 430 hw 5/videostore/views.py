from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.db.models import Q
from .models import Movie
from .forms import MovieForm

class MovieListView(ListView):
    model = Movie
    template_name = 'videostore/movie_list.html'
    context_object_name = 'movies'

    def get_queryset(self):
        qs = super().get_queryset()
        q = self.request.GET.get('q', '')
        if q:
            qs = qs.filter(
                Q(title__icontains=q) |
                Q(director_name__icontains=q) |
                Q(actor1_name__icontains=q) |
                Q(actor2_name__icontains=q) |
                Q(genre__icontains=q) |
                Q(movie_id__icontains=q)
            )
        return qs

class MovieDetailView(DetailView):
    model = Movie
    template_name = 'videostore/movie_detail.html'

class MovieCreateView(CreateView):
    model = Movie
    form_class = MovieForm
    template_name = 'videostore/movie_form.html'
    success_url = reverse_lazy('movie-list')

class MovieUpdateView(UpdateView):
    model = Movie
    form_class = MovieForm
    template_name = 'videostore/movie_form.html'
    success_url = reverse_lazy('movie-list')

class MovieDeleteView(DeleteView):
    model = Movie
    template_name = 'videostore/movie_confirm_delete.html'
    success_url = reverse_lazy('movie-list')
