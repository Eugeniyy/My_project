from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView

from .models import News, Category
from .forms import NewsForm

# Create your views here.

class HomeNews(ListView):
    model = News
    template_name = 'news/home_news_list.html'
    context_object_name = 'news'
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Home Page'
        return context
    
    def get_queryset(self):
        return News.objects.filter(is_published=True)
    
class NewsByCategory(ListView):
    model = News
    template_name = 'news/home_news_list.html'
    context_object_name = 'news'
    allow_empty = False # запретить показ пустых списков
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Category.objects.get(pk=self.kwargs['category_id'])
        return context
    
    def get_queryset(self):
        return News.objects.filter(category_id=self.kwargs['category_id'], is_published=True)
    
class ViewNews(DetailView):
    model = News
    context_object_name = 'news_item'
    
class CreateNews(CreateView):
    form_class = NewsForm
    template_name = 'news/add_news.html'