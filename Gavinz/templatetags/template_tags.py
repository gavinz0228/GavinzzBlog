from django import template
from Gavinz.models import *
register = template.Library()

@register.inclusion_tag('category.html')
def category():
  return { 'category':ArticleType.objects.all() }
@register.inclusion_tag('intro.html')
def intro():
  return { 'blogInfo':Blog.objects.all()[0] };