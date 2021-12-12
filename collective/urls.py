from django.urls import path
from . import views

app_name = 'collective'
urlpatterns = [
    path('<slug:slug>/', views.employee, name='employee'),

]
