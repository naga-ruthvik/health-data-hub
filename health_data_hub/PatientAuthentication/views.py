from django.shortcuts import render

# Create your views here.
def patient_log_home(request):
    return render(request,'patientAuthentication/PatientLog.html')

def host_login(request):
    return render(request,'patientAuthentication/HostLogin.html')

def patient_signup(request):
    return render(request,'patientAuthentication/PatientSignup.html')
