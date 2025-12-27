from django.db import models


class Project(models.Model):
    """Portfolio projects"""
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    short_description = models.CharField(max_length=300)
    description = models.TextField()

    # Images
    thumbnail = models.ImageField(upload_to='projects/thumbnails/', blank=True)
    featured_image = models.ImageField(upload_to='projects/featured/', blank=True)

    # Tech stack (stored as comma-separated values)
    tech_stack = models.CharField(
        max_length=500,
        help_text="Comma-separated list of technologies"
    )

    # Links
    github_url = models.URLField(blank=True)
    live_url = models.URLField(blank=True)

    # Meta
    is_featured = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=0)
    created_at = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['-is_featured', 'order', '-created_at']

    def __str__(self):
        return self.title

    def get_tech_list(self):
        """Return tech stack as a list"""
        return [tech.strip() for tech in self.tech_stack.split(',') if tech.strip()]
