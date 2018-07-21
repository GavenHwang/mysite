from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
from slugify import slugify


# 文章栏目
class ArticleColumn(models.Model):
    # OneToMany
    user = models.ForeignKey(User, related_name='article_column', on_delete=models.PROTECT)
    column = models.CharField(max_length=200)
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.column


# 文章标签
class ArticleTag(models.Model):
    author = models.ForeignKey(User, related_name="tag", on_delete=models.PROTECT)
    tag = models.CharField(max_length=500)

    def __str__(self):
        return self.tag


# 文章
class ArticlePost(models.Model):
    # OneToMany
    author = models.ForeignKey(User, related_name="article", on_delete=models.PROTECT)
    title = models.CharField(max_length=200)
    # 文章对象url
    slug = models.SlugField(max_length=500)
    # OneToMany
    column = models.ForeignKey(ArticleColumn, related_name="article_column", on_delete=models.PROTECT)
    body = models.TextField()
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)
    # 点赞用户
    users_like = models.ManyToManyField(User, related_name="article_like", blank=True)
    # 文章标签
    article_tag = models.ManyToManyField(ArticleTag, related_name="article_tag", blank=True)

    class Meta:
        ordering = ("-updated",)    # 按发布时间倒序排列
        index_together = (('id', 'slug'),)  # 建立索引

    def __str__(self):
        return self.title

    def save(self, *args, **kargs):
        self.slug = slugify(self.title)     # 文章对象的url
        super(ArticlePost, self).save(*args, **kargs)

    def get_absolute_url(self):
        return reverse("article:article_detail", args=[self.id, self.slug])

    def get_url_path(self):
        return reverse("article:list_article_detail", args=[self.id, self.slug])


# 评论
class Comment(models.Model):
    article = models.ForeignKey(ArticlePost, related_name="comments", on_delete=models.PROTECT)
    commentator = models.CharField(max_length=90, blank=True)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return "Comment by {0} on {1}".format(self.commentator.username, self.article)