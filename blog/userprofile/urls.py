from django.urls import path
from . import views

app_name = 'userprofile'

urlpatterns = [
    # 用户登录
    path('login/', views.user_login, name='login'),
    # 用户退出
    path('logout/', views.user_logout, name='logout'),
    # 用户注册
    path('register/', views.user_register, name='register'),
    # 用户删除
    path('delete/<int:id>/', views.user_delete, name='delete'),
    # 用户信息
    path('edit/<int:id>/', views.profile_edit, name='edit'),

    # 显示饼状图
    # path('echarts/', views.show_tag, name='show_tag'),
    # 关于
    path('about_me/', views.about_me, name='about_me'),


# /accounts/password/change/ [name='account_change_password'] 修改密码(需登录)
# /accounts/password/set/ [name='account_set_password'] 设置密码(用于邮件重置密码，不需要登录)


]

