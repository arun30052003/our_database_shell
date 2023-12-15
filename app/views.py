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

def insert_topic(request):
    to=input('Enter topic_name')
    NTO=Topic.objects.get_or_create(topic_name=to)[0]
    NTO.save()

    QLTO=Topic.objects.all()
    d={'topic':QLTO}
    return render(request,'topic.html',d)

def insert_webpage(request):
    to=input('Enter topic_name')
    wn=input('Enter name')
    wu=input('Enter url')
    we=input('Enter email')

    TO=Topic.objects.get(topic_name=to)
    NWO=Webpage.objects.get_or_create(topic_name=TO,name=wn,url=wu,email=we)[0]
    NWO.save()

    QLTO=Webpage.objects.all()
    d={'webpage':QLTO}
    return render(request,'webpage.html',d)

def insert_accessrecord(request):
    pk=int(input('Enter pk for webpage'))
    ad=input('Enter date')
    aa=input('Enter author')

    WO=Webpage.objects.get(pk=pk)

    NAO=AccessRecord.objects.get_or_create(name=WO,date=ad,author=aa)[0]
    NAO.save()

    QLTO=AccessRecord.objects.all()
    d={'accessrecord':QLTO}
    return render(request,'accessrecord.html',d)