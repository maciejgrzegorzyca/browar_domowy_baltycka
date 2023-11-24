from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Batch

def batches(request):
    mybatches = Batch.objects.all().values()
    template = loader.get_template('batchespage.html')

    context = {'mybatches': mybatches}

    return HttpResponse(template.render(context, request))



def details(request, id):
    mybatches = Batch.objects.get(id=id)
    template = loader.get_template('detailspage.html')

    context = {'mybatches': mybatches}

    return HttpResponse(template.render(context, request))