from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog
from django.utils import timezone
# Create your views here.


def home(request):
    blogs = Blog.objects  # 쿼리셋(모델을 오브젝트의 목록으로 가져오는 것), 메소드
    # blog에 있는 object를 가져오겠다고 선언하는 것
    return render(request, 'home.html', {'blogs': blogs})


def detail(request, blog_id):
    # detail 페이지로 들어가면 그 게시글만의 본문 내용을 다 보여주어야함
    # detail에서 뭘 받아서 그 리턴 값으로
    details = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'detail.html', {'details': details})


def new(request):
    return render(request, 'new.html')


def create(request):
    blog = Blog()
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()
    blog.save()  # 쿼리메소드
    return redirect('home')


def edit(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'edit.html', {'blog': blog})

    # CRUD의 u인데 edit 수정할 게시글들을 가져오는 부분


def update(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()
    blog.save()  # 쿼리메소드
    return redirect('home')
# CRUD의 u 수정을 하고 다시 저장하는 부분


def delete(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    blog.delete()  # 쿼리메소드
    return redirect('home')
# CRUD의 D 게시글을 삭제하는 부분
