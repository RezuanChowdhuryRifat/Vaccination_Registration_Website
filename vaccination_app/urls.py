from django.urls import path
from .views import AddressView,RegistrationView,VaccinecardView,OtpView
from . import views

app_name = 'vaccination_app'

urlpatterns = [

    path('', views.HomePageView, name='HomePageView'),
    path('covidcheck/', views.CovidCheckView, name='CovidCheckView'),
    path('faq/', views.FaqView, name='FaqView'),

    path('centeraddress/', AddressView.as_view(), name='centerAddress'),
    path('registration/', RegistrationView.as_view(), name='registration'),
    path('vaccinecard/', VaccinecardView.as_view(), name='vaccinationcard'),
    path('otp/', OtpView.as_view(), name='otp'),
   
]
