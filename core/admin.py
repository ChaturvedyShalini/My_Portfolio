from django.contrib import admin
from .models import SiteSettings, Skill, Achievement


@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    """Admin for site settings - singleton pattern"""
    fieldsets = (
        ('Personal Info', {
            'fields': ('name', 'title', 'email', 'phone', 'location')
        }),
        ('Hero Section', {
            'fields': ('hero_subtitle', 'typing_texts')
        }),
        ('About Section', {
            'fields': ('about_text', 'profile_image', 'resume_file')
        }),
        ('Social Links', {
            'fields': ('github_url', 'linkedin_url', 'twitter_url')
        }),
        ('Statistics', {
            'fields': ('projects_count', 'internships_count', 'certifications_count')
        }),
        ('SEO', {
            'fields': ('meta_description', 'meta_keywords'),
            'classes': ('collapse',)
        }),
    )

    def has_add_permission(self, request):
        return not SiteSettings.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'proficiency', 'order', 'is_active')
    list_filter = ('category', 'is_active')
    list_editable = ('proficiency', 'order', 'is_active')
    search_fields = ('name',)
    ordering = ('category', 'order', 'name')


@admin.register(Achievement)
class AchievementAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'is_featured', 'order')
    list_filter = ('is_featured',)
    list_editable = ('is_featured', 'order')
    search_fields = ('title', 'description')


# Customize admin site
admin.site.site_header = "Shalini's Portfolio Admin"
admin.site.site_title = "Portfolio Admin"
admin.site.index_title = "Manage Portfolio Content"
