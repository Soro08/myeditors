from django.urls import path, include
from . import views
from sqlparser import views as sqlviews

urlpatterns = [
    path('<int:id>', views.home, name="home"),

    path('compile', views.compilehtml, name="compile"),
    
    path('',sqlviews.accueil)
]