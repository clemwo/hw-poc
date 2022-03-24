from django.urls import path

from . import views

urlpatterns = [
    path('', views.project_list_view, name='index'),
    path('new', views.project_create, name='new'),
]