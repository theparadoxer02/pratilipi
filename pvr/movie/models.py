from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "countries"


class City(models.Model):
    name = models.CharField(max_length=50)
    country = models.ForeignKey('Country', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "cities"


class Movie(models.Model):
    name =  models.CharField(max_length=30, blank=False, unique=True)
    release_date = models.DateField(null=True, blank=True)
    genre = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return self.name


class Theatre(models.Model):
    name = models.CharField(max_length=50, blank=False)
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='cities')

    def __str__(self):
        return self.name

class RunningMovie(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='movies')
    theatre = models.ForeignKey(Theatre, on_delete=models.CASCADE, related_name='theatres')
    is_running = models.BooleanField(default=True)

    def __str__(self):
        return  self.movie.name + "   >>   " + self.theatre.name