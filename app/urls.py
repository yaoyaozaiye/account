from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'all', views.MyModelView)

urlpatterns = [
    path('', views.index, name='index'),
    path('save/', views.create, name='save', kwargs={'id': None}),
    path('save/<int:id>', views.create, name='save'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('api/', include(router.urls)),
]

