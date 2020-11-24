
from django.urls import path
from . import views


urlpatterns = [
    path('',views.index, name='index'),
    path('uploads/', views.Uploads, name='uploads'),
    path('create-employee', views.createEmployee, name='createEmployee'),
    path('login/', views.login, name='login'),
    path('Records/', views.all_employees, name='records')
]
