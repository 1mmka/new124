from typing import Any
from django.db import models
from django.shortcuts import render
from django.views.generic import ListView,ArchiveIndexView
from app.models import Book

# Create your views here.
class AllBooks(ListView):
    model = Book
    template_name = 'book.html'
    context_object_name = 'dct'

class BookInfo(ListView):
    model = Book
    template_name = 'info.html'
    
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['info'] = Book.objects.filter(pk = self.kwargs['pk']).first()
        return context

class BooksFilter(ArchiveIndexView):
    model = Book
    template_name = 'book.html'
    context_object_name = 'dct'
    
    date_field = 'date'

    def get_dated_queryset(self,**lookup):
        filter_type = str(self.kwargs['type'])
        if filter_type == 'date':
            self.ordering = ['date']
            self.allow_empty = False
        elif filter_type == 'year':
            self.date_list_period = 'year'
            self.allow_empty = False
        return super().get_dated_queryset(**lookup)