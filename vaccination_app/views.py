import os
from django.contrib import messages
from django import forms
from django.db.models.base import Model
from django.db.models.fields import BigIntegerField
from django.db.models.query import QuerySet
from django.forms.fields import JSONField, JSONString
from django.forms.forms import Form
from typing import List
from django.contrib import messages
from django.contrib.auth import settings
from django.shortcuts import redirect, render
from django.utils.translation import templatize
from django.views.generic import TemplateView, ListView, FormView
from .registrationform import PostForm
from .vaccinecardform import PostForm2
from .otpform import PostForm4
from .models import *
from django.http import HttpResponse, request
from django.http import HttpResponseRedirect 
from django.core.exceptions import ValidationError 
from django.db import connection
from datetime import date, datetime
from .Twilio import sendsms
from .OTPGenerator import gen_key,generate_code,verify_code


account_sid =os.environ.get("account_sid")
auth_token =os.environ.get("auth_token")


def HomePageView(request):
    return render(request, 'home.html')

def CovidCheckView(request):
    return render(request, 'covidcheck.html')

def FaqView(request):
    return render(request, 'faq.html')




class AddressView(ListView):
    http_method_names = ["get"]
    model = CenterAddress
    template_name = "centerAddress.html"
    context_object_name = "centers"
    queryset = CenterAddress.objects.all().order_by('id')
    
    
    


class VaccinecardView(FormView):
    template_name = "vaccinecard.html"
    form_class = PostForm2
    success_url='/otp'

    def form_valid(self, form):
        search_term=form.cleaned_data['NID']
        search_term2=form.cleaned_data['Date_of_Birth']
        valid = Nid.objects.filter(id=search_term)
        valid2 = Registration.objects.filter(nid=search_term).exists()
        if valid2:
          for objects in valid:
            if objects.dob == search_term2:
                 return super().form_valid(form)
            else:
              form.add_error('Date_of_Birth', 'Your date of birth is incorrect')
              return self.form_invalid(form)
        else:
              form.add_error('NID', 'You are not registered')
              return self.form_invalid(form)

class RegistrationView(FormView):
    template_name = "registration.html"
    form_class = PostForm
    success_url='/otp'
   
   

    def form_valid(self, form):
       
        search_term=form.cleaned_data['NID']
        search_term2=form.cleaned_data['Date_of_Birth']
        search_term3=form.cleaned_data['Phone_number']
        search_term4=form.cleaned_data['Center']
        today = date.today()
        user_age=  today.year-search_term2.year
        valid = Nid.objects.filter(id=search_term)
        valid2 = Registration.objects.filter(nid= search_term).exists()
        valid3 =Registration.objects.filter(mobile_no=search_term3).exists()
        valid4 = Nid.objects.filter(id=search_term).exists()
        if valid2:
            form.add_error('NID', 'You are already registered')
            return self.form_invalid(form)

        else:
            if valid3:
             form.add_error('Phone_number', 'This mobile number already registered')
             return self.form_invalid(form)
            else:
              for objects in valid:
                if valid4 and objects.dob == search_term2:
                 nid_obj = Nid.objects.get(id=form.cleaned_data['NID'])
                 center_obj = Center.objects.get(center_id=form.cleaned_data['Center'])
                 new_object = Registration.objects.create(
                  nid=nid_obj,
                  date = date.today(),
                  center=center_obj,
                  mobile_no=form.cleaned_data['Phone_number'],
                  age = user_age
                  )   
                 key = gen_key()
                 code = generate_code(key)
                 otp_obj = Otp.objects.create(
                    otpkey = code
                 ) 
                 msg_body =f'''
                 Covid-19 vaccine registration: Your OTP code:{code}
                 '''
                 sendsms(account_sid,auth_token,msg_body,'+12532011591',search_term3)
                 return super().form_valid(form)
                else:
                 form.add_error('NID', 'You are not eligible')
                 return self.form_invalid(form)

   


class OtpView(FormView):
    template_name = "otp.html"
    form_class=PostForm4
    success_url='/'
    def form_valid(self, form):
       search_term5 = form.cleaned_data['OTP'] 
       search_term6 = Otp.objects.filter(otpkey=search_term5).exists()
       print(search_term6)
       if search_term6:       
            messages.add_message(self.request, messages.SUCCESS, "You successfully registered")   
            return super().form_valid(form)
       else:
            form.add_error('OTP', 'Wrong OTP')
            return self.form_invalid(form)  
