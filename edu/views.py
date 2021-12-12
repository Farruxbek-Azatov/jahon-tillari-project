from django.shortcuts import render
from .models import Subject, Book, Slide, Video


def subject_list(request):
    subjects = Subject.objects.all()
    return render(request, 'edu/subject_list.html', {'subjects': subjects})


def book_list(request, subject, course):
    books = Book.objects.filter(subject__slug=subject, course=course)
    return render(request, 'edu/book_list.html', {'books': books})


def slide_list(request, subject, course):
    slides = Slide.objects.filter(subject__slug=subject, course=course)
    return render(request, 'edu/book_list.html', {'slides': slides})


def video_list(request, subject, course):
    videos = Book.objects.filter(subject__slug=subject, course=course)
    return render(request, 'edu/book_list.html', {'videos': videos})


def online_lessons(request):
    subjects = Subject.objects.all()
    return render(request, 'edu/online_lessons.html', {'subjects': subjects})
