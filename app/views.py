from django.shortcuts import render

# Create your views here.
from app.forms import *

from django.http import HttpResponse

def Insert_Topic(request):
    TFEO=Topic_form()
    d={'TFEO':TFEO}

    if request.method=='POST':
     TFDO=Topic_form(request.POST)
     if TFDO.is_valid():
            TFDO.save()
            return HttpResponse('Topic data inserterd success')

    return render(request,'Insert_Topic.html',d)


def Insert_Webpage(request):
    WFEO=Webpage_form()
    d1={'WFEO':WFEO}
    if request.method=='POST':
        WFDO=Webpage_form(request.POST)
        if WFDO.is_valid():
            WFDO.save()
            return HttpResponse('Webpage insert success')
        
    return render(request,'Insert_Webpage.html',d1)

