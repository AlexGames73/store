from django.shortcuts import render, redirect
from .models import Product
from user_agents import parse


def home(request):
    ua_parse = parse(request.META.get("HTTP_USER_AGENT"))
    if ua_parse.is_mobile:
        return render(request, 'store/home/mobile.html')
    else:
        return render(request, 'store/home/pc.html')
