from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User
import datetime
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
class ArticleType(models.Model):
    desc=models.CharField(max_length=100)
    def __unicode__(self):
        return self.desc
class Article(models.Model):
    title=models.CharField(max_length=100)
    content=models.CharField(max_length=10000)
    visitor=models.IntegerField()
    createDate=models.DateTimeField()
    author=models.ForeignKey(User)
    category=models.ForeignKey(ArticleType)
    def __unicode__(self):
        return str(self.title)

admin.site.register(Blog)
admin.site.register(Article)
admin.site.register(ArticleType)

def registerModel():
    admin.site.register(Blog)
    admin.site.register(Article)
    admin.site.register(ArticleType)
#if __title__=="__main__":
#    registerModel()


