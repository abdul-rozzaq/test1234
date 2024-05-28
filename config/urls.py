from django.contrib import admin
from django.urls import path

from .views import about, index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='home_page'),
    path('about/', about, name='about_page'),
]
