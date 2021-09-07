
from django import forms
from django.forms import widgets
from django.forms.fields import CharField


class PostForm(forms.Form):
   
   NID  = forms.IntegerField()
   Date_of_Birth = forms.DateField(widget=forms.SelectDateWidget)
   CAPTCHA = forms.CharField()
