from datetime import datetime

from django.core.mail import EmailMessage
from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.contrib.auth import authenticate
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.shortcuts import render_to_response


def index(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/home/')
    return render(request, 'web/login.html')


def home(request):
    return render(request, 'web/home.html')


def about(request):
    return render(request, 'web/about.html')


def contact(request):
    return render(request, 'web/contact.html')


def product(request):
	return render(request, 'web/product.html')


def save_contact(request):
    import pdb;pdb.set_trace()
    if request.POST.dict().get('number'):
        subject = "(Contact@ "+request.POST.dict().get('number')+") "

        if request.POST.dict().get('name'):
            name = request.POST.dict().get('name')
        else:
            name = "Guest "
        if request.POST.dict().get('message'):
            body = "Hey there is request from "+name+" ," +request.POST.dict().get('message')
        else:
            body = "Hey, There is an contact request from request.POST.dict().get('number'). Please contact as soon as possible."

        if request.POST.dict().get('subject'):
            subject += request.POST.dict().get('subject') + " from "+ name
        else:
            subject += "Contact Request from a "+ name

        email = EmailMessage(subject, body, to=['heliconengg@gmail.com'])
        email.send()
        return True
    return render(request, 'web/product.html')


def product_warm_shaft(request):
	return render(request,'web/product_warm_shaft.html')

def product_crown_pinion(request):
	return render(request,'web/product_crown_pinion.html')

def product_warm_wheel(request):
	return render(request,'web/product_warm_wheel.html')



def product_pinion_shaft(request):
	return render(request,'web/product_pinion_shaft.html')


def product_spiral_bevel_gear(request):
    return render(request,'web/product_spiral_bevel_gear.html')


def product_gear_shafts(request):
    return render(request,'web/product_gear_shafts.html')

def product_worm_wheel_shaft(request):
    return render(request,'web/product_worm_wheel_shaft.html')

def product_worm_shaft_elevators(request):
    return render(request,'web/product_worm_shaft_elevators.html')

def product_forging_gear_shaft(request):
    return render(request,'web/product_forging_gear_shaft.html')

def product_crown_pinion_steel(request):
    return render(request,'web/product_crown_pinion_steel.html')


def product_balancing_gear(request):
    return render(request,'web/product_balancing_gear.html')

def product_spur_gear(request):
    return render(request,'web/product_spur_gear.html')


def product_loose_gears(request):
    return render(request,'web/product_loose_gear.html')
