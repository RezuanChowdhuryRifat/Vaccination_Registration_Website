
from django.contrib import messages
from django import forms
from django.db.models.base import Model
from django.db.models.query import QuerySet
from django.forms.forms import Form
from typing import List
from django.contrib import messages
from django.shortcuts import redirect, render
from django.utils.translation import templatize
from django.views.generic import TemplateView, ListView, FormView
from .registrationform import PostForm
from .vaccinecardform import PostForm2
from .otpform import PostForm4
from .models import Address, Nid, Center, CenterAddress, Student, GovernmentEmployee, Citizen, MedicalPersonel, Registration, Volunteering
from django.http import HttpResponse, request
from django.http import HttpResponseRedirect 
from django.core.exceptions import ValidationError 
from django.db import connection
from datetime import date, datetime

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

    def form_valid(self, form):
        search_term=form.cleaned_data['NID']
        search_term2=form.cleaned_data['Date_of_Birth']
        valid = Nid.objects.filter(id=search_term)
        for objects in valid:
            if valid and objects.dob == search_term2:
                return super().form_valid(form)
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
        valid = Nid.objects.filter(id=search_term)
    

        print(search_term)
        for objects in valid:
            if valid and objects.dob == search_term2:
               
                return super().form_valid(form)
            else:
              form.add_error('NID', 'You are not eligible')
              return self.form_invalid(form)

   


class OtpView(FormView):
    template_name = "otp.html"
    form_class=PostForm4
    success_url='/'
    def form_valid(self, form):
       search_term5=form.cleaned_data['OTP']        
       messages.add_message(self.request, messages.SUCCESS, "You successfully registered")   
       return super().form_valid(form)
