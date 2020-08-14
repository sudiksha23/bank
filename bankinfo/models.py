from django.conf import settings
from django.db import models

# Create your models here.
class EntrySignupQuerySet(models.QuerySet):
    pass

class EntrySignupManager(models.Manager):
    def get_queryset(self):
        return EntrySignupQuerySet(self.model, using=self._db)

class EntrySignup(models.Model):
    
    bank_name=models.CharField(max_length=122)
    address=models.CharField(max_length=122)
    state=models.CharField(max_length=122)
    district=models.CharField(max_length=122)
    branch=models.CharField(max_length=122)
    contact=models.IntegerField()
    ifsc=models.CharField(max_length=122,primary_key=True)
    micr=models.IntegerField()
    
    def __str__(self):
        return self.ifsc

    class meta:
        verbose_name = 'EntrySignup post'
        verbose_name_plural = 'EntrySignup posts'