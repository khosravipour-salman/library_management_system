from django import forms
from extra.models import Contact


class ContactForm(forms.ModelForm):
	class Meta:
		model = Contact
		fields = '__all__'