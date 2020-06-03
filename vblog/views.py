from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment
from .forms import NewComment
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
    # comment_form = NewComment()
    # new_comment = None
    # ! before save data from from comment form
    if request.method == 'POST':
        comment_form = NewComment(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            # ! connect comment with post
            new_comment.post = post
            new_comment.save()
            comment_form = NewComment()

    else:
        comment_form = NewComment()
    context = {
        'title': post,
        'post': post,
        'comments': comments,
        'comment_form': comment_form
    }

    return render(request, 'post_detail.html', context)
