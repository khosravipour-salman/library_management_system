from django.contrib import admin
from book.models import BookModel, BookmarkModel


admin.site.register(BookModel)
admin.site.register(BookmarkModel)
