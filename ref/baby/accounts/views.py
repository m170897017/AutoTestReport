from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import RequestContext

from accounts.models import record
from accounts.forms import ContractForm

def hello1(request):
    
    return render_to_response('debug/search.html')


def hello2(request):
    
    info = request.META.keys()
    
    return HttpResponse('META is %s' % info)


def search(request):
    
    if request.method == 'POST':
        form = ContractForm(request.POST)
    else:
        form = ContractForm()
    # in case of csrf failure, we need to use requestcontext here    
    variables = RequestContext(request, {'form':form})
    return render_to_response('debug/contract_form.html', variables)
#    return render_to_response('debug/contract_form.html', {'form':form})