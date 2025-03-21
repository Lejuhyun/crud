# CRUD

## 0. setting
- 가상환경 생성 : `python -m venv venv`
- 가상환경 활성화: `source venv/Scripts/activate`
- `.gitignore` 설정 (python, windows, macos, django)

## 1. Django 설정
- 장고 설치 :`pip install django`

- 프로젝트 생성
```shell
django-admin startproject crud . #내가 있는 장소에 'crud'라는 프로젝트를 만들어주세요.
```
- 앱 생성
```shell
django-admin startapp posts
```

- 앱 등록: crud(프로젝트)안에 있는 settings.py에서 installed_apps에 앱 등록하기

- post(앱) 안에 들어있는 views를 url.py에 불러오기 : `from posts import views`

- posts(앱) 하위에 templates라는 폴더 만들어주기

- 서버 실행하기: `python manage.py runserver`

1. urls.py에 path('index/', views.index) 만들기
2. views.py에 def index(request): 함수 만들기
3. templates에 index.html 생성

## 2.CRUD
- 의미: **Create(생성), Read(읽기), Update(수정), Delete(삭제)**의 약자로, 데이터베이스에서 데이터를 관리하는 기본적인 기능

- **modeling** (models.py)
```shell
from django.db import models
#Django의 데이터베이스 관련 기능을 제공하는 models 모듈을 가져옴
class Post(models.Model): 
#models.Model을 상속받아 Django에서 데이터베이스 테이블을 자동으로 생성
    title = models.CharField(max_length=100) 
    # CharField: 문자열, 최대 255자
    content = models.TextField()
    # TextField: 긴 문자열, 길이제한 없음
```

    - **ORM(Object-Relational Mapping)**: 객체(Object, python)와 데이터베이스(Table, sql)를 연결(Mapping) 해주는 기술
        - SQL을 직접 작성하지 않고도 데이터베이스를 조작할 수 있도록 도와주는 도구입니다.

- migration(python세상의 코드를 SQL 세상으로 보내는 것)
```shell
# 번역본 생성
python manage.py makemigrations
```
```shell
# DB에 반영
python manage.py migrate
```

- **create super user**
```shell
python manage.py createsuperuser
```

- 관리자페이지(admin)에 모델 등록(`admin.py`)
```python
from django.contrib import admin
from .models import Post #현재 폴더에서 models라는 파일에 있는 Post 접근

# Register your models here.
admin.site.register(Post) #관리자 사이트에 Post라는 클래스를 등록하기
```

- # Read
 1. views.py에서 데이터 가져오기
```python
def index(request):
    posts = Post.objects.all() #Post라는 클래스에 모든 데이터를 가져오는 함수
    context = {
        'posts': posts,
    }
    return render(request, 'index.html', context)
```
2. index.html에서 posts에 있는 데이터들을 반복문을 통해 출력
```html
<body>
    <h1>index</h1>
    {% for post in posts%}
        <p>{{post.title}}</p>
        <p>{{post.content}}</p>
        <hr>
    {% endfor %}
</body>
```