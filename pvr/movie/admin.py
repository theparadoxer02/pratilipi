from django.contrib import admin
from .models  import Country, City, Movie, Theatre, RunningMovie
# Register your models here.

admin.site.register(Country)
admin.site.register(City)
admin.site.register(Movie)
admin.site.register(Theatre)
admin.site.register(RunningMovie)

