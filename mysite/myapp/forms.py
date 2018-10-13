from django import forms
from django.contrib.auth import get_user_model
from .models import menue

class showMenue(forms.ModelForm):
    image = forms.FileField(required=False)
    class Meta:
        model=menue
        fields=('foodtime' , 'foodname' , 'foodprice' , 'image', )