"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from datetime import datetime

def home(request):
    """Renders the home page."""

    template = loader.get_template('app/index.html')
    context = {
            'title':'Home',
            'message':'Your application menu page.',
            'year':datetime.now().year,
    }

    return HttpResponse(template.render(context, request))

def menu(request):
    """Renders the menu page."""

    template = loader.get_template('app/menu.html')
    context = {
            'title':'Menu',
            'message':'Your application menu page.',
            'year':datetime.now().year,
    }

    return HttpResponse(template.render(context, request))

def devZone(request):
    """Renders the delivery zone page."""

    template = loader.get_template('app/devZone.html')
    context = {
            'title':'Delivery Zone',
            'message':'Your Delivery Zone page.',
            'year':datetime.now().year,
    }

    return HttpResponse(template.render(context, request))

def gallery(request):
    """Renders the gallery page."""

    template = loader.get_template('app/gallery.html')
    context = {
            'title':'gallery',
            'message':'Your gallery page.',
            'year':datetime.now().year,
    }

    return HttpResponse(template.render(context, request))

def about(request):
    """Renders the about page."""

    template = loader.get_template('app/about.html')
    context = {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
    }

    return HttpResponse(template.render(context, request))

def contact(request):
    """Renders the contact page."""

    template = loader.get_template('app/contact.html')
    context = {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
    }

    return HttpResponse(template.render(context, request))
