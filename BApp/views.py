from django.shortcuts import render
from BApp.forms import BlogForm


def list(request):
    lists = BlogForm
    return render(request, 'list.html', {'forms': lists})


def details(request):
    return render(request, 'detailsview.html')
