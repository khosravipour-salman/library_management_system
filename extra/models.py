from django.db import models
from accounting.models import CustomUserModel
from book.models import BookModel


class LikeModel(models.Model):
    user = models.ForeignKey(CustomUserModel, on_delete=models.CASCADE)
    book = models.ForeignKey(BookModel, on_delete=models.CASCADE)
    vote = models.BooleanField()
    create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} liked {self.book.name}' if self.vote else f'{self.user.username} disliked {self.book.name}'


class PublisherModel(models.Model):
    name = models.CharField(max_length=42)
    address = models.TextField()

    def __str__(self):
        return self.name


class CategoryModel(models.Model):
    name = models.CharField(max_length=42, unique=True)

    def __str__(self):
        return self.name
