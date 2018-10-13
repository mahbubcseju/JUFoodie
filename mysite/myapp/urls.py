from django.urls import path
from . import views

urlpatterns = [

    path('',views.index, name="index"),
    path('showmenue',views.showmenue, name="showmenue"),
    path('test', views.test, name="test"),
]