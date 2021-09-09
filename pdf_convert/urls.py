from django.urls import path
from . import views

urlpatterns = {
    path('showInfo', views.show_info, name='showInfo'),
    path('VaccineCard-pdf', views.render_pdf_view, name='VaccineCard-pdf')
}