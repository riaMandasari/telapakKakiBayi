from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request,"index.html")

# def pelatihan (request):

#     return render(request,'pelatihan.html')

# def pengujian (request):

#     return render(request,'pengujian.html')


