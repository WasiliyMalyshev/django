from django.urls import path
from . import views

urlpatterns=[
    path("", views.curdate_index, name = "curdate_index"),

]