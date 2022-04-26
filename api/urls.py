from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_articles),
    path('article/<int:pk>', views.article),
    path('create', views.create),
    path('update/<int:pk>', views.update),
    path('delete/<int:pk>', views.delete),
]
