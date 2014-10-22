from django import forms

class ContractForm(forms.Form):
    
    subject = forms.CharField(max_length=100)
    email = forms.EmailField(required=False, label='Your e-mail addr')
    message = forms.CharField(widget=forms.Textarea)
    