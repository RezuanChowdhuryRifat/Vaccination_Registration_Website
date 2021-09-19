from django import forms
from django.core.exceptions import ValidationError
from django.core import validators
from django.db.models.enums import Choices
from django.db.models.query import QuerySet
from django.forms import widgets
from django.forms.fields import CharField
from captcha.fields import CaptchaField
from .models import *

centers=(
     ('1', '----------'),
    ('264923041', 'Nagar Matri Sadan'),
    ('413526234', 'Shaheed Sarwardi Medical College and Hospital'),
    ('525200792', 'Kuwait Bangladesh Friendship Hospital(Uttara)'),
    ('582216709', 'Bangabandhu Sheikh Mujib Medical University Hospital (BSMMU)'),
    ('598595316', 'BGB Hospital'),
)
class PostForm(forms.Form):
   
   NID  = forms.CharField(validators=[validators.MaxLengthValidator(10)])
   Date_of_Birth = forms.DateField(widget=forms.SelectDateWidget(years=range(1921,2004)))
   Category = forms.ModelChoiceField(queryset= Categorylist.objects.all().values_list('list',flat=True))
   Phone_number  = forms.CharField(help_text="Please exclude country code Example: 1734983690",validators=[validators.MaxLengthValidator(10)])
   Center = forms.ChoiceField(choices=centers)
   CAPTCHA = CaptchaField()
