from django.contrib import admin
from author.models import AuthorModel


class AuthorAdmin(admin.ModelAdmin):
    list_display = ("name", )
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(AuthorModel, AuthorAdmin)
