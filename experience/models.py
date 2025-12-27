from django.db import models


class Experience(models.Model):
    """Work experience and internships"""
    EXPERIENCE_TYPE_CHOICES = [
        ('internship', 'Internship'),
        ('full_time', 'Full Time'),
        ('part_time', 'Part Time'),
        ('freelance', 'Freelance'),
        ('training', 'Training'),
    ]

    title = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    experience_type = models.CharField(
        max_length=50,
        choices=EXPERIENCE_TYPE_CHOICES,
        default='internship'
    )
    location = models.CharField(max_length=200, blank=True)

    # Dates
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    is_current = models.BooleanField(default=False)

    # Details
    description = models.TextField()
    responsibilities = models.TextField(
        blank=True,
        help_text="One responsibility per line"
    )
    technologies = models.CharField(
        max_length=500,
        blank=True,
        help_text="Comma-separated list of technologies used"
    )

    # Visual
    icon_class = models.CharField(
        max_length=100,
        blank=True,
        help_text="Icon class for timeline"
    )
    company_logo = models.ImageField(upload_to='experience/logos/', blank=True)

    # Meta
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['-start_date', 'order']
        verbose_name_plural = "Experiences"

    def __str__(self):
        return f"{self.title} at {self.company}"

    def get_responsibilities_list(self):
        """Return responsibilities as a list"""
        if not self.responsibilities:
            return []
        return [r.strip() for r in self.responsibilities.split('\n') if r.strip()]

    def get_technologies_list(self):
        """Return technologies as a list"""
        if not self.technologies:
            return []
        return [t.strip() for t in self.technologies.split(',') if t.strip()]

    def get_duration(self):
        """Return duration string"""
        if self.is_current:
            return f"{self.start_date.strftime('%b %Y')} - Present"
        if self.end_date:
            return f"{self.start_date.strftime('%b %Y')} - {self.end_date.strftime('%b %Y')}"
        return self.start_date.strftime('%b %Y')
