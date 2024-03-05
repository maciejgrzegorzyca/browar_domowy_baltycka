from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Batch

def batches_home(request):
    mybatches = Batch.objects.all()
    template = loader.get_template('batches_home.html')

    context = {'mybatches': mybatches}

    return HttpResponse(template.render(context, request))



def batches_detail(request, id):
    mybatches = Batch.objects.get(id=id)
    template = loader.get_template('batch_detail.html')

    context = {'mybatches': mybatches}

    return HttpResponse(template.render(context, request))