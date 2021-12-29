from django.shortcuts import render
from .models import Subject, Book, Slide, Video


def subject_list(request):
    subjects = Subject.objects.all()
    return render(request, 'edu/subject_list.html', {'subjects': subjects, 'active': 'edu'})


def book_list(request, subject, course):
    books = Book.objects.filter(subject__slug=subject, course=course)
    return render(request, 'edu/book_list.html', {'books': books, 'active': 'edu'})


def slide_list(request, subject, course):
    slides = Slide.objects.filter(subject__slug=subject, course=course)
    return render(request, 'edu/slide_list.html', {'slides': slides, 'active': 'edu'})


def video_list(request, subject, course):
    videos = Video.objects.filter(subject__slug=subject, course=course)
    return render(request, 'edu/video_list.html', {'videos': videos, 'active': 'edu'})


def online_lessons(request):
    subjects = Subject.objects.all()
    return render(request, 'edu/online_lessons.html', {'subjects': subjects, 'active': 'edu'})


def directions(request):
    return render(request, 'direction.html', {'active': 'edu'})
