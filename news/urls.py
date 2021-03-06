from django.urls import path
from . import views

app_name = 'news'
urlpatterns = [
    path('', views.PostListView.as_view(), name='post_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:slug>/',
         views.post_detail, name='post_detail'),
    path('search/', views.search, name='search'),
]
