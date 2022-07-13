from django.db import models
from django.template.defaultfilters import slugify
from accounting.models import CustomUserModel
from book.models import BookModel


class CustomModelManager(models.Manager):
    def create(self, **obj_data):
        user_obj, book_obj, user_vote = obj_data.get('user'), obj_data.get('book'), obj_data.get('vote')
        like_obj = LikeModel.objects.filter(user=user_obj, book=book_obj)
        
        if like_obj.exists():
            like_obj = like_obj[0]

            if like_obj.vote == user_vote:
                like_obj.delete()

            elif like_obj.vote != user_vote:
                like_obj.vote = user_vote
                like_obj.save()

        else:
            super(CustomModelManager, self).create(**obj_data)


class LikeModel(models.Model):
    user = models.ForeignKey(CustomUserModel, on_delete=models.CASCADE)
    book = models.ForeignKey(BookModel, on_delete=models.CASCADE, related_name='likes')
    vote = models.BooleanField()
    create = models.DateTimeField(auto_now_add=True)

    objects = CustomModelManager()


    def total_likes(book_obj):
        return LikeModel.objects.filter(vote=True, book=book_obj).count()

    def __str__(self):
        return f'{self.user.user.username} liked {self.book.name}' if self.vote else f'{self.user.user.username} disliked {self.book.name}'


class PublisherModel(models.Model):
    name = models.CharField(max_length=42)
    address = models.TextField()
    slug = models.SlugField(unique=True, null=True)


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)
        
    def __str__(self):
        return self.name


class CategoryModel(models.Model):
    name = models.CharField(max_length=42)
    slug = models.SlugField(unique=True, null=True)


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)
        
    def __str__(self):
        return self.name
