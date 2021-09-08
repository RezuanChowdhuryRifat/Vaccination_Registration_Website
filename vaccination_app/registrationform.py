from django import forms
from django.forms import widgets
from django.forms.fields import CharField

choice =(
    ('264923041', 'Nagar Matri Sadan'),
    ('413526234', 'Shaheed Sarwardi Medical College and Hospital'),
    ('525200792', 'Kuwait Bangladesh Friendship Hospital(Uttara)'),
    ('582216709', 'Bangabandhu Sheikh Mujib Medical University Hospital (BSMMU)'),
    ('598595316', 'BGB Hospital'),
)
class PostForm(forms.Form):
   
   NID  = forms.IntegerField()
   Date_of_Birth = forms.DateField(widget=forms.SelectDateWidget(years=range(1921,2004)))
   Phone_number  = forms.IntegerField()
   Center = forms.ChoiceField(choices=choice)
   CAPTCHA = forms.CharField()
 