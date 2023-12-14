from django.shortcuts import render

# Create your views here.
from app.models import *

def topic(request):
    QLTO=Topic.objects.all()
    d={'topic':QLTO}
    return render(request,'topic.html',d)

def webpage(request):
    QLTO=Webpage.objects.all()
    d={'webpage':QLTO}
    return render(request,'webpage.html',d)

def accessrecord(request):
    QLTO=AccessRecord.objects.all()
    d={'accessrecord':QLTO}
    return render(request,'accessrecord.html',d)