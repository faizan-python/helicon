from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.contrib.auth import authenticate
from django.http import (
    HttpResponse,
    HttpResponseBadRequest,
    HttpResponseRedirect
)
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.shortcuts import render_to_response

from customer.models import Customer


@require_http_methods(["GET"])
@login_required(login_url='/admin/')
def add_customer(request):
    if request.method == "GET":
        return render(request, 'customer/addcustomer.html')


@require_http_methods(["POST"])
@login_required(login_url='/admin/')
def customer_create(request):
    if request.method == "POST":
        customer_values = {}
        for name, value in request.POST.iteritems():
            customer_values[name] = value
        del customer_values['csrfmiddlewaretoken']
        customer_values['created_by'] = request.user
        customer_values['gender'] = customer_values['radio1']
        del customer_values['radio1']
        customer_obj = Customer.objects.create(**customer_values)
        return HttpResponse(customer_obj)


@require_http_methods(["GET"])
@login_required(login_url='/admin/')
def customer_view(request):
    if request.method == "GET":
        context = RequestContext(request, {
            "customers": Customer.objects.filter(
                is_active=True).only("id",
                                     "first_name",
                                     "last_name",
                                     "gender",
                                     "phone_number",
                                     "total_pending",
                                     "address",
                                     "email")})
        return render_to_response('customer/viewcustomer.html',
                                  context_instance=context)


@require_http_methods(["GET", "POST"])
@login_required(login_url='/admin/')
def customer_edit(request, id):
    if request.method == "GET":
        cust_obj = Customer.objects.filter(id=id, is_active=True)
        if cust_obj:
            context = RequestContext(request, {
                "customer": cust_obj[0]})
            return render_to_response('customer/editcustomer.html',
                                      context_instance=context)
        return HttpResponseRedirect("/home/")
    if request.method == "POST":
        customer_values = {}
        for name, value in request.POST.iteritems():
            customer_values[name] = value
        del customer_values['csrfmiddlewaretoken']
        customer_values['gender'] = customer_values['radio1']
        del customer_values['radio1']
        mechanic_obj = Customer.objects.filter(id=id).update(**customer_values)
        return HttpResponse(mechanic_obj)


@require_http_methods(["GET"])
@login_required(login_url='/admin/')
def customer_detail(request, id):
    if request.method == "GET":
        cust_obj = Customer.objects.filter(id=id, is_active=True)
        if cust_obj:
            context = RequestContext(request, {
                "customer": cust_obj[0]})
            return render_to_response('customer/customerdetail.html',
                                      context_instance=context)
        return HttpResponseRedirect("/home/")
