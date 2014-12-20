from django.shortcuts import render,HttpResponse
from .models import *
from django.core.paginator import Paginator
pageSize=20
#import html.parser

def home(request,currentPage="1"):
    #visitor=Blog.isSetup()
    #return render(request,"index.html",{"Article":visitor});
    blog=Blog.objects.all()[0]
    p=Paginator(Article.objects.order_by('createDate').all().reverse(),pageSize)
    page=p.page(int(currentPage))
    pageContent=page.object_list
    return render(request,"index.html",{"blogInfo":blog,"articles":pageContent,"pageCount":p.page_range,"currentPage":currentPage})
    #return HttpResponse(str(count(articles)))
def profile(request):
    return render(request,"profile.html",{"content":"content"})
def articles(request):
    return render(request,"articles.html",{"articles":Article.objects.order_by('createDate').all().reverse()[0:5]})
def articles(request,currentPage="1"):
    p=Paginator(Article.objects.order_by('createDate').all().reverse(),pageSize)
    page=p.page(int(currentPage))
    pageContent=page.object_list
    return render(request,"articles.html",{"articles":pageContent,"pageCount":p.page_range,"currentPage":currentPage})


def contactus(request):
    return render(request,"contactus.html",{"contactInfo":"sdf"})
