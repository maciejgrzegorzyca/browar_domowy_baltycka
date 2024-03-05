from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Blog_add

# Create your views here.


def blog_home(request):
    mycomments = Blog_add.objects.all()
    template = loader.get_template('blog_home.html')

    context = {'mycomments': mycomments}

    return HttpResponse(template.render(context, request))




def blog_detail(request, id):
    mycomments = Blog_add.objects.get(id=id)
    template = loader.get_template('blog_detail.html')

    context = {'mycomments': mycomments}

    return HttpResponse(template.render(context, request))