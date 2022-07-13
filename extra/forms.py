from django import forms
from extra.models import Contact, CategoryModel, PublisherModel


class ContactForm(forms.ModelForm):
	class Meta:
		model = Contact
		fields = '__all__'


class CategoryForm(forms.ModelForm):
	class Meta:
		model = CategoryModel
		exclude = ('slug', )


class PublisherForm(forms.ModelForm):
	class Meta:
		model = PublisherModel
		exclude = ('slug', )
		