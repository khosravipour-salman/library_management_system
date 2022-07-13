from django.shortcuts import render, get_object_or_404, redirect
from extra.models import CategoryModel, LikeModel, Contact
from book.models import BookModel
from accounting.models import CustomUserModel
from extra.forms import ContactForm


def categories(request, category_slug=None):
	category_list = CategoryModel.objects.all()
	context = {
		'category_list': category_list,
	}

	cat_obj = CategoryModel.objects.get(slug=category_slug) if category_slug else None
	if cat_obj is not None: context.update({'obj_list': cat_obj.books.all()}) 

	return render(request, 'book/categories.html', context)
	

def like_book(request, book_slug):
	book_obj = get_object_or_404(BookModel, slug=book_slug)
	user_obj = CustomUserModel.objects.get(user=request.user)
	LikeModel.objects.create(book=book_obj, user=user_obj, vote=True)

	return redirect(request.META.get('HTTP_REFERER'))


def dislike_book(request, book_slug):
	book_obj = get_object_or_404(BookModel, slug=book_slug)
	user_obj = CustomUserModel.objects.get(user=request.user)
	LikeModel.objects.create(book=book_obj, user=user_obj, vote=False)

	return redirect(request.META.get('HTTP_REFERER'))


def contact_us(request):
	if request.method == 'POST':
	
		form = ContactForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('book:book_list')

	form = ContactForm()
	return render(request, 'extra/contact_us.html', {'form': form, })


def contact_list(request):
	context = {'obj_list': Contact.objects.all()}
	return render(request, 'extra/contact_list.html', context)