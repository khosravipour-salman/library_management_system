from django.contrib import admin
from book.models import BookModel, BookmarkModel, CommentModel


class BookAdmin(admin.ModelAdmin):
    list_display = ("name", "create", "user", "active", )
    prepopulated_fields = {"slug": ("name",)}

admin.site.register(BookModel, BookAdmin)

admin.site.register(BookmarkModel)
admin.site.register(CommentModel)