from django import forms
from author.models import AuthorModel


class AuthorForm(forms.ModelForm):
	class Meta:
		model = AuthorModel
		exclude = ('slug', )