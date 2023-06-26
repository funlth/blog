# 引入redirect重定向模块
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
# 引入User模型
from django.contrib.auth.models import User
# 引入HttpResponse
from django.http import HttpResponse, JsonResponse
# 导入数据模型ArticlePost, ArticleColumn
from django.template.loader import render_to_string

from .models import ArticlePost, ArticleColumn
# 引入刚才定义的ArticlePostForm表单类
from .forms import ArticlePostForm
# 引入markdown模块
import markdown
# 引入login装饰器
from django.contrib.auth.decorators import login_required
# 引入分页模块
from django.core.paginator import Paginator
# 引入搜索 Q 对象
from django.db.models import Q
# Comment 模型
from comment.models import Comment

from comment.forms import CommentForm

# 通用类视图
from django.views import View
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView

from my_blog.settings import LOGGING
import logging
import re

# logging.config.dictConfig(LOGGING)
# logger = logging.getLogger('django.request')


# 文章列表
def article_list(request):
    # 从 url 中提取查询参数
    search = request.GET.get('search')
    order = request.GET.get('order')
    column = request.GET.get('column')
    tag = request.GET.get('tag')
    likes = request.GET.get('order', '')

    # 初始化查询集
    article_list = ArticlePost.objects.all()

    # 搜索查询集
    if search:
        article_list = article_list.filter(
            Q(title__icontains=search) |
            Q(body__icontains=search)
        )
    else:
        # 将 search 参数重置为空
        search = ''

    # 栏目查询集
    if column is not None and column.isdigit():
        article_list = article_list.filter(column=column)

    # 标签查询集
    if tag and tag != 'None':
        article_list = article_list.filter(tags__name__in=[tag])

    # 查询集排序
    if order == 'total_views':
        # 按热度排序博文
        article_list = article_list.order_by('-total_views')
        # 如果设置了按点赞数排序，则使用点赞数量字段进行降序排列
    if likes:
        article_list = article_list.order_by('-likes')

    # 每页显示 1 篇文章
    paginator = Paginator(article_list, 11)
    # 获取 url 中的页码
    page = request.GET.get('page')
    # 将导航对象相应的页码内容返回给 articles
    articles = paginator.get_page(page)
    # 需要传递给模板（templates）的对象
    context = {
        'articles': articles,
        'order': order,
        'search': search,
        'column': column,
        'tag': tag,
        'like':likes,
    }
    # render函数：载入模板，并返回context对象
    return render(request, 'article/list.html', context)


# 文章详情
def article_detail(request, id):
    # 取出相应的文章
    # article = ArticlePost.objects.get(id=id)
    # logger.warning('Something went wrong!')
    article = get_object_or_404(ArticlePost, id=id)

    # 取出文章评论
    comments = Comment.objects.filter(article=id)

    # 浏览量 +1
    article.total_views += 1
    article.save(update_fields=['total_views'])

    # 相邻发表文章的快捷导航
    pre_article = ArticlePost.objects.filter(id__lt=article.id).order_by('-id')
    next_article = ArticlePost.objects.filter(id__gt=article.id).order_by('id')
    if pre_article.count() > 0:
        pre_article = pre_article[0]
    else:
        pre_article = None

    if next_article.count() > 0:
        next_article = next_article[0]
    else:
        next_article = None

    # Markdown 语法渲染
    md = markdown.Markdown(
        extensions=[
            # 包含 缩写、表格等常用扩展
            'markdown.extensions.extra',
            # 语法高亮扩展
            'markdown.extensions.codehilite',
            # 目录扩展
            'markdown.extensions.toc',
            # 添加脚注
            'markdown.extensions.footnotes',
        ]
    )
    article.body = md.convert(article.body)

    # 为评论引入表单
    comment_form = CommentForm()

    # 需要传递给模板的对象
    context = {
        'article': article,
        'toc': md.toc,
        'comments': comments,
        'pre_article': pre_article,
        'next_article': next_article,
        'comment_form': comment_form,
    }
    # 载入模板，并返回context对象
    return render(request, 'article/detail.html', context)

# 文章详情/markdown优化
from markdown.extensions.toc import TocExtension
from markdown.extensions.tables import TableExtension
from markdown.extensions.sane_lists import SaneListExtension

