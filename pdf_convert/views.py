from django.shortcuts import render

from Vaccine_Registration.models import Nid, Registration, Center, Address, CenterAddress

from django.http import HttpResponse

from django.template.loader import get_template
from xhtml2pdf import pisa

# Create your views here.


#def show_info(request):
#    register_NID = Registration.NID
#    nid_fname = Nid.fname
#    nid_lname = Nid.lname
#    nid_dob = Nid.dob
#    address = Address.street_address
#    date = Registration.date
#    center_id = Center.center_id
#    center_name = Center.center_name
#    center_address = CenterAddress.street_address


def show_info(request):
    context = {
        'Nid': Registration.NID,
        'Fname': Nid.fname,
        'Lname': Nid.lname,
        'DOB': Nid.dob,
        'Address': Address.street_address,
        'Date of Registration': Registration.date,
        'Center_ID': Center.center_id,
        'Center_Name': Center.center_name,
        'Center_Address': CenterAddress.street_address,
    }
    return render(request, 'pdf_convert/ShowInfo.html', context)

def render_pdf_view(request):
    template_path = 'ShowInfo.html' # template_path = 'user_printer.html'
    context = {
        'Nid': Registration.NID,
        'Fname': Nid.fname,
        'Lname': Nid.lname,
        'DOB': Nid.dob,
        'Address': Address.street_address,
        'Date of Registration': Registration.date,
        'Center_ID': Center.center_id,
        'Center_Name': Center.center_name,
        'Center_Address': CenterAddress.street_address,
    } # context = {'myvar': 'this is your template context'}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="Vaccine-Card.pdf"' # Attachment enables it to be downloadable
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response) # dest=response; destination is response
    # if error then show some funy view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response