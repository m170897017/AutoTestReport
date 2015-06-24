#!/usr/bin/env python
# -*- coding:utf-8 -*-

from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_protect
from django.template import RequestContext
from django.core.mail import send_mail
from django.http import HttpResponseRedirect

import forms

def index(request):
    #    form = forms.test_records()
    #    if request.user.is_authenticated():
    #        sess_info = 'is authenticated!!'
    #    else:
    #        sess_info = 'is not authenticated!!'
    #    return render_to_response('index.html',{'form':form})
    #    return HttpResponse('this is my sessions: %s ...' % sess_info)
    return HttpResponseRedirect('/admin/')


def test(request):
    #    send_mail(u'test1',u'test2','170897017@qq.com',['linchenhang@tp-link.com.cn'],fail_silently=False)
    send_mail(u'test1', u'test2', 'linchenhang@tp-link.net', ['linchenhang@tp-link.net'], fail_silently=False)
    return HttpResponse('send e-mail successfully!!!')


@csrf_protect
def register_page(request):
    if request.method == 'POST':
        form = forms.RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(username=form.clean_username(),
                                            password=form.clean_password2(),
                                            email=form.clean_email())
            user.is_staff = True
            user.issuperset
            user.groups.add(1)
            user.save()

        else:
            return render_to_response('register_errors.html', {'errors': str(form.errors)})

        return HttpResponseRedirect('/admin/')
    else:
        form = forms.RegistrationForm()
        # in case of csrf error, requestcontext should be used here
        variables = RequestContext(request, {'form': form})
        return render_to_response('register.html', variables)
