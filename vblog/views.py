from django.shortcuts import render
from .models import Post
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
