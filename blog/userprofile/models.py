from django.db import models
from django.contrib.auth.models import User
# 引入内置信号
# from django.db.models.signals import post_save
# 引入信号接收器的装饰器
# from django.dispatch import receiver


# 用户扩展信息
class Profile(models.Model):
    # 与 User 模型构成一对一的关系
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile', verbose_name='用户')
    # 电话号码字段
    phone = models.CharField(max_length=20, blank=True, verbose_name='电话号码')
    # 头像
    avatar = models.ImageField(upload_to='avatar/%Y%m%d/', blank=True, verbose_name='头像', default='default.jpg')
    # 个人简介
    bio = models.TextField(max_length=500, blank=True, verbose_name='个人简介')

    def __str__(self):
        return 'user {}'.format(self.user.username)


