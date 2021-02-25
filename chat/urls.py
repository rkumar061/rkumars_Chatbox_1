from django.urls import path, include

from . import views


urlpatterns = [

    path('', views.index, name='index'),
    path('chat', views.chat, name='index'),
    path('newmsg', views.newmsg, name='index'),
    path('refresh', views.refresh, name='refresh'),

]
