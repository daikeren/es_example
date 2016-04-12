from django.shortcuts import render
from .models import Post
from elasticsearch_dsl import Search
from django.http import HttpResponse


def home(request):
    post_list = Post.objects.all()
    return render(request, 'home.html', {
        'post_list': post_list,
    })


def search(request):
    posts = None
    s = Search(index='trip_post')
    q = request.GET.get('q', None)
    if q:
        posts = s.query('match', title=q).execute()

    return render(request, 'search.html', {'posts': posts})
