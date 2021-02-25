from django.urls import path

from . import views


urlpatterns = [

    path('', views.home, name='home'),
    path('add', views.add, name='add'),
    path('addmore', views.ammount, name='ammount'),
    path('reset', views.home, name='reset')
]
