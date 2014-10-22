from django.db import models



class record(models.Model):
    
    date = models.DateField(verbose_name='Date')
    
    money_earn = models.FloatField(verbose_name='Input')
    money_consume = models.FloatField(verbose_name='Output')
    
    # decide what record display
    def unicode(self):
        return self.date
    
    # decide order of record
    class Meta:
        ordering = ['date']
    
