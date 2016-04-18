
from django import forms
from home_page.models import Document

class DocumentForm(forms.ModelForm):

    docfile = forms.FileField(
        label='Select a file'
    )
    title = forms.CharField(label='Title', max_length=100)
    #for categories
    INDIA = 'IN'
    WORLD = 'WO'
    SPORTS = 'SP'

    categoryChoices = (
    	(INDIA, 'India'),
    	(WORLD, 'World'),
    	(SPORTS, 'Sports'),
    	)
    categories = forms.ChoiceField(choices=categoryChoices,
    									required = True)

    class Meta:
        model = Document

        fields = ('title','docfile','categories')

    

