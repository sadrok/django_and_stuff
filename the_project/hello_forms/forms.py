from django import forms
from hello_forms.models import SiteUser

class FormName(forms.ModelForm):
    class Meta:
        model = SiteUser
        fields = '__all__'
