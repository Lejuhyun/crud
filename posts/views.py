from django.shortcuts import render
from .models import Post
# Create your views here.

def index(request):
    posts = Post.objects.all() #Post라는 클래스에 모든 데이터를 가져오는 함수
    
    context = {
        'posts': posts,
    }

    return render(request, 'index.html', context)