from django.contrib import admin
from polls.models import Poll, Choice

#admin.site.register(Poll)

class ChoiceInline(admin.TabularInline):
    model = Choice
    
    # you will get three extra slots when you come to this page everytime
    extra = 3

class PollAdmin(admin.ModelAdmin):
    fieldsets = [
              (None, {'fields':['question']}),
              ('Date information', {'fields':['pub_date'],'classes':['collapse']}),
              ]
    inlines = [ChoiceInline]
    list_display = ('question', 'pub_date', 'was_published_recently')
    list_filter  = ['pub_date']
    search_fields = ['question']
    date_dierarchy = 'pub_date'
    
admin.site.register(Poll, PollAdmin) 








