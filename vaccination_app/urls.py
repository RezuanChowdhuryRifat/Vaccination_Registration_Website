from django.urls import path
from .views import AddressView,RegistrationView,OtpView
from . import views

app_name = 'vaccination_app'

urlpatterns = [

    path('', views.HomePageView, name='HomePageView'),
    path('covidcheck/', views.CovidCheckView, name='CovidCheckView'),
    path('faq/', views.FaqView, name='FaqView'),

    path('centeraddress/', AddressView.as_view(), name='centerAddress'),
    path('registration/', RegistrationView.as_view(), name='registration'),
    path('vaccinecard/', views.VaccinecardView, name='vaccinationcard'),
    path('otp/', OtpView.as_view(), name='otp'),
    path('showInfo/', views.show_info, name='showInfo'),
    path('vaccineCardpdf/', views.renderpdfview, name='vaccineCardpdf')
   
]
