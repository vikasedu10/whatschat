from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('<str:room>/', views.room, name="room"),
    path('check_room', views.check_room, name="check_room"),
    path('send', views.send, name="send"),
    path('get-messages/<str:room>/', views.get_messages, name="get-messages"),
]