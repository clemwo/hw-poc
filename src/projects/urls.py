from django.urls import path

from . import views

urlpatterns = [
    path('', views.project_list_view, name='index'),
    path('new', views.create_project_view, name='new'),
]