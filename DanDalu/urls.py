"""DanDalu URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.conf import settings
from django.conf.urls.static import static
import blogapp.views # blogapp/views.py 를 import함.


urlpatterns = [
    path('admin/', admin.site.urls), # admin창으로 연결.
    path('', blogapp.views.index, name='index'), # blogapp/views.py -> def index에 연결. 해당 path의 이름은 index
    path('blogMain/', blogapp.views.blogMain, name='blogMain'), # blogapp/views.py -> def blogMain에 연결. 해당 path의 이름은 blogMain
    path('blogMain/createBlog/', blogapp.views.createBlog, name='createBlog'), # blogapp/views.py -> def createBlog에 연결. 해당 path의 이름은 createBlog
    path('ckeditor/', include('ckeditor_uploader.urls')), # ckeditor 주소로 이동.
    path('blogMain/detail/<int:blog_id>', blogapp.views.detail, name='detail'), # blogapp/views.py -> def detail에 연결. 해당 path의 이름은 detail
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)