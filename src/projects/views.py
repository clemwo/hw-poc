from django.http import HttpResponse
from django.shortcuts import render

from .models import Project

# Create your views here.

# CRUD Views

# List all the posts
def project_list_view(request):
    # get all the project objects
    project_objects = Project.objects.all()
    # create the context to be passed down to render
    context = {
        'project_objects': project_objects
    }

    return render(request, "projects/home.html", context)


def project_create_view(request):
    return render(request, 'projects/create_project.html')