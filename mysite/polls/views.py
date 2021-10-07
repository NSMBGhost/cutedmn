from django.shortcuts import render
from .models import Chp
from django.http import HttpResponse
from datetime import date
def getchp(request):
    dat=date.today()
    days=dat.day
    val=Chp.objects.get(cid=int(days))

    return HttpResponse("%s" % val.value)

# Create your views here.
