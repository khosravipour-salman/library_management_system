from django.shortcuts import render, get_object_or_404, redirect
from extra.models import CategoryModel, LikeModel, Contact
from book.models import BookModel
from accounting.models import CustomUserModel
from extra.forms import ContactForm, CategoryForm, PublisherForm


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
			return redirect('book:index')

	form = ContactForm()
	return render(request, 'extra/contact_us.html', {'form': form, })


def contact_list(request):
	context = {'obj_list': Contact.objects.all()}
	return render(request, 'extra/contact_list.html', context)


def staff_category_list(request):
	category_list_obj = CategoryModel.objects.all()
	return render(request, 'extra/staff_category_list.html', {'obj_list': category_list_obj})


def staff_category_delete(request, category_slug):
	category_obj = get_object_or_404(CategoryModel, slug=category_slug)
	if request.method == 'POST':
		category_obj.delete()
		return redirect('extra:category_list')

	return render(request, 'confirm_delete.html', {'obj': category_obj})


def staff_category_create(request):
	if request.method == 'POST':
		form = CategoryForm(request.POST)
		if form.is_valid():
			form.save()

			return redirect('extra:category_list')
	
	form = CategoryForm()
	return render(request, 'extra/staff_category_create.html', {'form': form})


def staff_category_update(request, category_slug):
	category_obj = get_object_or_404(CategoryModel, slug=category_slug)

	if request.method == 'POST':
		form = CategoryForm(request.POST, instance=category_obj)
		if form.is_valid():
			form.save()
			return redirect('extra:category_list')

	form = CategoryForm(instance=category_obj)
	return render(request, 'extra/staff_category_edit.html', {'form': form})
