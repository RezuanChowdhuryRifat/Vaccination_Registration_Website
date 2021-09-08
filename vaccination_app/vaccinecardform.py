
from django import forms
from django.forms import widgets
from django.forms.fields import CharField


class PostForm2(forms.Form):
   
   NID  = forms.IntegerField()
   Date_of_Birth = forms.DateField(widget=forms.SelectDateWidget(years=range(1921,2004)))
   CAPTCHA = forms.CharField()
