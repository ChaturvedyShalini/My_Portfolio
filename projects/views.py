from django.shortcuts import render, get_object_or_404
from .models import Project


def project_list(request):
    """List all projects"""
    projects = Project.objects.filter(is_active=True)
    return render(request, 'projects/list.html', {'projects': projects})


def project_detail(request, slug):
    """Project detail page"""
    project = get_object_or_404(Project, slug=slug, is_active=True)
    return render(request, 'projects/detail.html', {'project': project})
