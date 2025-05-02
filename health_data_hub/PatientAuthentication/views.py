from django.shortcuts import render

# Create your views here.
def patient_log_home(request):
    return render(request,'patientAuthentication/PatientLog.html')

def patient_signin(request):
    return render(request,'patientAuthentication/PatientSignin.html')

def patient_signup(request):
    return render(request,'patientAuthentication/PatientSignup.html')
