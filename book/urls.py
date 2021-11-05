from django.urls import path
from django.urls.resolvers import URLPattern
from . import views
app_name='book'

urlpatterns= [
    path('',views.index,name='index'),
    path('create', views.create, name="create"),
    path('linkdel/<bpk>', views.linkdel, name="linkdel")
]