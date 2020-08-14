from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from . import views
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from django.conf.urls.static import static 
from bankinfo import views
from bankinfo import models
from bankinfo import forms
#from bankinfo.views import *

#routers = routers.DefaultRouter()

#routers.register(r'EntrySignups', views.EntrySignupViewSet)

urlpatterns = [
    #path('', include(routers.urls)),
    
   # path('admin', admin.site.urls),
    path("", views.index, name='home'),
    path("index",views.index, name='index'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path("searchtable1",views.searchtable1, name="entry"),
    path("searchtable2",views.searchtable2, name="entry"),
    #path("entrysignup", views.entrysignup, name="entry"),
    #path('entrysignup/', views.entrysignup_list),
    #re_path(r'^api/(?P<ifsc>\w+)/$', views.EntrySignupsViewSet.as_view()),
    #re_path(r'^api/(?P<ifsc>\w+)/$', views.BanksViewSet.as_view()),
    #re_path(r'^api/(?P<bank_name>[\w\ ]+)/(?P<city>[\w\ ]+)/$', views.EntrySignupViewSet2.as_view()),
    
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)