# def get_related_articles(article):
#     pre_article = ArticlePost.objects.filter(id__lt=article.id).order_by('-id').first()
#     next_article = ArticlePost.objects.filter(id__gt=article.id).order_by('id').first()
#     return pre_article, next_article

# def md_render(text):
#     md_extensions = [
#         'markdown.extensions.extra',
#         'markdown.extensions.codehilite',
#         'markdown.extensions.smarty',
#         'markdown.extensions.fenced_code',
#         SaneListExtension(),
#         TocExtension(permalink=True),
#         TableExtension(),
#     ]
#     md = markdown.Markdown(
#         extensions=md_extensions,
#         output_format='html5',
#     )
#     return md.convert(text)

# def article_detail(request, id):
#     article = get_object_or_404(ArticlePost, id=id)
#     comments = Comment.objects.filter(article=id)
#     article.total_views += 1
#     article.save(update_fields=['total_views'])
#     pre_article, next_article = get_related_articles(article)
#     article.body = md_render(article.body)
#     comment_form = CommentForm()
#     context = {
#         'article': article,
#         'toc': md_render(md.TOC),
#         'comments': comments,
#         'pre_article': pre_article,
#         'next_article': next_article,
#         'comment_form': comment_form,
#     }
#     return render(request, 'article/detail.html', context)

# 写文章的视图
# @login_required(login_url='/userprofile/login/')
# def article_create(request):
#     # 判断用户是否提交数据
#     if request.method == "POST":
#         # 将提交的数据赋值到表单实例中
#         article_post_form = ArticlePostForm(request.POST, request.FILES)
#
#         # 判断提交的数据是否满足模型的要求
#         if article_post_form.is_valid():
#             # 保存数据，但暂时不提交到数据库中
#             new_article = article_post_form.save(commit=False)
#             # 指定登录的用户为作者
#             new_article.author = User.objects.get(id=request.user.id)
#             if request.POST['column'] != 'none':
#                 # 保存文章栏目
#                 new_article.column = ArticleColumn.objects.get(id=request.POST['column'])
#             # 将新文章保存到数据库中
#             new_article.save()
#             # 保存 tags 的多对多关系
#             article_post_form.save_m2m()
#             # 完成后返回到文章列表
#             return redirect("article:article_list")
#         # 如果数据不合法，返回错误信息
#         else:
#             return HttpResponse("表单内容有误，请重新填写。")
#     # 如果用户请求获取数据
#     else:
#         # 创建表单类实例
#         article_post_form = ArticlePostForm()
#         # 文章栏目
#         columns = ArticleColumn.objects.all()
#         # 赋值上下文
#         context = {'article_post_form': article_post_form, 'columns': columns}
#         # 返回模板
#         return render(request, 'article/create.html', context)

# 文章发表/内容过滤
from bs4 import BeautifulSoup
@login_required(login_url='/userprofile/login/')
def article_create(request):
    if request.method == "POST":
        title = request.POST.get('title', '')

        # content = request.POST.get('content', '')
        #         # 提取出富文本正文内容
        #         # soup = BeautifulSoup(content, 'html.parser')
        #         # text_content = soup.get_text()
        # if has_badwords(title) or has_badwords(text_content):

        if has_badwords(title):
            # 检测到不良词汇时，返回错误提示
            return HttpResponse("文章标题不当言论，请修改后重新提交。不当言论信息检测值："+str(has_badwords(text=title)))
        else:
            article_post_form = ArticlePostForm(request.POST, request.FILES)
            if article_post_form.is_valid():
                new_article = article_post_form.save(commit=False)
                new_article.author = User.objects.get(id=request.user.id)
                if request.POST['column'] != 'none':
                    new_article.column = ArticleColumn.objects.get(id=request.POST['column'])
                new_article.save()
                article_post_form.save_m2m()
                return redirect("article:article_list")
            else:
                return HttpResponse("表单内容有误，请重新填写。")
    else:
        article_post_form = ArticlePostForm()
        columns = ArticleColumn.objects.all()
        context = {'article_post_form': article_post_form, 'columns': columns}
        return render(request, 'article/create.html', context)

def has_badwords(text):
    badword_list = ["不当言论",'不当言论1', '不当言论2', '不当言论3']
    for word in badword_list:
        if word in text:
            return True
    return False



