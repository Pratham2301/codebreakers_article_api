from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # path('', views.home),
    path('all-articles', views.get_all_articles),
    path('article/<slug:pk>', views.get_article_by_name),
    path('create', views.create_article),
    path('update/<int:pk>', views.update_article),
    path('delete/<int:pk>', views.delete_article),
]
