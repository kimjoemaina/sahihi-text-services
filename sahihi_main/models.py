from django.db import models
from django_quill.fields import QuillField

# Create your models here.
class PortfolioItem(models.Model):
    heading = models.CharField(max_length=120, blank=False)
    description = models.TextField(max_length=500, blank=False)
    sub_heading = models.CharField(max_length=120, blank=False)
    category = models.CharField(max_length=120, blank=True)
    image = models.ImageField(upload_to="photos/portfolio", blank=False)
    attribution = models.CharField(max_length=255, blank=True)
    completed_on = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'Portfolio Item'
        verbose_name_plural = 'Portfolio Items'

    def __str__(self):
        return self.heading

class TeamMember(models.Model):
    team_member_img = models.ImageField(upload_to="photos/team", blank=False)
    first_name = models.CharField(max_length=255, blank=False)
    last_name = models.CharField(max_length=255, blank=False)
    job_title = models.CharField(max_length=120, blank=False)
    facebook = models.URLField(max_length=255, blank=True)
    twitter = models.URLField(max_length=255, blank=True)
    linkedin = models.URLField(max_length=255, blank=True)
    joined_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        full_name = f'{self.first_name} {self.last_name}'
        return full_name

class BlogPost(models.Model):
    title = models.CharField(max_length=120, blank=False)
    sub_title = models.CharField(max_length=120, blank=True)
    slug = models.SlugField(max_length=120, unique=True, blank=False)
    content = QuillField(blank=False)
    published_on = models.DateTimeField(auto_now_add=True)
    publisher = models.CharField(max_length=120, blank=False)

    class Meta:
        ordering = ('-published_on',)

    def __str__(self):
        return self.title
