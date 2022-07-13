from django.urls import path
from book import views

app_name = 'book'

urlpatterns = [
	path('index/', views.book_list, name='book_list'),
	path('index/<str:filter_by>/<slug:filter_object>/', views.book_list_with_parameter, name='book_list_with_parameter'), 
	path('detail/<slug:slug>/', views.book_detail, name='book_detail'),
	path('advance-search/', views.advance_search, name='advance_search'),
	path('<slug:book_slug>/add-comment/', views.add_comment, name='add_comment'),
	path('bookmark/', views.bookmark_list, name='bookmark_list'),
	path('add-to-bookmark/<slug:book_slug>/', views.remove_or_add_to_bookmark, name='add_to_bookmark'),
]