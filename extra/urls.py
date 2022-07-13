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

	# staff routes
	path('category-list/', views.staff_category_list, name='category_list'),
	path('category-create/', views.staff_category_create, name='category_create'),
	path('category-delete/<slug:category_slug>/', views.staff_category_delete, name='category_delete'),
	path('category-update/<slug:category_slug>/', views.staff_category_update, name='category_update'),	

	# path('publisher-list/', views.staff_publisher_list, name='publisher_list'),
	# path('publisher-create/', views.staff_publisher_create, name='publisher_create'),
	# path('publisher-delete/<slug:publisher_slug>/', views.staff_publisher_delete, name='publisher_delete'),
	# path('publisher-update/<slug:publisher_slug>/', views.staff_publisher_update, name='publisher_update'),	
]