from django.shortcuts import render, redirect

from .models import Project
from .form import ProjectForm




def ProjectsView(request):
    data = Project.objects.all()
    context = {'projects': data}
    return render(request, 'projects.html', context=context)

def ProjectView(request, pk):
    data = Project.objects.get(pk=pk)
    context = {'project': data}
    return render(request, 'project.html', context=context)

def CreateProjectView(request):
    form = ProjectForm()
    if request.method == 'POST':
        data = ProjectForm(request.POST, request.FILES)
        if data.is_valid():
            data.save()
            return redirect('projects')
    context = {'form': form}
    return render(request, 'project-form.html', context=context)


def UpdateProjectView(request, pk):
    project = Project.objects.get(pk=pk)
    form = ProjectForm(instance=project)
    if request.method == 'POST':
        data = ProjectForm(request.POST, instance=project)
        if data.is_valid():
            data.save()
            return redirect('projects')
    
    context = {'form': form}
    return render(request, 'project-form.html', context=context)


def DeleteProjectView(request, pk):
    project = Project.objects.get(pk=pk)
    if request.method == 'POST':
        project.delete()
        return redirect('projects')
    context = {'object': project}
    return render(request, 'delete-confirm.html', context)
    

def main_url(request):
    return render(request, 'home.html')

def profile(request, username):
    return render(request, 'profile.html', {'name':username})