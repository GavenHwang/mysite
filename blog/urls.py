from django.conf.urls import url
from . import views

app_name = 'blog'
urlpatterns = [
    # 博客列表页
    url(r'^$', views.blog_title, name='blog_title'),
    # 博客内容页
    url(r'(?P<article_id>\d)/$', views.blog_article, name="blog_detail")
]