from .models import UploadFile, Employee
from django import forms


class UploadFileForm(forms.ModelForm):
    
    class Meta:
        model = UploadFile
        fields = ("excel_data",)

class EmployeeCreationForm(forms.ModelForm):
    date_of_birth = forms.DateTimeField()
    class Meta:
        model = Employee
        fields = "__all__"