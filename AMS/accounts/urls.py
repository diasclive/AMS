from django.urls import include, path

from . import views

urlpatterns = [
  path('', include('django.contrib.auth.urls')),
  path('index.html', views.index, name='index'),
]
