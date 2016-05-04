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

from mechanic.models import Mechanic


@require_http_methods(["GET"])
@login_required(login_url='/admin/')
def add_mechanic(request):
    if request.method == "GET":
        return render(request, 'mechanic/addmechanic.html')


@require_http_methods(["POST"])
@login_required(login_url='/admin/')
def add_mechanic_view(request):
    if request.method == "POST":
        mechanic_values = {}
        for name, value in request.POST.iteritems():
            mechanic_values[name] = value
        del mechanic_values['csrfmiddlewaretoken']
        mechanic_values['created_by'] = request.user
        mechanic_values['gender'] = mechanic_values['radio1']
        del mechanic_values['radio1']
        mechanic_obj = Mechanic.objects.create(**mechanic_values)
        return HttpResponseRedirect('/mechanic/view/')


@require_http_methods(["GET"])
@login_required(login_url='/admin/')
def mechanic_view(request):
    if request.method == "GET":
        context = RequestContext(request, {
            "mechanics": Mechanic.objects.all()})
        return render_to_response('mechanic/mechanic_detail.html',
                                  context_instance=context)


@require_http_methods(["POST"])
@login_required(login_url='/admin/')
def mechanic_delete(request):
    if request.method == "POST":
        mechanic_id = request.POST['id']
        mechanic_obj = Mechanic.objects.filter(id=mechanic_id)
        if mechanic_obj:
            mechanic_obj[0].delete()
            return HttpResponse({"success": True})
    return HttpResponseBadRequest


@require_http_methods(["GET", "POST"])
@login_required(login_url='/admin/')
def mechanic_edit(request, id):
    if request.method == "GET":
        mechanic_obj = Mechanic.objects.filter(id=id)
        if mechanic_obj:
            context = RequestContext(request, {
                "mechanic": mechanic_obj[0]})
            return render_to_response('mechanic/editmechanic.html',
                                      context_instance=context)
        return HttpResponseBadRequest

    if request.method == "POST":
        mechanic_values = {}
        for name, value in request.POST.iteritems():
            mechanic_values[name] = value
        del mechanic_values['csrfmiddlewaretoken']
        mechanic_values['gender'] = mechanic_values['radio1']
        del mechanic_values['radio1']
        mechanic_obj = Mechanic.objects.filter(id=id).update(**mechanic_values)
        return HttpResponse(mechanic_obj)
