
from django import forms
from home_page.models import Document

class DocumentForm(forms.ModelForm):

    docfile = forms.FileField(
        label='Select a file'
    )
    title = forms.CharField(label='Title', max_length=100)
    class Meta:
        model = Document

        fields = ('title','docfile')

    

