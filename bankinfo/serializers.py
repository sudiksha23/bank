from rest_framework import serializers
from .models import EntrySignup
#from django.contrib.auth.models import EntrySignup

class EntrySignupSerializer(serializers.ModelSerializer):
    class meta:
        model = EntrySignup
        fields = ('bank_name','address','state','district','branch','contact','ifsc','micr')
    #fields = '__all__'