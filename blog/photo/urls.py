# coding:utf-8
from django.urls import path
from . import views
app_name = 'photo'

urlpatterns = [
    path('', views.photo_list, name='photo_list'),
    path('category/<int:category_id>/', views.photo_category, name='photo_category'),
]