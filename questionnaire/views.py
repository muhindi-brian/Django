from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
)
from .models import QuestionnaireResponse

def home(request):
    return render(request, "questionnaire/home.html")

def about(request):
    return render(request, "questionnaire/about.html")


class QuestionnaireListView(ListView):
    model = QuestionnaireResponse
    context_object_name = "questionnaire"
    template_name = "questionnaire/list_view.html"
    ordering = ["-date_published"]

class QuestionnaireCreateView(CreateView):
    model = QuestionnaireResponse
    fields = ["gender","age","nationality","question_1"]
    success_url = "/listview/"
# Create your views here.s