from django.db import models
from django.contrib.auth.models import User


# 用户注册模型
class UserProfile(models.Model):
    # cascade属性，删除user时会删除它外键对应的数据
    user = models.OneToOneField(User, unique=True, on_delete=models.CASCADE)
    birth = models.DateField(blank=True, null=True)
    phone = models.CharField(max_length=20, null=True)

    def __str__(self):
        return 'user {}'.format(self.user.username)


# 用户个人详细信息
class UserInfo(models.Model):
    user = models.OneToOneField(User, unique=True, on_delete=models.CASCADE)
    school = models.CharField(max_length=100, blank=True)
    company = models.CharField(max_length=100, blank=True)
    profession = models.CharField(max_length=100, blank=True)
    address = models.CharField(max_length=100, blank=True)
    aboutme = models.TextField(blank=True)
    photo = models.TextField(blank=True)

    def __str__(self):
        return "user:{}".format(self.user.username)