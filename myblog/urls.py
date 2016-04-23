from django.conf.urls import patterns, include, url
from django.contrib import admin
from blog1.views import index, info
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myblog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url (r'^index/', index),
    url (r'^info/', info)
)
