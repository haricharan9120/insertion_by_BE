from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from app.models import *


def insert_topic(request):
    tn=input()
    TO=Topic.objects.get_or_create(topic_name=tn)
    return HttpResponse('TOPIC IS CREATED')


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
        return HttpResponse('WEBPAGE IS CREATED')
    else:
        return HttpResponse('NO SUCH TOPIC IN PARENT TABLE')
    


def insert_Access(request):
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
    return HttpResponse('ACCESS RECORD IS CREATED')

