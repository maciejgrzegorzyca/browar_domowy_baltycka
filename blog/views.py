from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


# Create your views here.
def blogpage(request):
 
     return render(request, "blog.html", {})
