from django.shortcuts import render, redirect
from .models import Product


def index(request):
    return render(request, 'store/index.html')
