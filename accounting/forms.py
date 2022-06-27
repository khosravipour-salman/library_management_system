from django import forms
from django.contrib.auth.models import User
from accounting.models import CustomUserModel


class LoginForm(forms.Form):
	username = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput())


class CompleteProfileForm(forms.ModelForm):
	first_name = forms.CharField(max_length=124, required=False)
	last_name = forms.CharField(max_length=124, required=False)	
	email = forms.EmailField(required=False)

	class Meta:
		model = CustomUserModel
		fields = (
			'age', 'phone_number', 'gender',
			'address', 'national_code',
			'first_name', 'last_name', 'email', 
		)
