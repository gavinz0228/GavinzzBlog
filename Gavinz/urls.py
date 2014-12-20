from django.conf.urls import patterns, include, url

from django.contrib import admin
from . import views
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Gavinz.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r"^profile/",views.profile),
    url(r"^articles/$",views.articles),
    url(r"^articles/(?P<currentPage>[0-9]+)/$",views.articles),
    url(r"^contactus/",views.contactus),
    url(r"(?P<currentPage>[0-9]+)",views.home),
    url(r"",views.home),


)
