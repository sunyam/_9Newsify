from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from home_page.models import Document
from home_page.forms import DocumentForm

# def home(request):
#     return render(request, 'home_page/home.html')

def cat_india(request):
    return render(request, 'home_page/cat_india.html')

def cat_world(request):
    return render(request, 'home_page/cat_world.html')

def cat_sports(request):
    return render(request, 'home_page/cat_sports.html')

def cat_misc(request):
    return render(request, 'home_page/cat_misc.html')




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

def cat_india(request):
    # Load documents for the list page
    documents = Document.objects.all()

    # Render list page with the documents and the form
    return render_to_response(
        'home_page/cat_india.html', #'list.html',
        {'documents': documents},
        context_instance=RequestContext(request)
    )

def cat_world(request):
    # Load documents for the list page
    documents = Document.objects.all()

    # Render list page with the documents and the form
    return render_to_response(
        'home_page/cat_world.html', #'list.html',
        {'documents': documents},
        context_instance=RequestContext(request)
    )

def cat_sports(request):
    # Load documents for the list page
    documents = Document.objects.all()

    # Render list page with the documents and the form
    return render_to_response(
        'home_page/cat_sports.html', #'list.html',
        {'documents': documents},
        context_instance=RequestContext(request)
    )

def cat_misc(request):
    # Load documents for the list page
    documents = Document.objects.all()

    # Render list page with the documents and the form
    return render_to_response(
        'home_page/cat_misc.html', #'list.html',
        {'documents': documents},
        context_instance=RequestContext(request)
    )
