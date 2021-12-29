from django.urls import path
from . import views

app_name = 'edu'
urlpatterns = [
    path('', views.subject_list, name='subject_list'),
    path('books/<slug:subject>/<course>/',
         views.book_list, name='book_list'),
    path('slides/<slug:subject>/<course>/',
         views.slide_list, name='slide_list'),
    path('videos/<slug:subject>/<course>/',
         views.video_list, name='video_list'),
    path('online_lessons/', views.online_lessons, name='online_lessons'),
    path('directions/', views.directions, name='directions'),
]
