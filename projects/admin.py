from django.contrib import admin
from .models import Project


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_featured', 'is_active', 'order', 'created_at')
    list_filter = ('is_featured', 'is_active')
    list_editable = ('is_featured', 'is_active', 'order')
    search_fields = ('title', 'description', 'tech_stack')
    prepopulated_fields = {'slug': ('title',)}
    ordering = ('-is_featured', 'order', '-created_at')

    fieldsets = (
        (None, {
            'fields': ('title', 'slug', 'short_description', 'description')
        }),
        ('Images', {
            'fields': ('thumbnail', 'featured_image')
        }),
        ('Technical', {
            'fields': ('tech_stack',)
        }),
        ('Links', {
            'fields': ('github_url', 'live_url')
        }),
        ('Settings', {
            'fields': ('is_featured', 'is_active', 'order')
        }),
    )
