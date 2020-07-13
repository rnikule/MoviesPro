from django.urls import path
from Movies import views


urlpatterns = [
    path('',views.MovieList.as_view()),
]
