
from django import forms
from django.forms import widgets
from django.forms.fields import CharField


class PostForm(forms.Form):
   
   NID  = forms.CharField()
   Date_of_Birth = forms.DateField(widget=forms.SelectDateWidget)
   CAPTCHA = forms.CharField()
