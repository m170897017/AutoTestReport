from django.db import models
import datetime
from django.utils import timezone

# Create your models here.
class Poll(models.Model):
    # the name of each field instance(question or pub_date) will be used as column name
    question = models.CharField(max_length=200)
    # you can use an optional first positional argument to designate a human-readable name, such as date published
    pub_date = models.DateTimeField('date published')
    def __unicode__(self):
        return self.question
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently'
    
class Choice(models.Model):
    # that tells Django each Choice is related to a single Poll
    poll = models.ForeignKey(Poll)
    
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField()
    def __unicode__(self):
        return self.choice_text


