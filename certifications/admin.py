from django.contrib import admin
from .models import Certification


@admin.register(Certification)
class CertificationAdmin(admin.ModelAdmin):
    list_display = ('title', 'issuer', 'issue_date', 'is_active', 'order')
    list_filter = ('issuer', 'is_active')
    list_editable = ('is_active', 'order')
    search_fields = ('title', 'issuer', 'description')
    ordering = ('order', '-issue_date')

    fieldsets = (
        (None, {
            'fields': ('title', 'issuer', 'description')
        }),
        ('Dates', {
            'fields': ('issue_date', 'expiry_date')
        }),
        ('Credentials', {
            'fields': ('credential_id', 'credential_url')
        }),
        ('Visual', {
            'fields': ('badge_image', 'icon_class')
        }),
        ('Settings', {
            'fields': ('order', 'is_active')
        }),
    )
