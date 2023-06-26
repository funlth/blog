# coding:utf-8
import feedparser
from django.contrib.syndication.views import Feed
from django.urls import reverse_lazy
from .models import ArticlePost as Post


'''

'''

class LatestPostsFeed(Feed):
    title = "Blog Posts"
    link = reverse_lazy("blog:post_list")
    description = "The latest blog posts from our website."

    def items(self):
        return Post.objects.order_by("-published_date")[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.body

    def item_link(self, item):
        return reverse_lazy("blog:post_detail", args=[item.slug])