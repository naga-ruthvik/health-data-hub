from django.shortcuts import render
from .models import BookAppointment
# Create your views here.
def book_appointments(request):
    if request.method=='POST':
        name=request.POST['fullname']
        dob=request.POST['dob']
        gender=request.POST['gender']
        email=request.POST['email']
        phone=request.POST['phone']
        emergency_contact=request.POST['emergency_phone']
        hospital=request.POST['hospital']
        department=request.POST['department']
        time=request.POST['time']
        book_form=BookAppointment.objects.create(name=name,dob=dob,gender=gender,email=email,
                                        phone=phone,emergency_contact=emergency_contact,hospital=hospital,
                                        department=department,time=time)
        book_form.save()

    return render(request,'patient_templates/book_appointment.html')

def my_appointments(request):
    app=BookAppointment.objects.all()
    return render(request,'patient_templates/my_appointments.html',{'app_det':app})