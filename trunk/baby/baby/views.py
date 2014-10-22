from django.http import HttpResponse
from django.shortcuts import render_to_response

def hello(request):
    name = 'lch'
    return render_to_response('debug/hello.html', {'name':name})