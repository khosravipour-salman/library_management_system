from django.urls import path
from book import views

urlpatterns = [
	path('index/', views.book_list, name='book_list'),
	path('index/<str:filter_by>/<slug:filter_object>/', views.book_list_with_parameter, name='book_list_with_parameter'), 
	path('detail/<slug:slug>/', views.book_detail, name='book_detail'),
	path('advance-search/', views.advance_search, name='advance_search'),
	path('categories/', views.categories, name='categories'), 
	path('categories/<slug:category_slug>/', views.categories, name='categories_with_param'), 
	path('<slug:book_slug>/add-comment/', views.add_comment, name='add_comment'),
	path('add-to-bookmark/<slug:book_slug>/', views.add_to_bookmark, name='add_to_bookmark'),
]