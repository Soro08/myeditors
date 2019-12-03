from django.urls import path, include
from . import views
from .sqlviews.compile import compilesql

urlpatterns = [
    path('', views.home, name="home"),
    path('compile', views.compilesql, name="compile"),

    path('getexo', views.getexo, name="getexo"),
]