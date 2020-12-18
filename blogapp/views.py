from django.shortcuts import render, redirect, get_object_or_404
from .forms import CreateBlog
from .models import Blog

# Create your views here.

def index(request): # index 창에 대한 함수 정의
    return render(request, 'index.html') # blogapp/templates/index.html과 연결

def blogMain(request): # blogMain 창에 대한 함수 정의
    blogs = Blog.objects.all() # 같은 위치에 있는 models에서 Blog를 갖고옴

    return render(request, 'blogMain.html', {'blogs': blogs}) # blogapp/templates/blogMain.html과 연결.

def createBlog(request): # createBlog 창에 대한 함수 정의

    if request.method == "POST": # request.method가 POST형식인가
        form = CreateBlog(request.POST)

        if form.is_valid():
            form.save()
            return redirect('blogMain')
        else:
            return redirect('index')

    else:
        form = CreateBlog()
        return render(request, 'createBlog.html', {'form' : form})

def detail(request, blog_id): # detail 창에 대한 함수 정의
                              # 몇 번째 글인지 판별하기 위해 blog_id를 input값으로 받아온다. 이는 DB에서 primary key를 판별하기 위함이다.
    blog_detail = get_object_or_404(Blog, pk=blog_id) # get_object_or_404는 객체가 있으면 해당 객체를 반환하고, 없으면 404 error를 반환하는 것이다.

    return render(request, 'detail.html', {'blog_detail': blog_detail})