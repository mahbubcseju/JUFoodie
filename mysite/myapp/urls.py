from django.urls import path
from . import views

urlpatterns = [

    path('',views.index, name="index"),
    path('addmenue',views.addmenue, name="addmenue"),
    path('showmenue',views.showmenue, name="showmenue"),
    path('ordermenue/<int:id>/',views.ordermenue, name="ordermenue"),
    path('test', views.test, name="test"),
]