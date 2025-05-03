"""
URL configuration for health_data_hub project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

# PATIENT VIEWS
from patient_home import views as homeviews
from appointments import views as AppointmentViews
from patient_services import views as ServiceViews
from hospitals_nearby import views as HospitalView
from patient_account import views as PatientAccountViews
from MainHome import views as mainhomeview
from PatientAuthentication import views as PatAuthViews
# PATIENT VIEWS

# HOST VIEWS
from HostHome import views as HostHomeViews
from host_upload_files import views as UploadFileViews
from SeeAppointments import views as HostAppointmentsViews
from PatientAuthentication import views as PAuthViews
# HOST VIEWS

urlpatterns = [
    path('admin/', admin.site.urls),
    path('patient/',homeviews.home_page,name='patient_home'),
    path('book/',AppointmentViews.book_appointments,name='book_appointments'),
    path('patient/myappointments/',AppointmentViews.my_appointments,name='my_appointments'),
    path('services/',ServiceViews.service,name='services'),
    path('hospitals_nearby/',HospitalView.hospital,name='hospitals'),
    path('account/',PatientAccountViews.account,name='account'),
    path('account/medicalrecords',PatientAccountViews.medical_records,name='medical_records'),
    path('',mainhomeview.main_home,name='main_page'),
    path('patientlogin',PatAuthViews.patient_log_home,name='patient_login_home'),
    path('patientlogin/signup',PatAuthViews.patient_signup,name='patient_signup'),
    path('host/',HostHomeViews.host_home,name='host_home'),
    path('upload/',UploadFileViews.upload_files,name='uploadfiles'),
    path('hostappointments/',HostAppointmentsViews.see_appointments,name='host_appointments'),
    path('patient-login/',PAuthViews.patient_log_home,name='patientlogin'),
    path('host-login/',PAuthViews.host_login,name='hostlogin'),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
