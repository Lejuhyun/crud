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

- modeling (models.py)
```shell
from django.db import models
#Django의 데이터베이스 관련 기능을 제공하는 models 모듈을 가져옴
class Post(models.Model): 
#models.Model을 상속받아 Django에서 데이터베이스 테이블을 자동으로 생성
#models.Model을 상속하면 해당 클래스가 데이터베이스 테이블과 연결
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