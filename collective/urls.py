from django.urls import path
from . import views

app_name = 'collective'
urlpatterns = [
    path('adminstration/', views.adminstration, name='adminstration'),
    path('<slug:slug>/', views.employee, name='employee'),

]
