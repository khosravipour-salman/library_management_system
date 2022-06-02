from django.db import models
from accounting.models import CustomUserModel
from loan.models import LoanModel


class BookModel(models.Model):
    name = models.CharField(max_length=42)
    cover = models.ImageField(upload_to='book_cover', default='default.jpg')
    create = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    desc = models.TextField()
    translator = models.CharField(max_length=42)
    publisher = models.ForeignKey("extra.PublisherModel", related_name='books', on_delete=models.CASCADE)
    category = models.ManyToManyField("extra.CategoryModel")
    author = models.ManyToManyField("author.AuthorModel")
    user = models.ForeignKey(CustomUserModel, on_delete=models.DO_NOTHING, related_name='books')
    active = models.BooleanField(default=True)
    loan = models.ForeignKey("loan.LoanModel", on_delete=models.CASCADE, related_name='books')

    def __str__(self):
        return self.name


class BookmarkModel(models.Model):
    user = models.OneToOneField(CustomUserModel, on_delete=models.CASCADE)
    book = models.ManyToManyField("book.BookModel")
    create = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user} has {self.book.count()}'


class CommentModel(models.Model):
    user = models.ForeignKey(CustomUserModel, on_delete=models.CASCADE)
    book = models.ForeignKey("book.BookModel", on_delete=models.CASCADE)
    title = models.CharField(max_length=16)
    content = models.TextField()
    create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} comment on {self.book.name}'

