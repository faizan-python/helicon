import json

from django.core import serializers
from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.contrib.auth import authenticate
from django.http import (
    HttpResponse,
    HttpResponseBadRequest
)
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.shortcuts import render_to_response

from mechanic.models import Mechanic
from customer.models import Customer
from vehical.models import Vehical
import datetime


@require_http_methods(["POST"])
@login_required(login_url='/admin/')
def get_user_vehical(request):
    if request.method == "POST":
        context = RequestContext(request)
        context_dict = {}
        customer_id = request.POST['id']
        cust_obj = Customer.objects.get(id=customer_id,
                                        is_active=True)
        vehicals = list(Vehical.objects.filter(customer=cust_obj,
                                               is_active=True).values())
        cust_obj = list(Customer.objects.filter(id=customer_id,
                                                is_active=True).values())
        obj = {
            "vehicals": vehicals,
            "customer": cust_obj
        }
        json.JSONEncoder.default = lambda self, obj: (
            obj.isoformat() if isinstance(obj, datetime.datetime) else None)
        return HttpResponse(json.dumps(obj), content_type="application/json")
