from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Batch
from django.views.generic import ListView, DetailView

    
#Class Based View
class BatchesHome(ListView):
    model = Batch
    template_name = 'batches_home.html'
    queryset = Batch.objects.all()  #bacthes/<modelname>_list.html


class BatchesDetail(DetailView):
    model = Batch
    template_name = 'batches_detail.html'
    queryset = Batch.objects.all()  #bacthes/<modelname>_list.html



#function views
# def batches_home(request):
#     mybatches = Batch.objects.all()
#     template = loader.get_template('batches_home.html')
#     context = {'mybatches': mybatches}
#     return HttpResponse(template.render(context, request))

# def batches_detail(request, id):
#     mybatches = Batch.objects.get(id=id)
#     template = loader.get_template('batch_detail.html')
#     context = {'mybatches': mybatches}
#     return HttpResponse(template.render(context, request))