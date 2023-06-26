from django.urls import path, reverse
# 引入views.py
from . import views
from .feeds import LatestPostsFeed
from .views import MyFeed  # 导入包含 MyFeed 视图的 views 模块
from allauth.account.views import PasswordChangeView

app_name = 'article'

urlpatterns = [
    # 文章列表
    path('article-list/', views.article_list, name='article_list'),
    # 文章详情
    path('article-detail/<int:id>/', views.article_detail, name='article_detail'),
    # 写文章
    path('article-create/', views.article_create, name='article_create'),
    # 删除文章
    path('article-delete/<int:id>/', views.article_delete, name='article_delete'),
    # 安全删除文章
    path('article-safe-delete/<int:id>/', views.article_safe_delete, name='article_safe_delete'),
    # 更新文章
    path('article-update/<int:id>/', views.article_update, name='article_update'),
    # 点赞 +1
    path('increase-likes/<int:id>/', views.IncreaseLikesView.as_view(), name='increase_likes'),

    # 我的文章
    path('my_article/', views.my_articles, name='my_article'),

    # 我的点赞/需创建点赞模型/暂未创建点赞模型
    # path('my_likes/',views.my_likes, name='my_likes'),

    # 列表类视图
    path('list-view/', views.ArticleListView.as_view(), name='list_view'),
    # 详情类视图
    path('detail-view/<int:pk>/', views.ArticleDetailView.as_view(), name='detail_view'),
    # 创建类视图
    path('create-view/', views.ArticleCreateView.as_view(), name='create_view'),
    # 导航首页
    path('index_home', views.welcome_mysite, name='index_home'),

    # rss
    path("rss/", MyFeed(), name="my_feed"),  # 配置用于绑定 RSS feed 的 URL 模式，并指定该视图的名称
    # 推荐内容
    # path("recommend/<int:pk>", views.article_recommend, name='recommend'),
    # 作者下所有文章
    path('author/<int:pk>/', views.author_detail, name='author_detail'),

    # 错误页显示
    # path('*\d+/', views.page_not_found_view, name='error_page'),

    # allauth
    # path('accounts/password/change/', PasswordChangeView.as_view(), name='account_change_password')

]
