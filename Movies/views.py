from django.shortcuts import render,redirect

from .models import Movie, Users
from .serializers import MovieSerializer
from .forms import UserForm, LoginForm
from django.contrib import messages
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import SearchFilter, OrderingFilter

#from rest_framework.authentication import TokenAuthentication
#from rest_framework.permissions import IsAuthenticated



def register_view(request):
    if request.method == "POST":
        rform = UserForm(request.POST)
        if rform.is_valid():
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            username = request.POST.get('username')
            password = request.POST.get('password')
            email = request.POST.get('email')
            mobile = request.POST.get('mobile')

            data = Users(
               first_name = first_name,
               last_name = last_name,
                username = username,
               password = password,
               email = email,
               mobile = mobile
            )
            data.save()
            rform = UserForm()
            context = {'form':rform}
            return render(request,'register.html', context)

    else:
        rform = UserForm()
        context = {'form': rform}
        return render(request, 'register.html', context)



def login_view(request):
    if request.method == "POST":
        lform = LoginForm(request.POST)
        if lform.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = Users.objects.filter(username = username, password = password)

            if not user:
                messages.warning(request, "Incorrect username or password")
                lform = LoginForm()
                context = {'form': lform}
                return render(request, 'login.html', context)
            else:
                return redirect('/api/')

    else:
        lform = LoginForm()
        context = {'form': lform}
        return render(request, 'login.html', context)



class MovieList(generics.ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    pagination_class = PageNumberPagination
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('name', 'director', 'genre')
    # authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated,)
