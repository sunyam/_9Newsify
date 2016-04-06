
from django import forms


class DocumentForm(forms.Form):

    docfile = forms.FileField(
        label='Select a file'
    )

    title = forms.CharField(label='Title', max_length=100)