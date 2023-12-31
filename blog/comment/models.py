from django.db import models
from django.contrib.auth.models import User
from article.models import ArticlePost
# django-ckeditor
from ckeditor.fields import RichTextField
# django-mptt
from mptt.models import MPTTModel, TreeForeignKey

# 博文的评论
class Comment(MPTTModel):
    article = models.ForeignKey(
        ArticlePost,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='作者评论'
    )

    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        related_name='comments',
        verbose_name='读者评论',
    )

    # mptt树形结构
    parent = TreeForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='children',
    )

    # 记录二级评论回复给谁, str
    reply_to = models.ForeignKey(
        User,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name='replyers'
    )

    body = RichTextField()
    created = models.DateTimeField(auto_now_add=True)

    class MPTTMeta:
        order_insertion_by = ['created']

    def __str__(self):
        return self.body[:20]

    class Meta:
        verbose_name = '内容'
        verbose_name_plural = '评论内容'

