from django import template
register = template.Library()

@register.inclusion_tag('nav_bar.html')
def nav_bar():
  return { 'nav_items':"sss", }