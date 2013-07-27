# Create your views here.
from datetime import date
from django.template import RequestContext
from django.http import HttpResponse
from django.shortcuts import render_to_response

from .models import MathModels

def mathmodels_page(request):
    mathmodels = MathModels.objects.all()
    
    return render_to_response('models.html', locals(), context_instance=RequestContext(request))


