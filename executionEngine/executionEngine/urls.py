from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('index1', views.screen1, name='screen1'),
    path('index2', views.screen2, name='screen2'),
    path('index3', views.screen3, name='screen3'),
    path('index4', views.screen4, name='screen4'),
]