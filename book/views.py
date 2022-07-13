from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q, Count
from itertools import chain
from book.forms import AdvanceSearchForm, CommentForm, BookForm
from book.models import BookModel, BookmarkModel
from author.models import AuthorModel
from accounting.models import CustomUserModel
from extra.models import PublisherModel
from extra.models import CategoryModel


def book_list(request):
	books = BookModel.active_book_manager.all()

	search = request.GET.get('search', 1)
	if search:
		books = BookModel.active_book_manager.filter(
			Q(name__icontains=search) | Q(author__name__icontains=search) |
			Q(publisher__name__icontains=search) | Q(translator__icontains=search) |
			Q(category__name__icontains=search)
		).distinct()

	page = request.GET.get('page', 1)
	paginator = Paginator(books, 12)

	try:
		book_obj_list = paginator.page(page)
	except PageNotAnInteger:
		book_obj_list = paginator.page(1)
	except EmptyPage:
		book_obj_list = paginator.page(paginator.num_pages)
	
	return render(request, 'book/index.html', {'obj_list': book_obj_list, })


def book_list_with_parameter(request, filter_by, filter_object):
	if filter_by == 'category': obj = CategoryModel.objects.get(slug=filter_object)
	elif filter_by == 'author':	obj = AuthorModel.objects.get(slug=filter_object)
	else: obj = PublisherModel.objects.get(slug=filter_object)

	books = BookModel.active_book_manager.filter(**{filter_by: obj})
	page = request.GET.get('page', 1)
	paginator = Paginator(books, 12)

	try:
		book_obj_list = paginator.page(page)
	except PageNotAnInteger:
		book_obj_list = paginator.page(1)
	except EmptyPage:
		book_obj_list = paginator.page(paginator.num_pages)

	context = {
		'obj_list': book_obj_list,
		'filter_field': filter_by,
		'filter_object': obj,		 
	}

	return render(request, 'book/index.html', context)


def book_detail(request, slug):
	book_obj = get_object_or_404(BookModel, slug=slug)

	book_category_ids = book_obj.category.values_list('id', flat=True)
	similar_books = BookModel.active_book_manager.filter(category__in=book_category_ids).exclude(id=book_obj.id)
	similar_books = similar_books.annotate(same_cats=Count('category')).order_by('-same_cats','-create')[:4]

	context = {
		'book_obj': book_obj,
		'similar_books': similar_books,
	}
	return render(request, 'book/detail.html', context)


def advance_search(request):
	qdict = {
		'bookname_icontain': 'name__icontains',
		'bookname_exact': 'name__exact',
		'pubname_icontain': 'publisher__name__icontains',
		'pubname_exact': 'publisher__name__exact',
		'authorname_icontain': 'author__name__icontains',
		'authorname_exact': 'author__name__exact',
	}

	form = AdvanceSearchForm(request.GET)
	if form.is_valid():
		q_objs = [Q(**{qdict[k]: form.cleaned_data[k]}) for k in qdict.keys() if form.cleaned_data.get(k, None)]
		search_results = BookModel.active_book_manager.filter(*q_objs)	

	page = request.GET.get('page', 1)
	paginator = Paginator(search_results.distinct(), 12)

	try:
		book_obj_list = paginator.page(page)
	except PageNotAnInteger:
		book_obj_list = paginator.page(1)
	except EmptyPage:
		book_obj_list = paginator.page(paginator.num_pages)

	return render(request, 'book/advance_search.html', {'obj_list': book_obj_list})


def add_comment(request, book_slug):
	book_obj = get_object_or_404(BookModel, slug=book_slug)
	user_obj = CustomUserModel.objects.get(user=request.user)

	if request.method == 'POST':
		form = CommentForm(request.POST)
		if form.is_valid():
			new_form = form.save(commit=False)
			new_form.user = user_obj
			new_form.book = book_obj
			new_form.save()
			return redirect('book:book_detail', slug=book_obj.slug)

	form = CommentForm()
	return render(request, 'book/add_comment.html', {'form': form})


def remove_or_add_to_bookmark(request, book_slug):
	book_obj = get_object_or_404(BookModel, slug=book_slug)
	user_obj = CustomUserModel.objects.get(user=request.user)

	bookmark_obj = BookmarkModel.objects.get(user=user_obj)
	if book_obj in bookmark_obj.book.all():
		bookmark_obj.book.remove(book_obj)
	else:
		bookmark_obj.book.add(book_obj)

	return redirect(request.META.get('HTTP_REFERER'))


def bookmark_list(request):
	user_obj = CustomUserModel.objects.get(user=request.user)

	bookmark_obj = BookmarkModel.objects.get(user=user_obj)
	books = bookmark_obj.book.all()

	return render(request, 'book/bookmark_list.html', {'obj_list': books})


def staff_book_list(request):
	book_list_obj = BookModel.active_book_manager.all()
	return render(request, 'book/list.html', {'obj_list': book_list_obj})


def staff_book_detail(request, book_slug):
	book_obj = get_object_or_404(BookModel, slug=book_slug)
	return render(request, 'book/staff_book_detail.html', {'obj': book_obj})


def staff_book_delete(request, book_slug):
	book_obj = get_object_or_404(BookModel, slug=book_slug)
	if request.method == 'POST':
		book_obj.delete()
		return redirect('book:book_list')

	return render(request, 'book/confirm_delete.html', {'obj': book_obj})


def staff_book_update(request, book_slug):
	book_obj = get_object_or_404(BookModel, slug=book_slug)
	user_obj = CustomUserModel.objects.get(user=request.user)

	if request.method == 'POST':
		form = BookForm(request.POST, request.FILES, instance=book_obj)
		if form.is_valid():
			new_form = form.save(commit=False)
			new_form.user = user_obj
			new_form.slug = new_form.name
			new_form.save()

			return redirect('book:book_list')
		else:
			print(form.errors)
	form = BookForm(instance=book_obj)
	return render(request, 'book/staff_book_edit.html', {'form': form})
