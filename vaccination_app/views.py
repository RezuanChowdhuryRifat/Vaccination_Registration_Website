
from django.contrib import messages
from django import forms
from django.forms.forms import Form
from typing import List
from django.contrib import messages
from django.shortcuts import render
from django.utils.translation import templatize
from django.views.generic import TemplateView, ListView, FormView
from .registrationform import PostForm
from .vaccinecardform import PostForm
from .models import Address, Nid, Center, CenterAddress, Student, GovernmentEmployee, Citizen, MedicalPersonel, Registration, Volunteering








class AddressView(ListView):
    http_method_names = ["get"]
    model = CenterAddress
    template_name = "centerAddress.html"
    context_object_name = "centers"
    queryset = CenterAddress.objects.all().order_by('-id')[0:30]


class VaccinecardView(FormView):
    template_name = "vaccinationcard.html"
    form_class = PostForm


class RegistrationView(FormView):
    template_name = "registration.html"
    form_class = PostForm
