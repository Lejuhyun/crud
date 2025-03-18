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

- post(앱) 안에 들어있는 views를 url.py에 불러오기 : from posts import views