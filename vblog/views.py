from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment
# Create your views here.
# posts = [
#     {
#         'title':'post one',
#         'content':'python is easy and fun',
#         'post_date':'2-6-2020',
#         'author':'rima hazim'
#     },
#     {
#         'title':'post two',
#         'content':'django is easy and fun',
#         'post_date':'2-6-2020',
#         'author':'rmrm hazim'
#     },
#     {
#         'title':'post three',
#         'content':'web developemnt  is easy and fun',
#         'post_date':'2-6-2020',
#         'author':'rora hazim'
#     }
# ]


def home(request):
    posts = Post.objects.all()
    context = {'title': 'home', 'posts': posts}
    return render(request, 'home.html', context)


def about(request):
    context = {'title': 'about'}
    return render(request, 'about.html', context)


# post details


def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    comments = post.comments.filter(active=True)
    context = {'title': post, 'post': post, 'comments': comments}

    return render(request, 'post_detail.html', context)
