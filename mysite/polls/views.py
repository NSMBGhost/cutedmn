import json

from django.shortcuts import render
from .models import Chp,Pics
from django.http import HttpResponse
from datetime import date
import time
def getchp(request):
    dat=date.today()
    days=dat.day
    val=Chp.objects.get(cid=int(days))
    result = {"chp": val.value}
    return HttpResponse(json.dumps(result), content_type="application/json")
def upload(request):
    if request.method=='POST':
        nowtime=time.strftime('%Y%m%d')
        nowtime=str(nowtime)
        files=request.FILES.getlist("files")
        for f in files:
            pic=Pics(value=nowtime,paths=f)
            pic.save()
        return HttpResponse("OK")
# Create your views here.
