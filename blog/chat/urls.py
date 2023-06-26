# coding:utf-8
# chat/urls.py


from django.urls import path, reverse

from . import views

app_name = 'chat'

urlpatterns = [
   # path('', views.index, name='index'),
   # path('<str:room_name>/', views.room, name='room'),
   # path('chat_robot/', views.chatRobot, name='chatrobot'),

   path('<str:room_name>/', views.room, name='room'),
   path('post-message/', views.post_message, name='message'),


]