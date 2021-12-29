from django.db.models import query
from django.shortcuts import render, get_object_or_404
from django.views.generic.list import ListView
from django.contrib.postgres.search import SearchVector
from .models import Post
from .forms import SearchForm


class PostListView(ListView):
    template_name = 'news/list.html'
    paginate_by = 5
    queryset = Post.published.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active'] = 'blog'
        return context


def post_detail(request, year, month, day, slug):
    post = get_object_or_404(Post, status='published',
                             slug=slug,
                             publish__year=year,
                             publish__month=month,
                             publish__day=day)
    return render(request, 'news/detail.html', {'post': post, 'active': 'blog'})


def search(request):
    search_vector = SearchVector(
        'title', 'title_ru', 'title_en', 'body', 'body_ru', 'body_en')
    query = request.GET.get('query')
    posts = Post.objects.annotate(search=search_vector).filter(search=query)
    return render(request, 'news/search.html', {'posts': posts, 'active': 'blog'})
