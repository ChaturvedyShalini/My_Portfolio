from django.shortcuts import render
from .models import Certification


def certification_list(request):
    """List all certifications"""
    certifications = Certification.objects.filter(is_active=True)
    return render(request, 'certifications/list.html', {'certifications': certifications})
