from django.contrib import admin
from extra.models import PublisherModel, CategoryModel, LikeModel

class PublisherAdmin(admin.ModelAdmin):
    list_display = ("name", )
    prepopulated_fields = {"slug": ("name",)}


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", )
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(PublisherModel, PublisherAdmin)
admin.site.register(CategoryModel, CategoryAdmin)
admin.site.register(LikeModel)