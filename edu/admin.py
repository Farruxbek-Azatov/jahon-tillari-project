from django.contrib import admin
from .models import OnlineLesson, Subject, Book, Slide, Video


# class BookInline(admin.StackedInline):
#     model = Book


# class SlideInline(admin.StackedInline):
#     model = Slide


# class VideoInline(admin.StackedInline):
#     model = Video


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}
    # inlines = [BookInline, SlideInline, VideoInline]


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('subject', 'name', 'course', 'book')


@admin.register(Slide)
class SlideAdmin(admin.ModelAdmin):
    list_display = ('subject', 'name', 'course', 'slide')


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('subject', 'name', 'course', 'url')


@admin.register(OnlineLesson)
class OnlineLessonAdmin(admin.ModelAdmin):
    list_display = ('subject', 'name', 'url')
