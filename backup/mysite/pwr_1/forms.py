#from django import newforms as forms
from django import forms
import re
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

class test_records(forms.Form):
    
    record = forms.CharField(max_length=10)
    record_1 = forms.CharField(max_length=10)
    
    def __unicode__(self):
        return 'test_record!!!!'
    
    
    
class RegistrationForm(forms.Form):
    username = forms.CharField(label='Username', max_length=30)
    email    = forms.EmailField(label='E-mail')
    password1= forms.CharField(label='Password', widget=forms.PasswordInput())
    password2= forms.CharField(label='Password confirmed', widget=forms.PasswordInput())
    
    def clean_username(self):
        ''' used for verify user validation '''
        
        username = self.cleaned_data['username']
        if not re.search(r'\w+$', username):
            raise forms.ValidationError('Only character or number or underline is allowed!')
        try:
            User.objects.get(username=username)
        except ObjectDoesNotExist:
            return username
        raise forms.ValidationError('User already exists!!')
    
    def clean_email(self):
        ''' used for verify e-mail address '''
        
        email = self.cleaned_data['email']
        try:
            User.objects.get(email=email)
        except ObjectDoesNotExist:
            return email
        raise forms.ValidationError('E-mail already exists!!')
    
    def clean_password2(self):
        ''' used for confirmed password twice '''
        
        if 'password1' in self.cleaned_data:
            pswd1 = self.cleaned_data['password1']
            pswd2 = self.cleaned_data['password2']
            if pswd1 == pswd2:
                return pswd2
            else:
                raise forms.ValidationError('Confirmed password failed!!')
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    
    
    
    