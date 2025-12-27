from django.db import models


class SiteSettings(models.Model):
    """Global site settings - singleton model"""
    name = models.CharField(max_length=100, default="Shalini Chaturvedy")
    title = models.CharField(max_length=200, default="Data Analyst | Cloud & ML Enthusiast")
    email = models.EmailField(default="shalini.chaturvedy@example.com")
    phone = models.CharField(max_length=20, blank=True)
    location = models.CharField(max_length=200, default="Bengaluru, Karnataka, India")

    # Hero section
    hero_subtitle = models.TextField(default="Transforming data into actionable insights")
    typing_texts = models.TextField(
        help_text="Comma-separated list of texts for typing effect",
        default="Data Analyst,Cloud & ML Enthusiast,Python Developer"
    )

    # About section
    about_text = models.TextField(blank=True)
    profile_image = models.ImageField(upload_to='profile/', blank=True)
    resume_file = models.FileField(upload_to='documents/', blank=True)

    # Social links
    github_url = models.URLField(blank=True)
    linkedin_url = models.URLField(blank=True)
    twitter_url = models.URLField(blank=True)

    # Stats
    projects_count = models.PositiveIntegerField(default=0)
    internships_count = models.PositiveIntegerField(default=0)
    certifications_count = models.PositiveIntegerField(default=0)

    # Meta
    meta_description = models.TextField(blank=True)
    meta_keywords = models.CharField(max_length=500, blank=True)

    class Meta:
        verbose_name = "Site Settings"
        verbose_name_plural = "Site Settings"

    def __str__(self):
        return "Site Settings"

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)

    @classmethod
    def load(cls):
        obj, created = cls.objects.get_or_create(pk=1)
        return obj


class Skill(models.Model):
    """Skills with categories and proficiency levels"""
    CATEGORY_CHOICES = [
        ('programming', 'Programming & Data'),
        ('cloud', 'Cloud & Systems'),
        ('visualization', 'Visualization'),
        ('other', 'Other'),
    ]

    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    proficiency = models.PositiveIntegerField(
        default=80,
        help_text="Proficiency level 0-100"
    )
    icon_class = models.CharField(
        max_length=100,
        blank=True,
        help_text="Font Awesome or custom icon class"
    )
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['category', 'order', 'name']

    def __str__(self):
        return f"{self.name} ({self.get_category_display()})"


class Achievement(models.Model):
    """Achievements and research highlights"""
    title = models.CharField(max_length=200)
    description = models.TextField()
    icon_class = models.CharField(max_length=100, blank=True)
    date = models.DateField(blank=True, null=True)
    link = models.URLField(blank=True)
    is_featured = models.BooleanField(default=False)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order', '-date']

    def __str__(self):
        return self.title
