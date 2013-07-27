from datetime import date
from django.template import RequestContext
from django.http import HttpResponse
from django.shortcuts import render_to_response

from .models import Regression

def regression_page(request):
    regression = Regression.objects.all()
    
    return render_to_response('regression.html', locals(), context_instance=RequestContext(request))


