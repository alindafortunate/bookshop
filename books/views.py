from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Books


# Create your views here.
class BookListView(ListView):
    model = Books
    context_object_name = "book_list"
    template_name = "books/book_list.html"


class BookDetailView(DetailView):
    model = Books
    context_object_name = "bookdetail"
    template_name = "books/book_detail.html"
