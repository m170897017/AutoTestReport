from django.contrib import admin
from accounts.models import record

# manage model
class Record_admin(admin.ModelAdmin):
    
    list_display = ('date',)
#    search_fields = ('date',)
    list_filter = ('date',)



admin.site.register(record, Record_admin)
