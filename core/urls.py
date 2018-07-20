from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('search', views.search, name='search'),
    path('about', views.about, name='about'),
    path('suggest', views.suggest, name='suggest'),
    path('feedback', views.feedback, name='feedback'),
    path('term/<str:term_str>', views.term, name='term'),
    path('explore/<str:alphabet>', views.explore, name='explore'),
]