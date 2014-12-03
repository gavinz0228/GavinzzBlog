from django.shortcuts import render,HttpResponse
from .models import *

def home(request):

    visitor=Blog.isSetup()
    #return render(request,"index.html",{"Article":visitor});
    blog=Blog.objects.all()[0]
    return render(request,"index.html",{"blogInfo":blog,"blogList":"list"})
