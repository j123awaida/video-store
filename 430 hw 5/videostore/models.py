from django.db import models
from django.urls import reverse
from django.core.validators import MinValueValidator, MaxValueValidator
import datetime

class Movie(models.Model):
    movie_id = models.CharField('MovieID', max_length=20, unique=True)
    title = models.CharField('MovieTitle', max_length=200)
    actor1_name = models.CharField('Actor1Name', max_length=100)
    actor2_name = models.CharField('Actor2Name', max_length=100, blank=True)
    director_name = models.CharField('DirectorName', max_length=100)

    GENRES = [
        ('Comedy', 'Comedy'),
        ('Romance', 'Romance'),
        ('Action', 'Action'),
        ('Drama', 'Drama'),
        ('Thriller', 'Thriller'),
        ('Sci-Fi', 'Sci-Fi'),
        ('Horror', 'Horror'),
        ('Animation', 'Animation'),
        ('Other', 'Other'),
    ]
    genre = models.CharField('MovieGenre', max_length=20, choices=GENRES)

    release_year = models.PositiveSmallIntegerField(
        'ReleaseYear',
        validators=[
            MinValueValidator(1888),
            MaxValueValidator(datetime.date.today().year + 1),
        ],
    )

    class Meta:
        ordering = ['-release_year', 'title']

    def __str__(self):
        return f"{self.title} ({self.release_year})"

    def get_absolute_url(self):
        return reverse('movie-detail', args=[self.pk])
