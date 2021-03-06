
from django import forms
from django.forms import widgets
from django.core import validators 
from django.forms.fields import CharField
from captcha.fields import CaptchaField


class PostForm2(forms.Form):
   
   NID  = forms.CharField(validators=[validators.MaxLengthValidator(10)])
   Date_of_Birth = forms.DateField(widget=forms.SelectDateWidget(years=range(1921,2004)))
   CAPTCHA = CaptchaField()
