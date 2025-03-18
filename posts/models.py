from django.db import models

# Create your models here.

class Post(models.Model): #models.Model을 상속받아 Django에서 데이터베이스 테이블을 자동으로 생성
    title = models.CharField(max_length=100) 
    # CharField: 문자열, 최대 255자
    content = models.TextField()
    # TextField: 긴 문자열, 길이제한 없음