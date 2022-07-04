from django import forms
from book.models import CommentModel


class AdvanceSearchForm(forms.Form):
	bookname_icontain = forms.CharField(required=False)
	bookname_exact = forms.CharField(required=False)
	pubname_icontain = forms.CharField(required=False)
	pubname_exact = forms.CharField(required=False)
	authorname_icontain = forms.CharField(required=False)
	authorname_exact = forms.CharField(required=False)

	class Meta:
		fields = (
			'bookname_icontain', 'bookname_exact', 'pubname_icontain', 
			'pubname_exact', 'authorname_icontain', 'authorname_exact', 
		)


class CommentForm(forms.ModelForm):
	title = forms.CharField()
	content = forms.Textarea()

	class Meta:
		model = CommentModel
		fields = ('title', 'content', )
