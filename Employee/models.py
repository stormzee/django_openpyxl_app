from django.db import models
# from django.utils import timezone
# import datetime
# # Create your models here.
# Create your views here.

from django.contrib.auth import get_user_model

User = get_user_model()

class Supervisor(models.Model):
    name = models.CharField(max_length=150, default=None)

    def __str__(self):
        return self.name

class Employee(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    age = models.DurationField(default=None, null=True)
    date_of_birth = models.DateTimeField(default=None)
    position = models.CharField(max_length=100, default=None, blank=True)
    department = models.CharField(max_length=100, default=None, blank=True)
    salary = models.FloatField(default=None, blank=True, null=True)
    supervisors = models.ManyToManyField(Supervisor, blank=True)
    Date_of_employment = models.DateField(default="2020-01-01", null=True)

    def __str__(self):
        return self.first_name + " " + self.last_name
    
    def get_age(self):
        import datetime
        self.age = (datetime.date.today() - self.date_of_birth)/365
        return self.age

    def save(self, *args, **kwargs):
        self.get_age()
        super(Employee, self).save(*args, **kwargs)


class UploadFile(models.Model):
    excel_data = models.FileField(upload_to='documents/')
    time_uploaded = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=200, blank=True)





    

   
