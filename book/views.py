from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from itertools import chain
from book.forms import AdvanceSearchForm
from book.models import BookModel
from author.models import AuthorModel
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
	context = {
		'book_obj': get_object_or_404(BookModel, slug=slug)
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
	paginator = Paginator(search_results.distinct(), 2)

	try:
		book_obj_list = paginator.page(page)
	except PageNotAnInteger:
		book_obj_list = paginator.page(1)
	except EmptyPage:
		book_obj_list = paginator.page(paginator.num_pages)

	return render(request, 'book/advance_search.html', {'obj_list': book_obj_list})
