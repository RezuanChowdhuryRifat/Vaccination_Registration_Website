import os
from django.contrib import messages
from django import forms
from django.db.models.base import Model
from django.db.models.query import QuerySet
from django.conf import settings
from django.forms.forms import Form
from typing import List
from django.contrib import messages
from django.contrib.auth import settings
from django.http.response import JsonResponse
from django.shortcuts import redirect, render
from django.urls.base import reverse
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
from django.template.loader import get_template
from xhtml2pdf import pisa
from importlib import import_module
from django.contrib.sessions.backends.db import SessionStore
from django.contrib.auth.decorators import login_required

account_sid =os.environ['account_sid']
auth_token =os.environ['auth_token']


def HomePageView(request):
    return render(request, 'home.html')

def CovidCheckView(request):
    return render(request, 'covidcheck.html')

def FaqView(request):
    return render(request, 'faq.html')




class AddressView(ListView):
    http_method_names = ["get"]
    model = Center
    template_name = "centeraddress.html"
    context_object_name = "centers"
    queryset = Center.objects.all().order_by('center_address')

  
      
def VaccinecardView(request):

    form_class = PostForm2
    # if request is not post, initialize an empty form
    form = form_class(request.POST or None)
    if request.method == 'POST':
      
        if form.is_valid():
            search_term=form.cleaned_data['NID']
            search_term2=form.cleaned_data['Date_of_Birth']
            valid = Nid.objects.filter(id=search_term)
            valid2 = Registration.objects.filter(nid=search_term).exists()
            if valid2:
             for objects in valid:
              if objects.dob == search_term2:
                human = True
                search_term3 = Registration.objects.get(nid=search_term).mobile_no 
                
                request.session['NID'] = search_term
                key = gen_key()
                code = generate_code(key)
                otp_obj = Otp.objects.create(
                    otpkey = code
                 ) 
                msg_body =f'''
                 Covid-19 vaccine registration: Your OTP code:{code}
                 '''
                sendsms(account_sid,auth_token,msg_body,'+19287560208','+880'+str(search_term3))
                return redirect('/votp')

            else:
              form.add_error('Date_of_Birth', 'Your date of birth is incorrect')
        else:
              form.add_error('NID', 'You are not registered')
              form = PostForm2()  

    context = {
        'form': form
    }

    return render(request, 'vaccinecard.html', context)

# class VaccinecardView(FormView):
#     template_name = "vaccinecard.html"
#     form_class = PostForm2
#     success_url = 'showInfo/'

#     def form_valid(self, form):
#         search_term=form.cleaned_data['NID']
#         search_term2=form.cleaned_data['Date_of_Birth']
#         valid = Nid.objects.filter(id=search_term)
#         valid2 = Registration.objects.filter(nid=search_term).exists()
#         if valid2:
#           for objects in valid:
#             if objects.dob == search_term2:
#                 human = True

#                 request.session['NID'] = 'search_term'

#                 return super().form_valid(form)
#             else:
#               form.add_error('Date_of_Birth', 'Your date of birth is incorrect')
#               return self.form_invalid(form)
#         else:
#               form.add_error('NID', 'You are not registered')
#               return self.form_invalid(form)

class RegistrationView(FormView):
    template_name = "registration.html"
    form_class = PostForm
    success_url='/otp'
   
   

    def form_valid(self, form):
       
        search_term=form.cleaned_data['NID']
        search_term2=form.cleaned_data['Date_of_Birth']
        search_term3=form.cleaned_data['Phone_number']
        search_term4=form.cleaned_data['Center']
        if search_term4 == '1':
            form.add_error('Center', 'Please choose a center')
            return self.form_invalid(form)
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
                 human = True
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
                 sendsms(account_sid,auth_token,msg_body,'+19287560208','+880'+search_term3)
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

class VacOtpView(FormView):
    template_name = "votp.html"
    form_class=PostForm4
    success_url='/showInfo'
    def form_valid(self, form):
       search_term5 = form.cleaned_data['OTP'] 
       search_term6 = Otp.objects.filter(otpkey=search_term5).exists()
       print(search_term6)
       if search_term6:    
       
            return super().form_valid(form)
       else:
            form.add_error('OTP', 'Wrong OTP')
            return self.form_invalid(form)              

def show_info(request):
    id = request.session['NID']


    registration = Registration.objects.get(nid=id)
    center_id = Registration.objects.get(nid=id).center
    
    nid = Nid.objects.get(id=id)

    address_id = Nid.objects.get(id=id).address
    center = Center.objects.get(center_id = center_id.center_id)
   
    address = Address.objects.get(id=address_id.id)
    center_address= Center.objects.get(center_id = center_id.center_id).center_address



    return render(request, 'ShowInfo.html',  {'nid': nid, 'registration':registration,'address':address,'center':center,'center_id':center_address})


def renderpdfview(request):

    id = request.session['NID']
    del request.session['NID']


    registration = Registration.objects.get(nid=id)
    center_id = Registration.objects.get(nid=id).center
    
    nid = Nid.objects.get(id=id)

    address_id = Nid.objects.get(id=id).address
    center = Center.objects.get(center_id = center_id.center_id)
   
    address = Address.objects.get(id=address_id.id)
    center_address= Center.objects.get(center_id = center_id.center_id).center_address
    template_path = 'renderpdf.html' # template_path = 'user_printer.html'

    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="VaccineCard.pdf"' # Attachment enables it to be downloadable
    # find the template and render it.
    template = get_template(template_path)
    html = template.render({'nid': nid, 'registration':registration,'address':address,'center':center,'center_id':center_address})

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response) # dest=response; destination is response
    # if error then show some funy view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

@login_required(login_url='/login')
def AdminView(request):
    count = Registration.objects.all().count()
    count2 = Nid.objects.all().count() - count
    return render(request,'admin.html',{'count':count,'count2':count2})


def AdminpanelView(request):
    count = Registration.objects.all().count()
    count2 = Nid.objects.all().count() - count
    print(count)
    print(count2)
    if request.method == "POST":
      Categorylist.objects.all().delete()   
      Government_employee= request.POST.get('1')
      Medical_personnel = request.POST.get('2')
      Volunteer = request.POST.get('3')
      Student = request.POST.get('4')
      Citizen = request.POST.get('5')
      if Government_employee != None:
         new_object = Categorylist.objects.create(
             list = "Government employee"
         )
      if Medical_personnel != None:
         new_object = Categorylist.objects.create(
             list = "Medical personnel"
         ) 
      if Volunteer != None:
         new_object = Categorylist.objects.create(
             list = "Volunteer"
         ) 
      if Student != None:
         new_object = Categorylist.objects.create(
             list = "Student"
         )
      if Citizen != None:
         new_object = Categorylist.objects.create(
             list = "Citizen"
         )   

    return render(request,'adminpanel.html',{'count':count,'count2':count2})
   
  

def LoginView(request):
    if request.method == "POST":  
     admin_mail= request.POST.get('email')
     admin_pass = request.POST.get('password')
     if admin_mail == "vaccination@gov.io" and admin_pass =="covid-19":
         return render(request,'admin.html')
     
         
    return render(request,'login.html')    