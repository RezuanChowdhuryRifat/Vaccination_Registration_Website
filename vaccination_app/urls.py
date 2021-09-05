from django.urls import path
from .views import AddressView,RegistrationView,VaccinecardView

app_name = 'vaccination_app'

urlpatterns = [

    path('centeraddress/', AddressView.as_view(), name = 'centerAddress'),
    path('registration/', RegistrationView.as_view(), name = 'registration'),
    path('vaccinecard/', VaccinecardView.as_view(), name = 'vaccinationcard'),
   
]