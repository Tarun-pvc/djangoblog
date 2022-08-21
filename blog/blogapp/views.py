from multiprocessing import context
from django.shortcuts import render, HttpResponse
from .models import Blog, Author, Book

# Create your views here.


def index(request):

    blogs = Blog.objects.all().filter(blog_published=True)
    context = {"blogs": blogs}
    return render(request, "./blogapp/index.html", context=context)


def blog(request):

    return HttpResponse("Blog")


def about(request):
    return HttpResponse("about page")


def authors(request):
    authors = Author.objects.all()
    context = {"authors": authors}
    return render(request, './blogapp/authors.html', context=context)


def authorblogs(request, id):
    blogs = Blog.objects.filter(blog_author=id)
    context = {"blogs": blogs}
    return render(request, './blogapp/authorblogs.html', context=context)
