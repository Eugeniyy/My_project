from tkinter.tix import Tree
from unicodedata import category
from django.db import models
from django.urls import reverse

# Create your models here.

class News(models.Model):
    title = models.CharField(max_length=150, verbose_name='Title')
    content = models.TextField(blank=True, verbose_name='Content')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created_at')
    update_at = models.DateTimeField(auto_now=True, verbose_name='Update_at')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', verbose_name='Photo', blank=True)
    is_published = models.BooleanField(default=True, verbose_name='Is_publish')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Category')
    
    def get_absolute_url(self):
        return reverse(viewname="view_news", kwargs={"pk": self.pk})
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'New' #Наименование модели в единственному числе
        verbose_name_plural = 'News' #Наименование модели во множественном числе
        ordering = ['-created_at']      
    
class Category(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name='Title category')

    def get_absolute_url(self):
        return reverse(viewname="category", kwargs={"category_id": self.pk})
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['title']