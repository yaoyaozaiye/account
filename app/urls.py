# @Time: 2023/6/24 21:23
# @Author: 田莉
# @File: urls.py
# @Software: PyCharm
from django.urls import path

from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('create', views.create, name='create'),
    path('delete/<int:id>', views.delete, name='delete')
]