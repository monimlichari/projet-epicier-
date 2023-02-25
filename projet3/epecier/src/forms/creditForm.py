from django import forms
from src.models import Credit  

class CreditForm(forms.ModelForm):  
    class Meta:  
        model=Credit
        fields = "__all__" 