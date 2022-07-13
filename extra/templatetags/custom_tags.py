from django import template
from extra.models import LikeModel


register = template.Library()

@register.simple_tag
def total_likes_dislikes(book_obj, vote):
    return LikeModel.objects.filter(book=book_obj, vote=vote).count()