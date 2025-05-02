from django.shortcuts import render
from host_upload_files.models import Upload
# Create your views here.
def account(request):
    return render(request,'patient_templates/account.html')

def medical_records(request):
    report_files=Upload.objects.all()
    return render(request,'patient_templates/medical_records.html',{'report_files':report_files})