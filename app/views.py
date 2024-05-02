from django.shortcuts import render
from django.http import HttpResponse
from django.db.models.functions import Length

# Create your views here.
from app.models import *


def insert_topic(request):
    tn=input()
    TO=Topic.objects.get_or_create(topic_name=tn)
    d={'QLTO':Topic.objects.all()}
    return render(request,'display_topic.html',d)


def insert_Webpage(request):
    '''tn=input()
    TO=Topic.objects.get_or_create(topic_name=tn)[0]
    TO.save()
    n=input()
    u=input()
    e=input()
    WO=Webpage.objects.get_or_create(topic_name=TO,name=n,url=u,email=e)[0]
    WO.save()
    return HttpResponse('WEBPAGE CREATED')
    
    tn=input()
    LTO=Topic.objects.get(topic_name=tn)
    '''

    tn=input()
    n=input()
    u=input()
    e=input()
    LTO=Topic.objects.filter(topic_name=tn)
    if LTO:
        TO=LTO[0]
        WO=Webpage.objects.get_or_create(topic_name=TO,name=n,url=u,email=e)[0]
        WO.save()
        d={'QLWO':Webpage.objects.all()}
        return render(request,'display_webpage.html',d)
    else:
        d={'QLTO':Topic.objects.all()}
        return render(request,'display_topic.html',d)
    


def insert_Access(request):
    '''
    tn=input()
    TO=Topic.objects.get_or_create(topic_name=tn)[0]
    TO.save()
    n=input()
    u=input()
    e=input()
    WO=Webpage.objects.get_or_create(topic_name=TO,name=n,url=u,email=e)[0]
    WO.save()
    date=input()
    author=input()
    AO=AccessRecord.objects.get_or_create(name=WO,date=date,author=author)
    '''
    i=input('enter id')
    WO=Webpage.objects.get(id=i)

    d=input('enter date')
    a=input('enter author')
    AO=AccessRecord.objects.get_or_create(name=WO,date=d,author=a)[0]
    AO.save()
    d={'QLAO':AccessRecord.objects.all()}

    return render(request,'display_accessrecord.html',d)










def display_topic(request):
    QLTO=Topic.objects.all()
    d={'QLTO':QLTO}
    return render(request,'display_topic.html',context=d)



def display_webpage(request):
    QLWO=Webpage.objects.all()
    QLWO=Webpage.objects.filter(topic_name='WWE')
    QLWO=Webpage.objects.exclude(topic_name='WWE')
    QLWO=Webpage.objects.all()[1:3:]
    QLWO=Webpage.objects.order_by('name')
    QLWO=Webpage.objects.order_by('-name')
    QLWO=Webpage.objects.order_by(Length('name'))
    QLWO=Webpage.objects.order_by(Length('name').desc())
    
    
    d={'QLWO':QLWO}
    return render(request,'display_webpage.html',context=d)



def display_accessrecord(request):
    QLAO=AccessRecord.objects.all()
    d={'QLAO':QLAO}
    return render(request,'display_accessrecord.html',context=d)




