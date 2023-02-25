from django import forms
from src.models import Admin  

class AdminForm(forms.ModelForm):  
    class Meta:  
        model=Admin
        fields = "__all__" 