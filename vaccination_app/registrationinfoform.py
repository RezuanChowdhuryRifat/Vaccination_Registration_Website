from django import forms
from django.db.models.enums import Choices
from django.forms import widgets
from django.forms.fields import CharField
from django.utils.regex_helper import Choice

choice_value= [('1', 'Dhaka'), ('2', 'Chittagong'), ('3', 'Khulna')]  
class PostForm3(forms.Form):
   Phone_number  = forms.IntegerField()
   Center = forms.ChoiceField(choices = choice_value)
   OTP = forms.IntegerField()
