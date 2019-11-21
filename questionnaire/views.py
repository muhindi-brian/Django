from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, "questionnaire/home.html")

def about(request):
    return render(request, "questionnaire/about.html")

# Create your views here.
