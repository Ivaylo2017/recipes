"""postproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
    This is the dispatcher - it tells the MVC what to display when certain URL is typed in by the user
     #$ in regex means stop don't show anything past me.
     <pk> implies primary key but you can specify any of the post attributes (for example slug) so that url is friendly to serach engine bots
"""
from django.conf.urls import url
from django.contrib import admin
from records import views #so that we can invoke the views.Post... method
from django.conf import settings
from django.conf.urls.static import static #This module manages static paths

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.PostListView.as_view(), name='list_posts'),
    url(r'^(?P<pk>\d+)/$',views.PostDetailView.as_view(), name='detail_post'),
    url(r'^create/$',views.CreatePostView.as_view(), name='create_post'),
    url(r'^(?P<pk>\d+)/update/$',views.UpdatePostView.as_view(), name='update_post'),
    url(r'^(?P<pk>\d+)/delete/$',views.DeletePostView.as_view(), name='delete_post'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
#This is how to add static path to pics or stuff that don't get moved around also you need to import settings from django.conf
