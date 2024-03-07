from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Blog_add
from django.views.generic import ListView, DetailView


#Class Based View
class BlogHome(ListView):
    model = Blog_add
    template_name = 'blog_home.html'
    queryset = Blog_add.objects.all()  #blog/<modelname>_list.html


class BlogDetail(DetailView):
    model = Blog_add
    template_name = 'blog_detail.html'
    queryset = Blog_add.objects.all()  #blog/<modelname>_list.html



# Create your views here.

# function views
# def blog_home(request):
#     mycomments = Blog_add.objects.all()
#     template = loader.get_template('blog_home.html')
#     context = {'mycomments': mycomments}
#     return HttpResponse(template.render(context, request))

# def blog_detail(request, id):
#     mycomments = Blog_add.objects.get(id=id)
#     template = loader.get_template('blog_detail.html')
#     context = {'mycomments': mycomments}
#     return HttpResponse(template.render(context, request))