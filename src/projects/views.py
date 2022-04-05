from django.http import HttpResponse
from django.shortcuts import render

from .models import Project

from .create_project_form import CreateProjectForm

# Create your views here.

# CRUD Views

# List all the posts
def project_list_view(request):
    # get all the project objects
    project_objects = Project.objects.filter(status=Project.ACCEPTED)
    # create the context to be passed down to render
    context = {
        'project_objects': project_objects
    }
    return render(request, "projects/home.html", context)


def create_project_view(request):
    if request.method == "POST":
        create_project_form = CreateProjectForm(request.POST)
        if create_project_form.is_valid():
            project = create_project_form.save(commit=False)
            project.save()
    else:
        create_project_form = CreateProjectForm()
    return render(request, 'projects/create_project.html', {'form': create_project_form})