from django.db import models

# Create your models here.

class Department(models.Model):
    dep_name=models.CharField(max_length=20)
    dep_description=models.TextField()

    def __str__(self):
        return self.dep_name

class Doctors(models.Model):
    doc_name=models.CharField(max_length=200)
    doc_spec=models.CharField(max_length=200)
    dep_name=models.ForeignKey(Department,on_delete=models.CASCADE)
    doc_img=models.ImageField(upload_to='doctors')

    def __str__(self):
        return self.doc_name

class Booking(models.Model):
    p_name=models.CharField(max_length=255)
    p_phone=models.CharField(max_length=10)
    p_email=models.EmailField()
    doc_name=models.ForeignKey(Doctors,on_delete=models.CASCADE)
    booking_date=models.DateField()
    booked_on=models.DateField(auto_now=True)

class Contact(models.Model):
    f_name=models.CharField(max_length=255)
    l_name=models.CharField(max_length=255)
    pat_phone=models.CharField(max_length=10)
    pat_email=models.EmailField()
    remarks=models.TextField()

