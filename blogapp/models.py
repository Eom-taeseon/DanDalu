from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class Blog(models.Model): # Blog 모델을 생성. 이 모델은 앞으로 글 작성 모델이 될 것이다.
    title = models.CharField(max_length=100) # 제목. CharField로 최대 길이는 100글자
    pub_date = models.DateTimeField(auto_now_add=True) # 현재 시간을 그대로 받아와 저장해준다.
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, default=1) # 글쓴이에 대한 정보. django.contrib.auth.model에서 User값을 갖고오는데, 이 때의 User 값은 현재 로그인 한 인물에 대한 정보이다.
    body = RichTextUploadingField() # 글 작성을 전문으로 하는 ckeditor