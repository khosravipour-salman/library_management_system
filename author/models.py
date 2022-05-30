from django.db import models


class AuthorModel(models.Model):
    name = models.CharField(max_length=42)
    desc = models.TextField()

    def __str__(self):
        return self.name
