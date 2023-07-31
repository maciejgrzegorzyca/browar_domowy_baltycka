from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Batch

def batches(request):
    mybatches = Batch.objects.all().values()
    template = loader.get_template('batches.html')

    context = {
        'mybatches': mybatches
    }
    return HttpResponse(template.render(context, request))


    # template = loader.get_template("batches.html")
    # return HttpResponse(template.render())

# Create your views here.
