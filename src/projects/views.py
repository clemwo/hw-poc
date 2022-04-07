from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from .models import Project
from .create_project_form import CreateProjectForm
from django.contrib import messages

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
            messages.success(request, "Projekt erfolgreich eingereicht")
            return HttpResponseRedirect('')
    else:
        create_project_form = CreateProjectForm()
    return render(request, 'projects/create_project.html', {'form': create_project_form})


def details(request, slug, pk):
    project = Project.objects.get(pk=pk)
    print(slug)
    print(project.slug)

    if not slug == project.slug:
        return HttpResponseNotFound('<h1>Seite nicht gefunden.</h1> Bist du dir sicher, dass die URL richtig ist?')
    context = {
        'project_object': project
    }
    return render(request, 'projects/details.html', context)