# 删除文章，此方式有 csrf 攻击风险
@login_required(login_url='/userprofile/login/')
def article_delete(request, id):
    # 根据 id 获取需要删除的文章
    article = ArticlePost.objects.get(id=id)
    # 过滤非作者的用户
    if request.user != article.author:
        return HttpResponse("抱歉，你无权修改这篇文章。")
    # 调用.delete()方法删除文章
    article.delete()
    # 完成删除后返回文章列表
    return redirect("article:article_list")


# 安全删除文章
@login_required(login_url='/userprofile/login/')
def article_safe_delete(request, id):
    if request.method == 'POST':
        article = ArticlePost.objects.get(id=id)
        if request.user != article.author:
            return HttpResponse("抱歉，你无权修改这篇文章。")
        article.delete()
        return redirect("article:article_list")
    else:
        return HttpResponse("仅允许post请求")


# 更新文章
@login_required(login_url='/userprofile/login/')
def article_update(request, id):
    """
    更新文章的视图函数
    通过POST方法提交表单，更新titile、body字段
    GET方法进入初始表单页面
    id： 文章的 id
    """

    # 获取需要修改的具体文章对象
    article = ArticlePost.objects.get(id=id)

    # 过滤非作者的用户
    if request.user != article.author:
        return HttpResponse("抱歉，你无权修改这篇文章。")

    # 判断用户是否为 POST 提交表单数据
    if request.method == "POST":
        # 将提交的数据赋值到表单实例中
        article_post_form = ArticlePostForm(data=request.POST)
        # 判断提交的数据是否满足模型的要求
        if article_post_form.is_valid():
            # 保存新写入的 title、body 数据并保存
            article.title = request.POST['title']
            article.body = request.POST['body']

            if request.POST['column'] != 'none':
                # 保存文章栏目
                article.column = ArticleColumn.objects.get(id=request.POST['column'])
            else:
                article.column = None

            if request.FILES.get('avatar'):
                article.avatar = request.FILES.get('avatar')

            article.tags.set(*request.POST.get('tags').split(','), clear=True)
            article.save()
            # 完成后返回到修改后的文章中。需传入文章的 id 值
            return redirect("article:article_detail", id=id)
        # 如果数据不合法，返回错误信息
        else:
            return HttpResponse("表单内容有误，请重新填写。")

    # 如果用户 GET 请求获取数据
    else:
        # 创建表单类实例
        article_post_form = ArticlePostForm()

        # 文章栏目
        columns = ArticleColumn.objects.all()
        # 赋值上下文，将 article 文章对象也传递进去，以便提取旧的内容
        context = {
            'article': article,
            'article_post_form': article_post_form,
            'columns': columns,
            'tags': ','.join([x for x in article.tags.names()]),
        }

        # 将响应返回到模板中
        return render(request, 'article/update.html', context)


# 点赞数 +1
class IncreaseLikesView(View):
    def post(self, request, *args, **kwargs):
        article = ArticlePost.objects.get(id=kwargs.get('id'))
        article.likes += 1
        article.save()
        return HttpResponse('success')


def article_list_example(request):
    """
    与下面的类视图做对比的函数
    简单的文章列表
    """
    if request.method == 'GET':
        articles = ArticlePost.objects.all()
        context = {'articles': articles}
        return render(request, 'article/list.html', context)


class ContextMixin:
    """
    Mixin
    """

    def get_context_data(self, **kwargs):
        # 获取原有的上下文
        context = super().get_context_data(**kwargs)
        # 增加新上下文
        context['order'] = 'total_views'
        return context


class ArticleListView(ContextMixin, ListView):
    """
    文章列表类视图
    """
    # 查询集的名称
    context_object_name = 'articles'
    # 模板
    template_name = 'article/list.html'

    def get_queryset(self):
        """
        查询集
        """
        queryset = ArticlePost.objects.filter(title='Python')
        return queryset


class ArticleDetailView(DetailView):
    """
    文章详情类视图
    """
    queryset = ArticlePost.objects.all()
    context_object_name = 'article'
    template_name = 'article/detail.html'

    def get_object(self):
        """
        获取需要展示的对象
        """
        # 首先调用父类的方法
        obj = super(ArticleDetailView, self).get_object()
        # 浏览量 +1
        obj.total_views += 1
        obj.save(update_fields=['total_views'])
        return obj


