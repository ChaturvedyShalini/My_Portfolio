from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.http import JsonResponse
from .models import SiteSettings, Skill, Achievement
from projects.models import Project
from experience.models import Experience
from certifications.models import Certification
from contact.forms import ContactForm


def home(request):
    """Main portfolio page with all sections"""
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Save the message
            form.save()

            # Try to send email notification
            try:
                send_mail(
                    subject=f"Portfolio Contact: {form.cleaned_data['subject']}",
                    message=f"""
New contact form submission:

Name: {form.cleaned_data['name']}
Email: {form.cleaned_data['email']}
Subject: {form.cleaned_data['subject']}

Message:
{form.cleaned_data['message']}
                    """,
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=[settings.CONTACT_EMAIL],
                    fail_silently=True,
                )
            except Exception:
                pass  # Email sending is optional

            # Handle AJAX requests
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return JsonResponse({
                    'success': True,
                    'message': 'Thank you! Your message has been sent successfully.'
                })

            messages.success(request, 'Thank you! Your message has been sent successfully.')
            return redirect('core:home')
        else:
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return JsonResponse({
                    'success': False,
                    'errors': form.errors
                }, status=400)
            messages.error(request, 'There was an error with your submission. Please check the form and try again.')

    form = ContactForm()
    context = {
        'skills': Skill.objects.filter(is_active=True),
        'skills_programming': Skill.objects.filter(is_active=True, category='programming'),
        'skills_cloud': Skill.objects.filter(is_active=True, category='cloud'),
        'skills_visualization': Skill.objects.filter(is_active=True, category='visualization'),
        'projects': Project.objects.filter(is_active=True),
        'experiences': Experience.objects.filter(is_active=True),
        'certifications': Certification.objects.filter(is_active=True),
        'achievements': Achievement.objects.all(),
        'featured_achievements': Achievement.objects.filter(is_featured=True),
        'form': form
    }
    return render(request, 'core/home.html', context)


def about(request):
    """About page"""
    context = {
        'skills': Skill.objects.filter(is_active=True),
        'achievements': Achievement.objects.all(),
    }
    return render(request, 'core/about.html', context)


def custom_404(request, exception):
    """Custom 404 page"""
    return render(request, 'core/404.html', status=404)


def api_stats(request):
    """API endpoint for stats (used by counters)"""
    settings = SiteSettings.load()
    return JsonResponse({
        'projects': settings.projects_count or Project.objects.filter(is_active=True).count(),
        'internships': settings.internships_count or Experience.objects.filter(is_active=True).count(),
        'certifications': settings.certifications_count or Certification.objects.filter(is_active=True).count(),
    })
