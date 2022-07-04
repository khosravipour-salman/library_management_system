from django.db import models
from django.template.defaultfilters import slugify


class AuthorModel(models.Model):
    name = models.CharField(max_length=42)
    desc = models.TextField()
    slug = models.SlugField(unique=True, null=True)


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)
        
    def __str__(self):
        return self.name
