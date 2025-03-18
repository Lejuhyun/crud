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