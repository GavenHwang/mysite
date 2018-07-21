import markdown
from django import template
from article.models import ArticlePost
from django.db.models import Count
from django.utils.safestring import mark_safe

register = template.Library()


@register.simple_tag
def total_articles():
    return ArticlePost.objects.count()


@register.simple_tag
def author_total_articles(user):
    return user.article.count()


@register.inclusion_tag('article/list/latest_articles.html')
def latest_articles(n=3):
    latest_articles = ArticlePost.objects.order_by("-created")[:n]
    return {"latest_articles": latest_articles}


# django2.0中assigment_tag改为了simple_tag
@register.simple_tag
def most_commented_article(n=3):
    # 给所有ArticlePost对象加上属性total_comments,属性值为：Count('comments'),然后排序，取前n个
    return ArticlePost.objects.annotate(total_comments=Count('comments')).order_by("-total_comments")[:n]


@register.filter(name='markdown')   # 将该标签的名字markdown_filter改为markdown
def markdown_filter(text):
    return mark_safe(markdown.markdown(text))