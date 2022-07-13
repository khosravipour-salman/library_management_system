from django.shortcuts import render, get_object_or_404, redirect
from author.models import AuthorModel
from author.forms import AuthorForm
from accounting.models import CustomUserModel


def staff_author_list(request):
	author_list_obj = AuthorModel.objects.all()
	return render(request, 'author/staff_author_list.html', {'obj_list': author_list_obj})


def staff_author_delete(request, author_slug):
	author_obj = get_object_or_404(AuthorModel, slug=author_slug)
	if request.method == 'POST':
		author_obj.delete()
		return redirect('author:author_list')

	return render(request, 'confirm_delete.html', {'obj': author_obj})


def staff_author_create(request):
	user_obj = CustomUserModel.objects.get(user=request.user)

	if request.method == 'POST':
		form = AuthorForm(request.POST)
		if form.is_valid():
			form.save()

			return redirect('author:author_list')
	
	form = AuthorForm()
	return render(request, 'author/staff_author_create.html', {'form': form})


def staff_author_update(request, author_slug):
	author_obj = get_object_or_404(AuthorModel, slug=author_slug)

	if request.method == 'POST':
		form = AuthorForm(request.POST, instance=author_obj)
		if form.is_valid():
			form.save()
			return redirect('author:author_list')

	form = AuthorForm(instance=author_obj)
	return render(request, 'author/staff_author_edit.html', {'form': form})