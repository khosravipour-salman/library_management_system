from django.urls import path
from extra import views

app_name = 'extra'

urlpatterns = [
	path('categories/', views.categories, name='categories'), 
	path('categories/<slug:category_slug>/', views.categories, name='categories_with_param'), 
	path('like-book/<slug:book_slug>/', views.like_book, name='like_book'),
	path('dis-like-book/<slug:book_slug>/', views.dislike_book, name='dislike_book'),
	path('contact-us/', views.contact_us, name='contact_us'),
	path('contact-us-message-list/', views.contact_list, name='contact_list'),
]