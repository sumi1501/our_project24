from django.shortcuts import render
from app.models import *
from django.http import HttpResponse
# Create your views here.
def topic(request ):
    if request.method=="POST":
        top=request.POST['to']
        TO=Topic.objects.get_or_create(topic_name=top)[0]
        TO.save()

        QLTO=Topic.objects.all()
        d={'topic':QLTO}
        return render(request,'topic_data.html',d)
    return render(request,'topic.html')


def web(request):
    if request.method=="POST":
        topic=request.POST['to']
        name=request.POST['na']
        url=request.POST['ur']

        TO=Topic.objects.get(topic_name=topic)
        WB=Webpage.objects.get_or_create(topic_name=TO,name=name,url=url)[0]
        WB.save()

        QLWO=Webpage.objects.all()
        d={'webpage':QLWO}
        return render(request,'web_data.html',d)
    return render(request,'web.html')


def access(request):
    if request.method=="POST":
        name=request.POST['na']
        author=request.POST['au']
        date=request.POST['dt']
        WO=Webpage.objects.get(name=name)
        ARO=AccessRecord.objects.get_or_create(name=WO,author=author,date=date)[0]
        ARO.save()

        QLAO=AccessRecord.objects.all()
        d={'accessrecord':QLAO}
        return render(request,'access_data.html',d)
    return render(request,'access.html')
