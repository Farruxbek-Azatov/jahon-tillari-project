from django.shortcuts import render, get_object_or_404
from django.views.generic.list import ListView
from .models import Post


class PostListView(ListView):
    template_name = 'news/list.html'
    paginate_by = 5
    queryset = Post.published.all()


def post_detail(request, year, month, day, slug):
    post = get_object_or_404(Post, status='published',
                             slug=slug,
                             publish__year=year,
                             publish__month=month,
                             publish__day=day)
    return render(request, 'news/detail.html', {'post': post})
