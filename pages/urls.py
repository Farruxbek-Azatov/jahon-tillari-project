from django.urls import path
from . import views

app_name = 'pages'
urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('check/', views.check, name='check'),
    path('apply/', views.apply_page, name='apply_page'),
]
