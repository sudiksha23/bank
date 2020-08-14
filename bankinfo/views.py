from django.shortcuts import render, HttpResponse, redirect
from bankinfo.models import EntrySignup
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from rest_framework.decorators import api_view
from bankinfo.forms import EntrySignupForm
from django.core.files import File
from rest_framework import viewsets
from .serializers import EntrySignupSerializer
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser,FormParser, FileUploadParser
from rest_framework.response import Response
import json
from rest_framework import status
from os import path
import os
from django.http import Http404
from rest_framework import generics
from django.http import HttpResponse, JsonResponse
from wsgiref.util import FileWrapper
from django.views.decorators.csrf import csrf_exempt
from rest_framework.settings import api_settings

#@api_view(['GET'])
#def EntrySignupViewSet2(self, request, bank_name, city):
  #  queryset = EntrySignup.objects.filter(city__iexact=city, bank__name__icontains=bank_name)
   #// serializer = EntrySignupSerializer(branch_qset, many=True)
#	//return Response(serializer.data, safe=False)
    
#//@api_view(['GET'])
#//def EntrySignupViewSet(self,request, ifsc):
 # //  queryset = EntrySignup.objects.filter(ifsc=ifsc)
  # // serializer = EntrySignupSerializer(branch_qset, many=True)
   # //return Response(serializer.data, safe=False)
    
def index(request):
    return render(request, 'index.html')


def searchtable1(request):    
    if request.method == 'POST':
        u = request.POST["u"]
    s=EntrySignup.objects.filter(ifsc=u)
    return render(request, 'index.html', {'set' : s})

def searchtable2(request):
    if request.method == 'POST':
        c = request.POST["c"]
        d = request.POST["d"]
    s=EntrySignup.objects.filter(district=c, bank_name=d)
    return render(request, 'index.html', {'set1' : s})