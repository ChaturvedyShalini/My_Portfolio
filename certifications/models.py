from django.db import models


class Certification(models.Model):
    """Professional certifications"""
    title = models.CharField(max_length=200)
    issuer = models.CharField(max_length=200)
    issue_date = models.DateField()
    expiry_date = models.DateField(blank=True, null=True)
    credential_id = models.CharField(max_length=200, blank=True)
    credential_url = models.URLField(blank=True)

    # Visual
    badge_image = models.ImageField(upload_to='certifications/badges/', blank=True)
    icon_class = models.CharField(max_length=100, blank=True)

    # Description
    description = models.TextField(blank=True)

    # Meta
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['order', '-issue_date']

    def __str__(self):
        return f"{self.title} - {self.issuer}"

    def is_valid(self):
        """Check if certification is still valid"""
        from django.utils import timezone
        if not self.expiry_date:
            return True
        return self.expiry_date >= timezone.now().date()
