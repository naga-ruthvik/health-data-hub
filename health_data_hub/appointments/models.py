from django.db import models
from phone_field import PhoneField
# Create your models here.
gender_choices=(
    ("male","male"),
    ("female","female"),
    ("other","other"),
)
department_choices=(
    ("Cardiology","Cardiology"), ("Neurology","Neurology"), ("Orthopedics","Orthopedics"),
    ("Dermatology","Dermatology"),("ENT","ENT"),("Gastroenterology","Gastroenterology"),
)
class BookAppointment(models.Model):
    name=models.CharField(max_length=200)
    dob=models.DateField()
    email=models.EmailField(null=True)
    gender=models.CharField(choices=gender_choices,max_length=20)
    phone=PhoneField(blank=True)
    emergency_contact=models.CharField(max_length=10)
    hospital=models.CharField(max_length=400,default='no hospital')
    department=models.CharField(max_length=200,choices=department_choices)
    time=models.TimeField()
