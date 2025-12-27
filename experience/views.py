from django.shortcuts import render
from .models import Experience


def experience_list(request):
    """List all experiences"""
    experiences = Experience.objects.filter(is_active=True)
    return render(request, 'experience/list.html', {'experiences': experiences})
