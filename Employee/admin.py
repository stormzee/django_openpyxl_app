from django.contrib import admin

# Register your models here.
from .models import Employee, Supervisor, UploadFile

admin.site.register(Employee)
admin.site.register(Supervisor)
admin.site.register(UploadFile)

