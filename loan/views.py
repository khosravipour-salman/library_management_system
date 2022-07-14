from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from loan.models import LoanModel, DebtModel
from accounting.models import CustomUserModel
from book.models import BookModel


def loan_basket(request):
	user_obj = CustomUserModel.objects.get(user=request.user)
	loan_obj_list = LoanModel.objects.filter(user=user_obj, status='C')
	if not loan_obj_list.exists():
		loan_obj = LoanModel.objects.create(user=user_obj, status='C')
	else: loan_obj = loan_obj_list[0]

	return render(request, 'loan/loan_basket.html', {'loan_obj': loan_obj})


def add_to_loan(request, book_slug):
	book_obj = get_object_or_404(BookModel, slug=book_slug)
	user_obj = CustomUserModel.objects.get(user=request.user)
	loan_obj_list = LoanModel.objects.filter(user=user_obj, status='C')

	loan_list = [loan_obj.books.all() for loan_obj in LoanModel.objects.filter(Q(status='S'), Q(status='T')) if loan_obj.book.all is not None]

	if not loan_obj_list.exists():
		loan_obj = LoanModel.objects.create(user=user_obj, status='C')

	else: loan_obj = loan_obj_list[0]

	if request.user.is_staff:
		book_limit = 7
	else:
		book_limit = 5

	if book_obj not in loan_obj.books.all() and book_obj not in loan_list and loan_obj.books.count() < book_limit:
		loan_obj.books.add(book_obj)

	return redirect(request.META.get('HTTP_REFERER'))	


def remove_from_loan(request, book_slug):
	book_obj = get_object_or_404(BookModel, slug=book_slug)
	user_obj = CustomUserModel.objects.get(user=request.user)
	loan_obj_list = LoanModel.objects.filter(user=user_obj, status='C')

	if not loan_obj_list.exists():
		loan_obj = LoanModel.objects.create(user=user_obj, status='C')

	else: loan_obj = loan_obj_list[0]

	if book_obj in loan_obj.books.all():
		loan_obj.books.remove(book_obj)

	return redirect(request.META.get('HTTP_REFERER'))	
