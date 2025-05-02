from django.shortcuts import render,redirect
from .models import Upload
# Create your views here.
def upload_files(request):
    if request.method=='POST':
        patient_id=request.POST['patient_id']
        appointment_number=request.POST['appointment_number']
        reports=request.FILES.get('reports')
        Upload.objects.create(patient_id=patient_id,appointment_number=appointment_number,reports=reports)
        
        

    return render(request,'host_templates/upload_files.html')