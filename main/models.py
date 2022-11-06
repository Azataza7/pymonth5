from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models import Sum


class Director(models.Model):
    name = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.name

    @property
    def movies_count(self):
        return self.movies.all().count()


class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    duration = models.IntegerField(default=0)
    director = models.ForeignKey(Director, on_delete=models.CASCADE, related_name='movies', null=True)

    def __str__(self):
        return self.title

    @property
    def reviews(self):
        review = Review.objects.filter(movie=self)
        return [{'text'} for i in review]

    @property
    def rating(self):
        summa = Review.objects.all().aggregate(Sum('stars'))["stars__sum"]
        count = Review.objects.all().count()
        try:
            return summa / count
        except:
            return 0


class Review(models.Model):
    text = models.TextField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='reviews', null=True)
    stars = models.PositiveSmallIntegerField(default=1, validators=[MaxValueValidator(5), MinValueValidator(1)])

    def __str__(self):
        return self.text
