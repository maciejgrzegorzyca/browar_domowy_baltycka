from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


# Create your views here.
def homepage(request):
 
     return render(request, "home.html", {})

def showpage(request):
          return render(request, "hb_show.html", {})

def reviewpage(request):
          return render(request, "style_review.html", {})