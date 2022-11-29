from django.shortcuts import render
from django.views.generic import View, DetailView, ListView
from .models import Article, HashTag, Course


class HomePage(View):
    def get(self, request, *args, **kwargs):
        articles = Article.objects.all()[0:4]
        context = {
            'posts': articles
        }
        return render(request, 'home.html', context)


class Posts(View):
    def get(self, request, *args, **kwargs):
        articles = Article.objects.all()
        categories = HashTag.objects.all()
        context = {
            'posts': articles,
            'categories': categories
        }
        return render(request, 'posts.html', context)


class PostDetailView(View):
    template_name: str = 'post-detail.html'

    def get(self, request, pk, *args, **kwargs):
        post = Article.objects.get(pk=pk)
        categories = HashTag.objects.all()
        context = {
            'object': post,
            'categories': categories
        }

        return render(request, self.template_name, context)


class CategoryView(DetailView):
    model = HashTag
    template_name: str = 'category-detail.html'


class CourseListView(ListView):
    model = Course
    template_name: str = 'course-list.html'


class CourseDetailView(DetailView):
    model = Course
    template_name: str = 'course-detail.html'
