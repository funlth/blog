# from django.shortcuts import render, redirect
#
# from django.views import View
from django.views.generic import ListView
# from django.contrib.auth.mixins import LoginRequiredMixin
#
from article.models import ArticlePost
#
#
# class CommentNoticeListView(LoginRequiredMixin, ListView):
#     """通知列表"""
#     # 上下文的名称
#     context_object_name = 'notices'
#     # 模板位置
#     template_name = 'notice/list.html'
#     # 登录重定向
#     login_url = '/userprofile/login/'
#
#     # 未读通知的查询集
#     def get_queryset(self):
#         return self.request.user.notifications.unread()
#
#
# class CommentNoticeUpdateView(View):
#     """更新通知状态"""
#     # 处理 get 请求
#     def get(self, request):
#         # 获取未读消息
#         notice_id = request.GET.get('notice_id')
#         # 更新单条通知
#         if notice_id:
#             article = ArticlePost.objects.get(id=request.GET.get('article_id'))
#             request.user.notifications.get(id=notice_id).mark_as_read()
#             return redirect(article)
#         # 更新全部通知
#         else:
#             request.user.notifications.mark_all_as_read()
#             return redirect('notice:list')


from django.views.generic import View
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin


class CommentNoticeListView(LoginRequiredMixin, ListView):
    """通知列表"""
    context_object_name = 'notices'
    template_name = 'notice/list.html'
    login_url = '/userprofile/login/'
    redirect_field_name = 'next'  # 改善用户登录体验

    def get_queryset(self):
        return self.request.user.notifications.unread()


class CommentNoticeUpdateView(View):
    """更新通知状态"""

    def get(self, request):
        notice_id = request.GET.get('notice_id')
        article_id = request.GET.get('article_id')

        if notice_id and article_id:
            # 更安全的取对象方式
            article = get_object_or_404(ArticlePost, id=article_id)
            notice = get_object_or_404(request.user.notifications, id=notice_id)
            if notice.recipient == request.user:
                notice.mark_as_read()
            else:
                return redirect('404')  # 给用户返回404错误页面等提示信息
            return redirect(article)
        elif notice_id:
            notice = get_object_or_404(request.user.notifications, id=notice_id)
            if notice.recipient == request.user:
                notice.mark_as_read()
            else:
                return redirect('404')
            return redirect('notice:list')
        else:
            request.user.notifications.mark_all_as_read()
            return redirect('notice:list')