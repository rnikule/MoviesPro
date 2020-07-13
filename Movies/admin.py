from django.contrib import admin

from .models import Movie, Users

class MovieAdmin(admin.ModelAdmin):
    list_display = ['name', 'imdb_score', 'director', 'popularity', 'genre']
    search_fields = ['name', 'director']
    pass

class UserAdmin(admin.ModelAdmin):
    list_display = ['first_name','last_name','username','password','email','mobile']

admin.site.register(Movie, MovieAdmin)
admin.site.register(Users, UserAdmin)