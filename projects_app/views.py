from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Project
from .form import ProjectForm




def ProjectsView(request):
    data = Project.objects.all()
    context = {'projects': data}
    return render(request, 'projects.html', context=context)

@login_required(login_url='login')
def ProjectView(request, pk):
    data = Project.objects.get(pk=pk)
    context = {'project': data}
    return render(request, 'project.html', context=context)


@login_required(login_url='login')
def CreateProjectView(request):
    form = ProjectForm()
    if request.method == 'POST':
        data = ProjectForm(request.POST, request.FILES)
        if data.is_valid():
            form = data.save(commit=False)
            form.owner = request.user.profile
            form.save()
            return redirect('projects')
    context = {'form': form}
    return render(request, 'project-form.html', context=context)

@login_required(login_url='login')
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

@login_required(login_url='login')
def DeleteProjectView(request, pk):
    project = Project.objects.get(pk=pk)
    if request.method == 'POST':
        project.delete()
        return redirect('projects')
    context = {'object': project}
    return render(request, 'delete-confirm.html', context)
    