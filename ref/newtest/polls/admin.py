from django.contrib import admin
from polls.models import Poll, Choice


# admin.site.register(Choice)

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class PollAdmin(admin.ModelAdmin):
    fieldsets = [
    ('line1',{'fields':['pub_date'],'classes':['collapse']}),
    ('line2',{'fields':['question'],'classes':['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question','pub_date')
    list_filter = ['pub_date']
    
admin.site.register(Poll,PollAdmin)