class ArticleCreateView(CreateView):
    """
    创建文章的类视图
    """
    model = ArticlePost
    fields = '__all__'
    # 或者有选择的提交字段，比如：
    # fields = ['title']
    template_name = 'article/create_by_class_view.html'


# 错误页面
def page_not_found_view(
        request,
        exception,
        template_name='article/error_page.html'):
    if exception:
        # logger.error(exception)
        pass
    url = request.get_full_path()
    return render(request,
                  template_name,
                  {'message': '哎呀，您访问的地址 ' + url + ' 是一个未知的地方。请点击首页看看别的？',
                   'statuscode': '404'},
                  status=404)


# feed rss订阅
from django.contrib.syndication.views import Feed  # 导入 Django 提供的 Feed 视图类
from django.urls import reverse_lazy, reverse  # 导入反向URL解析函数，用于生成视图函数对应的 URL
from article.models import ArticlePost  # 导入自定义模型


class MyFeed(Feed):  # 创建 MyFeed 作为继承 Feed 的子类
    title = "博客——lee"  # 定义 feed 标题
    link = reverse_lazy("home")  # 定义 feed 链接，并通过反向URL解析函数指定链接为 home 页面
    description = "rss订阅："  # 定义 feed 描述

    def items(self):  # 创建 items 方法，返回需要展示在 feed 中的数据，默认返回所有数据，可以通过切片操作限制条目数
        return ArticlePost.objects.all()[:10]  # 返回自定义模型 MyModel 的前10个实例

    def item_title(self, item):  # 可选方法，重写此方法以改变每个 feed 条目的标题。传递的参数是请求项（RequestItem），它是一种包含在您的 `items()` 方法中返回的对象的实例。
        return item.title  # 返回请求项的标题

    def item_description(self, item):  # 可选方法，重写此方法以改变每个 feed 条目的描述。传递的参数是请求项，与 item_title 相同。
        # return item.description  # 返回请求项的描述
        return item.body

    def item_link(self, item):  # 可选方法，重写此方法以改变每个 feed 条目的链接。传递的参数是请求项。
        return reverse_lazy("article:detail_view", kwargs={"pk": item.pk})  # 返回通过反向 URL 解析函数解析的特定实例的 URL




# 生成文章分享链接
def post_detail(request, pk):
    # 获取当前文章对象
    post = ArticlePost.objects.get(pk=pk)

    return render(request, 'article/detail.html', {"post": post, "request": request})


# 我的文章
def my_articles(request):
    articles = ArticlePost.objects.filter(author=request.user).order_by('-created')
    context = {
        'articles': articles
    }
    return render(request, 'article/my_articles.html', context)




# 我的喜欢
# 迭代，需要添加点赞模型，暂时未创建点赞模型
def my_likes(request):

    pass
'''点赞模型方法
class ArticleLikeView(View):

    def post(self, request, pk):
        if not request.user.is_authenticated:
            return HttpResponseBadRequest()

        article = ArticlePost.objects.get(pk=pk)
        like, created = ArticleLike.objects.get_or_create(user=request.user, article=article)

        if not created:
            like.delete()
            article.likes -= 1
            article.save()
            return JsonResponse({'liked': False, 'count': article.likes})
'''


# 欢迎页
def welcome_mysite(request):
    return render(request, 'index_home.html')

# 推荐文章
def article_recommend(request, article_id):
    # 获取当前文章的标签
    current_article = get_object_or_404(ArticlePost, id=article_id)
    tags = current_article.tags.all()

    # 根据标签查找相关的文章
    recommended_articles = ArticlePost.objects.filter(tags__in=tags).exclude(id=article_id).distinct()

    # 在模板中渲染推荐列表
    return render(request, 'article/article_recommend.html', {'recommended_articles': recommended_articles})



'''
获取作者信息
获取作者下全部文章信息
'''
from userprofile.models import Profile as profile
# 作者下所有文章
def author_detail(request, id):
    # 获取作者信息和包含该作者 ID 的所有文章
    author_info = profile.objects.get(id=id)
    articles = ArticlePost.objects.filter(id=id)
    content = {
        'author_info':author_info,
        'articles':articles
    }
    return render(request, 'article/author_articles.html', content)
    pass