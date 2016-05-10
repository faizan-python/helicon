import json

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

from quotation.models import (
    Quotation,
    QuotationPart
)


@require_http_methods(["GET"])
@login_required(login_url='/admin/')
def quotation(request):
    if request.method == "GET":
        return render(request, 'quotation/quotation.html')


@require_http_methods(["POST"])
@login_required(login_url='/admin/')
def quotation_generate(request):
    if request.method == "POST":
        data = request.POST.dict()
        forms = json.loads(data.keys()[0])
        quotation_form = forms.get('customer')
        part_data = forms.get('part_data')
        del forms['customer']
        del forms['part_data']
        forms.update(quotation_form)
        forms['created_by'] = request.user
        quotation_obj = Quotation.objects.create(**forms)

        part_obj = []
        part_total_cost = 0
        for part in part_data:
            if part:
                if part.get('part_name') and part.get('price'):
                    obj = QuotationPart.objects.create(part_name=part.get('part_name'),
                                                       price=part.get('price'),
                                                       description=part.get('description'),
                                                       part_quantity=part.get(
                                                           'part_quantity'),
                                                       created_by=request.user)
                    part_total_cost += (int(obj.price)
                                        * int(obj.part_quantity))
                    part_obj.append(obj)

        quotation_obj.parts.add(*part_obj)
        quotation_obj.save()
        return HttpResponse("Invoice Generated Successfilly")


@require_http_methods(["GET"])
@login_required(login_url='/admin/')
def quotation_list(request):
    if request.method == "GET":
        context = RequestContext(request, {
            "quotations": Quotation.objects.filter(is_active=True)})
        return render_to_response('quotation/quotation_list.html',
                                  context_instance=context)


@require_http_methods(["GET"])
@login_required(login_url='/admin/')
def quotation_pdf(request, id):
    if request.method == "GET":
        quotation_obj = Quotation.objects.filter(is_active=True, id=id)
        if quotation_obj:
            context = RequestContext(request, {
                "quotation": quotation_obj[0]})
            return render_to_response('quotation/quotationpdf.html',
                                      context_instance=context)
    return HttpResponseBadRequest("Error")
