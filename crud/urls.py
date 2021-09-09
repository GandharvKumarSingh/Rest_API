from django.contrib import admin
from django.urls import path, include
from crud import views

urlpatterns = [
    path('', views.studentList, name="students"),
    path('detail/<int:pk>/', views.studentDetail, name="detail"),
    path('create', views.studentCreate, name="create"),
    path('update/<int:pk>/', views.studentUpdate, name="update"),
    path('delete/<int:pk>/', views.studentDelete, name="delete")
]
