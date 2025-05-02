from django.shortcuts import render

from appointments.models import BookAppointment
# Create your views here.
def see_appointments(request):
    app=BookAppointment.objects.all()
    return render(request,'host_templates/see_appointments.html',{'app_det':app})

