from django.db import models

# Create your models here.
class Upload(models.Model):
    patient_id=models.IntegerField()
    appointment_number=models.IntegerField()
    reports=models.FileField(upload_to='patient_files/')
    uploaded_at=models.DateTimeField(auto_now=True)
    
    def __int__(self):
        
        return self.appointment_number