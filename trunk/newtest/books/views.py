# Create your views here.
from django.shortcuts import render_to_response
from django.http import HttpResponse
import datetime
from django.template.loader import get_template
from django.template import Context
from books.models import Book
from django.core.mail import send_mail

def hours_ahead(request, offset):
    offset = int(offset)
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    return render_to_response('hours_ahead.html',{'hour_offset':offset,'next_time':dt})
    


def current_datetime(request):
    now = datetime.datetime.now()
    return render_to_response('current_datetime.html',{'current_date':now})

def base_view(request):
    info = request.META.items()
    info.sort()
    return HttpResponse('this is %s' % info)

def search_form(request):
    return render_to_response('search_form.html')

def search(request):
    errors = []
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            errors.append('Enter a search term.')
        elif len(q) > 20:
            errors.append('Please enter at most 20.')
        else:
            books = Book.objects.filter(title__icontains=q)
            return render_to_response('search_results.html',{'books':books,'query':q})
    
    return render_to_response('search_form.html',{'errors':errors})
#        message = 'You searched for:%r' % request.GET['q']
#    else:
#        message = 'You submitted an empty form.'
#    return HttpResponse(message)

def contact(request):
    errors = []
    if request.method == 'POST':
        if not request.POST.get('subject',''):
            errors.append('enter a subject')
        if not request.POST.get('message',''):
            errors.append('enter a message')
        if request.POST.get('email') and '@' not in request.POST['email']:
            errors.append('enter a valid e-mail address')
        if not errors:
            send_mail(request.POST['subject'],
                      request.POST['message'],
                      request.POST.get('email','noreply@example.com'),['linchenhang@tp-link.net'],
                      )
            return HttpResponseRedirect('/contact/thanks/')
    return render_to_response('contact_form.html',
                              {'errors':errors,
                               'subject':request.POST.get('subject',''),
                               'message':request.POST.get('message',''),
                               'email':request.POST.get('email',''),
                               })
        
        
        
        
        
        
        
        
