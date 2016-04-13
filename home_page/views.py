from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from home_page.models import Document
from home_page.forms import DocumentForm

# def home(request):
#     return render(request, 'home_page/home.html')



def login(request):
    return render(request, 'home_page/login.html')

def home(request):
    
    # Handle file upload
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)

        if form.is_valid():
            # newdoc = Document(docfile=request.FILES['docfile'])
            # newdoc.save()
            form.save()
            # Redirect to the document list after POST
            return HttpResponseRedirect(reverse('home_page.views.home'))
    else:
        form = DocumentForm()  # A empty, unbound form
  

    
    # Load documents for the list page
    documents = Document.objects.all()

    # Render list page with the documents and the form
    return render_to_response(
        'home_page/home.html', #'list.html',
        {'documents': documents, 'form': form},
        context_instance=RequestContext(request)
    )

