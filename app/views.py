from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from app.models import *


def insert_topic(request):
    tn=input()
    TO=Topic.objects.get_or_create(topic_name=tn)[0]
    TO.save()
    return HttpResponse('TOPIC IS CREATED')


def insert_Webpage(request):
    tn=input()
    TO=Topic.objects.get_or_create(topic_name=tn)[0]
    TO.save()
    n=input()
    u=input()
    e=input()
    WO=Webpage.objects.get_or_create(topic_name=TO,name=n,url=u,email=e)[0]
    WO.save()
    return HttpResponse('WEBPAGE CREATED')


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

