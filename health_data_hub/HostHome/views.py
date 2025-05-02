from django.shortcuts import render

# Create your views here.
def host_home(request):
    return render(request,'host_templates/index.html')