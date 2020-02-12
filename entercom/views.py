from django.http import HttpResponse
import datetime
from django.template import Template, Context
from django.template.loader import get_template
from django.shortcuts import render

def barraArriba(request):

    return render(request, "miplantilla_base.html")

def contenido2(request):

    return render(request, "contenido2.html")



