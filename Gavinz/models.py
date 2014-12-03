from django.db import models
from django.contrib import admin

class BlogAdmin(admin.ModelAdmin):
    def has_add_permission(self,request):
        if not Blog.isSetup():
            blog=Blog.objects.create(blogName="Gavin's Blog",contactInfo="Gavinz0228@gmail.com",owner="Gavin Zhang",intro="My name is Gavin",visitor=120)
            blog.save()
        return False

class Blog(models.Model):

    blogName=models.CharField(max_length=50)
    contactInfo=models.CharField(max_length=500)
    owner=models.CharField(max_length=50)
    intro=models.CharField(max_length=1000)
    picture=models.CharField(max_length=150)
    visitor=models.IntegerField()
    @staticmethod
    def isSetup():
        if Blog.objects.count()==0:
            blog=Blog.objects.create(blogName="Gavin's Blog",contactInfo="Gavinz0228@gmail.com",owner="Gavin Zhang",intro="My name is Gavin",visitor=120)
            blog.save()
        return True

