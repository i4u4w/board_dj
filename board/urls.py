from django.urls import path
from . import views

app_name = "board"
urlpatterns = [
    path('', views.index, name="index"),
    path('detail/<bpk>', views.detail, name="detail"),
    path('delete/<bpk>', views.delete, name="delete"),
    path('create', views.create, name="create"),
    path('create_reply/<bpk>', views.create_reply, name="create_reply"),
    path('remove_reply/<rpk>/<bpk>', views.remove_reply, name="remove_reply"),
    path('addup/<bpk>', views.addup, name="addup"),
    path('removeup/<bpk>', views.removeup, name="removeup")
]