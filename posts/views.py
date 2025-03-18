from django.shortcuts import render, redirect
from .models import Post
# Create your views here.

def index(request):
    posts = Post.objects.all() #Post라는 클래스에 모든 데이터를 가져오는 함수
    
    context = {
        'posts': posts,
    }

    return render(request, 'index.html', context)

def detail(request, id):
    post = Post.objects.get(id = id)

    context = {
        'post': post,
    }

    return render(request, 'detail.html', context)

def new(request):
    return render(request, 'new.html')

def create(request):
    title = request.GET.get('title')
    content = request.GET.get('content')

    post = Post()
    post.title = title # Post라는 모델에 있는 'title'이라는 컬럼에
                       # 우리가 받은 title이라는 변수를 할당해준다
    post.content = content
    post.save()

    # return redirect('/index/')
    return redirect(f'/posts/{post.id}/')