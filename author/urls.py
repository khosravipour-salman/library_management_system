from django.urls import path
from author import views


app_name = 'author'

urlpatterns = [
	# staff routes
	path('author-list/', views.staff_author_list, name='author_list'),
	path('author-create/', views.staff_author_create, name='author_create'),
	path('author-delete/<slug:author_slug>/', views.staff_author_delete, name='author_delete'),
	path('author-update/<slug:author_slug>/', views.staff_author_update, name='author_update')	
]