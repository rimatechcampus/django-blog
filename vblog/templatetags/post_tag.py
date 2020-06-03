from django import template
from vblog.models import Post, Comment
# from django.contrib.auth.decorators import decorators

register = template.Library()


@register.inclusion_tag('latest_posts.html')
def letest_posts():
    context = {'l_posts': Post.objects.all()[0:5]}
    return context


@register.inclusion_tag('latest_comments.html')
def latest_comments():
    context = {'l_comments': Comment.objects.filter(active=True)[:5]}
    return context