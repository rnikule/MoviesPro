
from django.contrib import admin
from django.urls import path, include
from Movies import views as myviews
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',myviews.login_view, name='login'),
    path('api/', include('Movies.urls')),
    path('register/',myviews.register_view, name='register')
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
