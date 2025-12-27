from .models import SiteSettings


def site_context(request):
    """Add site settings to all templates"""
    return {
        'site_settings': SiteSettings.load()
    }
