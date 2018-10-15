from django import forms
from django.contrib.auth import get_user_model
from .models import menue
from django.utils.safestring import mark_safe
from django.forms import widgets

class addMenue(forms.ModelForm):
    image = forms.FileField(required=False)
    class Meta:
        model=menue
        fields=('foodtime' , 'foodname' , 'foodprice' , 'image', )


#
# class HorizontalRadioRenderer(forms.RadioSelect.renderer):
#    def render(self):
#      return mark_safe(u'\n'.join([u'%s\n' % w for w in self]))




CHOICES = [('Breakfast', 'Breakfast'),
               ('lunch', 'lunch'),
               ('Dinner','Dinner'),
           ('all','all')
           ]


class searchMenue(forms.Form):
    # css_style = 'style="display: inline-block; margin-right: 10px;"'
    search = forms.ChoiceField(label="Search menue for ",choices=CHOICES,initial=0,widget=forms.Select())