# coding:utf-8
from django.urls import path
from .views import upload_file, file_list, download_file
app_name = 'sharefile'

urlpatterns = [
    path('upload/', upload_file, name='upload_file'),
    path('', file_list, name='file_list'),
    path('download/<int:file_id>/', download_file, name='download_file'),  # 新加的路由

]