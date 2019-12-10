from django.shortcuts import render,redirect
from django.template import Template, loader
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from .models import *
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
from django.conf import settings
import json

# Create your views here.

def userLogin(request):
	return render(request,'index.html')
