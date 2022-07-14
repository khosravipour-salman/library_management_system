from django.urls import path
from loan import views


app_name = 'loan'

urlpatterns = [
	path('loan-basket/', views.loan_basket, name='loan_basket'),
	path('add-to-loan/<slug:book_slug>/', views.add_to_loan, name='add_to_loan'),
	path('remove-from-loan/<slug:book_slug>/', views.remove_from_loan, name='remove_from_loan'),
]