from django import forms 
from .models import EntrySignup
  
class EntrySignupForm(forms.ModelForm): 
    
    class Meta: 
        model = EntrySignup
        fields = ['bank_name','address','state','district','branch','contact','ifsc','micr'] 
 