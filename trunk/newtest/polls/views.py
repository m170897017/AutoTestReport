# Create your views here.
from django.http import HttpResponse
import datetime
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render_to_response

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