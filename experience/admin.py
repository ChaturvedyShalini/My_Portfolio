from django.contrib import admin
from .models import Experience


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('title', 'company', 'experience_type', 'start_date', 'is_current', 'is_active')
    list_filter = ('experience_type', 'is_current', 'is_active')
    list_editable = ('is_active',)
    search_fields = ('title', 'company', 'description')
    ordering = ('-start_date', 'order')

    fieldsets = (
        (None, {
            'fields': ('title', 'company', 'experience_type', 'location')
        }),
        ('Duration', {
            'fields': ('start_date', 'end_date', 'is_current')
        }),
        ('Details', {
            'fields': ('description', 'responsibilities', 'technologies')
        }),
        ('Visual', {
            'fields': ('icon_class', 'company_logo')
        }),
        ('Settings', {
            'fields': ('order', 'is_active')
        }),
    )
