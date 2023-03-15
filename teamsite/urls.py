from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('partnership', views.partnership, name='partnership'),
    path('team', views.team, name='team'),
    path('publications', views.publications, name='publications'),



]