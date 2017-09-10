import json
import datetime
import inflect
from num2words import num2words

from django.template import Context, Template
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
from django.utils import timezone
from django.template.loader import get_template

from mechanic.models import Mechanic
from customer.models import Customer
from vehical.models import (
    Vehical,
    OtherService
)
from service.models import (
    Service,
    Payment,
    DeliveryDetail,
    InvoiceDetail,
    TaxCost
)
from parts.models import (
    Part,
    LabourCost
)


def generate_datetime_number():
    data  = str(timezone.datetime.today().year)
    data += str(timezone.datetime.today().month)
    data += str(timezone.datetime.today().day)
    data += str(timezone.datetime.today().hour)
    data += str(timezone.datetime.today().minute)
    data += str(timezone.datetime.today().second)
    data += str(timezone.datetime.today().microsecond)
    data = int(data)
    return data


@require_http_methods(["GET"])
@login_required(login_url='/home/')
def service_add(request):
    if request.method == "GET":
        context = RequestContext(request, {
            "customers": Customer.objects.filter(is_active=True),
            "mechanics": Mechanic.objects.filter(is_active=True)})
        return render_to_response('service/service.html',
                                  context_instance=context)


@require_http_methods(["POST"])
@login_required(login_url='/admin/')
def service_create(request):
    if request.method == "POST":
        data = request.POST.dict()
        forms = json.loads(data.keys()[0])
        customer_form = forms.get('customer')
        service_form = forms.get('service_deatils')
        mechanic_id = forms.get('mechanic')
        gender = forms.get('gender')
        tin_number = customer_form.get('tin_number')
        del customer_form['tin_number']

        if customer_form.get('radio1'):
            del customer_form['radio1']
        customer = Customer.objects.filter(
            **customer_form)
        if not customer:
            customer_form['created_by'] = request.user
            customer_form['gender'] = gender
            customer_obj = Customer.objects.create(**customer_form)
        else:
            customer_obj = customer[0]

        customer_obj.tin_number = tin_number
        customer_obj.save()

        if forms.get("service_type") == "vehical":
            vehical_form = forms.get("service_type_form")
            vehical_form['customer'] = customer_obj
            vehical = Vehical.objects.filter(**vehical_form)
            if not vehical:
                vehical_form['created_by'] = request.user
                vehical_form['last_serviced_date'] = timezone.now()
                vehical = Vehical.objects.create(**vehical_form)
            else:
                vehical = vehical[0]
                vehical.last_serviced_date = timezone.now()
                vehical.save()
            service_form['vehical'] = vehical

        if forms.get("service_type") == "other":
            other_form = forms.get("service_type_form")
            other_form['customer'] = customer_obj
            other_form['created_by'] = request.user
            other_form['created_at'] = timezone.now()
            other_form['number'] = generate_datetime_number()
            other_obj = OtherService.objects.create(**other_form)
            service_form['otherservice'] = other_obj

        if mechanic_id:
            service_form['serviced_by'] = Mechanic.objects.get(id=mechanic_id)
        service_form['created_by'] = request.user
        service_form['customer'] = customer_obj
        service_form['expected_delivery_date'] = datetime.datetime.strptime(
            service_form['expected_delivery_date'], "%m/%d/%Y").date()

        if service_form.get('purchase_order_date'):
            service_form['purchase_order_date'] = datetime.datetime.strptime(
                service_form['purchase_order_date'], "%m/%d/%Y").date()
        else:
            del service_form['purchase_order_date']

        advance_payment = False
        if service_form.get('advance_payment'):
            if int(service_form.get('advance_payment')) > 0:
                service_form['advance_payment'] = int(
                    service_form.get('advance_payment'))
                advance_payment = True
                payment = Payment.objects.create(
                    payment_amount=int(service_form.get('advance_payment')),
                    recieved_by=request.user,
                    payment_type=Payment.PaymentOptions.Advance.value)
        else:
            service_form['advance_payment'] = 0

        service = Service.objects.create(**service_form)
        if advance_payment:
            service.payment.add(payment)
            service.total_paid = int(service_form.get('advance_payment'))
            service.save()
        obj = list(Service.objects.filter(
            invoice_number=service.invoice_number).values())
        json.JSONEncoder.default = lambda self, obj: (
            obj.isoformat() if isinstance(obj, datetime.datetime) else None)
        return HttpResponse(json.dumps(obj), content_type="application/json")


@require_http_methods(["GET"])
@login_required(login_url='/admin/')
def service_search(request):
    if request.method == "GET":
        context = RequestContext(request, {
            "services": Service.objects.filter(
                is_active=True).only("invoice_number",
                                     "customer",
                                     "vehical",
                                     "is_serviced",
                                     "service_date",
                                     "total_pending",
                                     "total_paid")})
        return render_to_response('service/servicesearch.html',
                                  context_instance=context)


@require_http_methods(["GET"])
@login_required(login_url='/admin/')
def service_view(request, id):
    if request.method == "GET":
        service_obj = Service.objects.filter(invoice_number=id)
        if service_obj:
            context = RequestContext(request, {
                "service": service_obj[0]})
            return render_to_response('service/viewservice.html',
                                      context_instance=context)
        return HttpResponseRedirect("/home/")


@require_http_methods(["GET"])
@login_required(login_url='/admin/')
def service_pending(request):
    if request.method == "GET":
        context = RequestContext(request, {
            "services": Service.objects.filter(
                is_active=True, is_serviced=False)})
        return render_to_response('service/pendingservice.html',
                                  context_instance=context)


@require_http_methods(["GET", "POST"])
@login_required(login_url='/admin/')
def service_edit(request, id):
    if request.method == "GET":
        service_obj = Service.objects.filter(invoice_number=id)
        if service_obj:
            context = RequestContext(request, {
                "service": service_obj[0]})
            return render_to_response('service/editservice.html',
                                      context_instance=context)
        return HttpResponseRedirect("/home/")
    if request.method == "POST":
        return HttpResponse("EDit")


@require_http_methods(["GET"])
@login_required(login_url='/admin/')
def invoice_get(request, id):
    if request.method == "GET":
        service_obj = Service.objects.filter(invoice_number=id)
        tax_obj = TaxCost.objects.filter(id=1)
        if service_obj and tax_obj:
            context = RequestContext(request, {
                "service": service_obj[0],
                "igst": tax_obj[0].igst,
                "gst": tax_obj[0].sgst + tax_obj[0].cgst})
            return render_to_response('service/invoice.html',
                                      context_instance=context)
        return HttpResponseRedirect("/home/")
    if request.method == "POST":
        return HttpResponse("EDit")


@require_http_methods(["GET"])
@login_required(login_url='/admin/')
def invoice_delete(request, id):
    if request.method == "GET":
        service_obj = Service.objects.filter(invoice_number=id)
        if service_obj:
            service_obj = service_obj[0]
            service_obj.is_active = False
            service_obj.save()
            
            invoice_detail = InvoiceDetail.objects.get(id=1)
            if service_obj.retail_invoice_number:
                services = Service.objects.filter(
                    retail_invoice_number__gt=service_obj.retail_invoice_number,
                    is_active=True)
                for service in services:
                    service.retail_invoice_number = int(service.retail_invoice_number) - 1
                    service.save()
                invoice_detail.latest_retail_invoice = int(invoice_detail.latest_retail_invoice) - 1


            if service_obj.tax_invoice_number:
                services = Service.objects.filter(
                    tax_invoice_number__gt=service_obj.tax_invoice_number,
                    is_active=True)
                for service in services:
                    service.tax_invoice_number = int(service.tax_invoice_number) - 1
                    service.save()
                invoice_detail.latest_tax_invoice = int(invoice_detail.latest_tax_invoice) - 1

            invoice_detail.save()

            return HttpResponseRedirect("/service/search/")
        return HttpResponseRedirect("/home/")
    if request.method == "POST":
        return HttpResponse("EDit")


@require_http_methods(["GET", "POST"])
@login_required(login_url='/admin/')
def create_invoice(request):
    if request.method == "GET":
        service_objs = Service.objects.filter(
            is_serviced=False, is_active=True)
        context = RequestContext(request, {
            "services": service_objs})
        return render_to_response('service/invoicecreate.html',
                                  context_instance=context)

    if request.method == "POST":
        return HttpResponse("EDit")


@require_http_methods(["GET", "POST"])
@login_required(login_url='/admin/')
def invoice(request):
    if request.method == "POST":
        request_dict = request.POST.dict()
        data = json.loads(request_dict.keys()[0])
        service_obj = Service.objects.filter(
            invoice_number=data.get('service_id'))
        if service_obj:
            service_obj = service_obj[0]
            if not service_obj.is_serviced:
                service_obj.is_serviced = True
                service_obj.labour_cost = data.get('labour_cost', 0)
                service_obj.tax = data.get('tax', 0)
                service_obj.total_cost = data.get('total_cost', 0)
                service_obj.tax_amount = data.get('tax_amount', 0)
                service_obj.service_tax = data.get('service_tax', 0)
                service_obj.service_tax_amount = data.get(
                    'service_tax_amount', 0)
                service_obj.remark = data.get('remark', "")
                if data.get('next_service_date'):
                    service_obj.next_service_date = datetime.datetime.strptime(
                        data.get('next_service_date'), "%m/%d/%Y").date()
                service_obj.delivery_date = timezone.now()
                service_obj.total_paid += int(data.get('total_paid', 0))
                if int(data.get('total_paid')) > 0:
                    payment = Payment.objects.create(payment_amount=data.get('total_paid'),
                                                     recieved_by=request.user,
                                                     cheque_number=data.get(
                                                         'cheque_number'),
                                                     payment_type=data.get('payment_type'))
                    if payment.payment_type == Payment.PaymentOptions.CHEQUE.value:
                        payment.cheque_bank_name = data.get(
                            'cheque_bank_name', "")
                        if data.get('cheque_date'):
                            payment.cheque_date = datetime.datetime.strptime(
                                data.get('cheque_date'), "%m/%d/%Y").date()
                        payment.save()
                    service_obj.payment.add(payment)
                total_pending = float(
                    data.get('total_cost', 0)) - float(data.get('total_paid', 0))
                total_pending -= service_obj.advance_payment
                service_obj.total_pending = total_pending
                if total_pending < 1:
                    service_obj.complete_payment = True

                part_data = data.get('part_data')
                part_obj = []
                part_total_cost = 0
                for part in part_data:
                    if part:
                        if part.get('part_name') and part.get('price'):
                            obj = Part.objects.create(part_name=part.get('part_name'),
                                                      price=part.get('price'),
                                                      part_quantity=part.get(
                                                          'part_quantity'),
                                                      created_by=request.user,
                                                      part_code=part.get('part_code'))
                            part_total_cost += (float(obj.price)
                                                * float(obj.part_quantity))
                            part_obj.append(obj)

                if len(part_data) > 1:
                    latest_invoice_id = InvoiceDetail.objects.get(id=1)
                    latest_invoice_id.latest_tax_invoice = int(latest_invoice_id.latest_tax_invoice) + 1
                    latest_invoice_id.save()
                    service_obj.tax_invoice_number = latest_invoice_id.latest_tax_invoice


                labour_data = data.get('labour_data')
                labour_obj = []
                labour_total_cost = 0
                for labour in labour_data:
                    if labour:
                        if labour.get('name') and labour.get('labour_price'):
                            obj = LabourCost.objects.create(
                                name=labour.get('name'),
                                labour_quantity=labour.get('labour_quantity'),
                                labour_price=labour.get('labour_price'),
                                created_by=request.user)
                            labour_total_cost += float(obj.labour_price)
                            labour_obj.append(obj)

                if len(labour_data) > 1:
                    latest_invoice_id = InvoiceDetail.objects.get(id=1)
                    latest_invoice_id.latest_retail_invoice = int(latest_invoice_id.latest_retail_invoice) + 1
                    latest_invoice_id.save()
                    service_obj.retail_invoice_number = latest_invoice_id.latest_retail_invoice

                service_obj.parts.add(*part_obj)
                service_obj.labourcost_detail.add(*labour_obj)
                service_obj.part_cost = part_total_cost
                service_obj.gate_pass_no = data.get('gate_pass_no', "")
                service_obj.freight_cost = data.get('freight_cost', 0)
                service_obj.invoice_date = timezone.datetime.today()
                service_obj.challan_date = timezone.datetime.today()
                service_obj.gst_type = data.get('gst_type', "")

                if data.get('challan_number'):
                    service_obj.challan_number = data.get('challan_number', "")

                service_obj.save()
                return HttpResponse("Invoice Generated Successfilly")
            return HttpResponseRedirect("/home/")


@require_http_methods(["POST"])
@login_required(login_url='/admin/')
def pending_payment(request):
    if request.method == "POST":
        request_dict = request.POST.dict()
        data = json.loads(request_dict.keys()[0])
        service_obj = Service.objects.filter(
            invoice_number=data.get('service_id'))
        if service_obj:
            service_obj = service_obj[0]
            if service_obj.is_serviced:
                pending_amount = service_obj.total_pending - \
                    data.get('pending_payment')

                if float(data.get('pending_payment')) > 0:
                    payment = Payment.objects.create(
                        payment_amount=data.get('pending_payment'),
                        recieved_by=request.user,
                        cheque_number=data.get(
                            'cheque_number'),
                        payment_type=data.get('payment_type'))

                    if payment.payment_type == Payment.PaymentOptions.CHEQUE.value:
                        payment.cheque_bank_name = data.get(
                            'cheque_bank_name', "")
                        if data.get('cheque_date'):
                            payment.cheque_date = datetime.datetime.strptime(
                                data.get('cheque_date'), "%m/%d/%Y").date()
                        payment.save()
                    service_obj.payment.add(payment)
                if pending_amount < 1:
                    service_obj.complete_payment = True

                service_obj.total_paid += data.get('pending_payment')
                service_obj.total_pending = pending_amount
                service_obj.save()
                return HttpResponse("Pending payment Complete")
            return HttpResponseRedirect("/home/")


def get_total_in_words(amount_a, amount_b):
    total = amount_a + amount_b
    num_list = str(total).split('.')
    before_decical = num_list[0]
    before_decimal_inwords = num2words(int(before_decical),lang='en_IN')
    words = before_decimal_inwords + " rupees"
    return words


def get_gst_details(service_obj):

    response_dict = {}
    if service_obj.gst_type != "IGST":
        tax_obj = TaxCost.objects.filter(id=1)
        if tax_obj and service_obj:
            tax_obj = tax_obj[0]
            tax_amount = service_obj.tax_amount
            total_tax = service_obj.tax

            sgst_per = float(tax_obj.sgst)*100.0/float(total_tax)
            sgst_amount = int(round(float(tax_amount)*float(sgst_per)/100.0))

            cgst_per = float(tax_obj.cgst)*100.0/float(total_tax)
            cgst_amount = int(round(float(tax_amount)*float(cgst_per)/100.0))

            response_dict["sgst"] = tax_obj.sgst
            response_dict["sgst_amount"] = sgst_amount
            response_dict["cgst"] = tax_obj.cgst
            response_dict["cgst_amount"] = cgst_amount

    return response_dict


@require_http_methods(["GET"])
@login_required(login_url='/admin/')
def invoice_view(request, id):
    if request.method == "GET":
        service_obj = Service.objects.filter(is_active=True, invoice_number=id)
        if service_obj:
            service_obj         = service_obj[0]

            service_grand_total = get_total_in_words(service_obj.part_cost,
                                                     service_obj.tax_amount)
            labour_grand_total  = get_total_in_words(service_obj.labour_cost,
                                                    service_obj.service_tax_amount)
            grand_total         = get_total_in_words(service_obj.total_cost, 0)
            gst_details         = get_gst_details(service_obj)

            context = RequestContext(request, {
                "service"             : service_obj,
                "service_grand_total" : service_grand_total,
                "labour_grand_total"  : labour_grand_total,
                "grand_total"         : grand_total,
                "sgst"                : gst_details.get("sgst", ""),
                "sgst_amount"         : gst_details.get("sgst_amount", ""),
                "cgst"                : gst_details.get("cgst", ""),
                "cgst_amount"         : gst_details.get("cgst_amount", "")})
            return render_to_response('service/invoicepdf.html',
                                      context_instance=context)


@require_http_methods(["GET"])
@login_required(login_url='/admin/')
def invoice_retail_view(request, id):
    if request.method == "GET":
        service_obj = Service.objects.filter(is_active=True, invoice_number=id)
        if service_obj:
            service_obj = service_obj[0]
            labour_grand_total  = get_total_in_words(service_obj.labour_cost,
                                                    service_obj.service_tax_amount)
            service_grand_total = get_total_in_words(service_obj.part_cost,
                                                     service_obj.tax_amount)
            grand_total         = get_total_in_words(service_obj.total_cost, 0)

            context = RequestContext(request, {
                "service": service_obj,
                "service_grand_total" : service_grand_total,
                "labour_grand_total"  : labour_grand_total,
                "grand_total"         : grand_total})
            return render_to_response('service/invoiceretailpdf.html',
                                      context_instance=context)


@require_http_methods(["GET"])
@login_required(login_url='/admin/')
def invoice_tax_view(request, id):
    if request.method == "GET":
        service_obj = Service.objects.filter(is_active=True, invoice_number=id)
        if service_obj:
            service_obj = service_obj[0]
            labour_grand_total  = get_total_in_words(service_obj.labour_cost,
                                                    service_obj.service_tax_amount)
            service_grand_total = get_total_in_words(service_obj.part_cost,
                                                     service_obj.tax_amount)
            grand_total         = get_total_in_words(service_obj.total_cost, 0)

            context = RequestContext(request, {
                "service": service_obj,
                "service_grand_total" : service_grand_total,
                "labour_grand_total"  : labour_grand_total,
                "grand_total"         : grand_total})
            return render_to_response('service/invoicetaxpdf.html',
                                      context_instance=context)


@require_http_methods(["GET", "POST"])
@login_required(login_url='/admin/')
def report(request):
    if request.method == "GET":
        context = RequestContext(request, {})
        return render_to_response('service/report.html',
                                  context_instance=context)
    if request.method == "POST":
        request_dict = request.POST.dict()
        from_date = datetime.datetime.strptime(request_dict.get("from_date"), "%m/%d/%Y").date()
        till_date = datetime.datetime.strptime(
            request_dict.get("till_date"), "%m/%d/%Y").date()
        from_date = datetime.datetime.combine(from_date, datetime.time.min)
        till_date = datetime.datetime.combine(till_date, datetime.time.max)

        if request_dict.get('pending'):
            complete_payment = False
        else:
            complete_payment = True

        service_obj = Service.objects.filter(
            service_date__gte=from_date,
            service_date__lte=till_date,
            complete_payment=complete_payment,
            is_serviced=True)
        template = get_template('service/reportview.html')
        context = Context({'services': service_obj, 'from': from_date,
                           "till": till_date})
        content = template.render(context)
        return HttpResponse(content)


@require_http_methods(["GET", "POST"])
@login_required(login_url='/admin/')
def customer_report(request):
    if request.method == "GET":
        context = RequestContext(request, {
            "customers": Customer.objects.filter(is_active=True)
        })
        return render_to_response('service/customerreport.html',
                                  context_instance=context)
    if request.method == "POST":
        request_dict = dict(request.POST.iterlists())
        customer_id = request_dict.get("customer_id")
        pending = request_dict.get("pending")
        if pending:
            complete_payment = False
        else:
            complete_payment = True

        customer_obj = Customer.objects.get(id=customer_id[0])

        service_obj = Service.objects.filter(customer=customer_obj,
                                             is_serviced=True)
        template = get_template('service/customerreportview.html')
        context = Context({'services': service_obj, 'customer': customer_obj})
        content = template.render(context)
        return HttpResponse(content)


@require_http_methods(["GET"])
@login_required(login_url='/admin/')
def invoice_list(request):
    if request.method == "GET":
        context = RequestContext(request, {
            "services": Service.objects.filter(
                is_active=True,
                is_serviced=True).only("invoice_number",
                                       "customer",
                                       "vehical",
                                       "is_serviced",
                                       "service_date",
                                       "total_pending",
                                       "total_paid")})
        return render_to_response('service/listinvoice.html',
                                  context_instance=context)


@require_http_methods(["GET"])
@login_required(login_url='/admin/')
def customer_report_generate(request, id):
    if request.method == "GET":
        customer_obj = Customer.objects.get(id=id)

        service_obj = Service.objects.filter(customer=customer_obj,
                                             is_serviced=True)
        total_cost = 0
        total_paid = 0
        total_pending = 0
        for service in service_obj:
            total_cost += service.total_cost
            total_paid += service.total_paid
            total_pending += service.total_pending

        context = RequestContext(request, {
            'services': service_obj,
            'customer': customer_obj,
            'total_pending': total_pending,
            'total_paid': total_paid,
            'total_cost': total_cost})
        return render_to_response('service/customerreportpdf.html',
                                  context_instance=context)


@require_http_methods(["GET", "POST"])
@login_required(login_url='/admin/')
def report_generate(request):
    if request.method == "POST":
        request_dict = request.POST.dict()
        from_date = datetime.datetime.strptime(
            request_dict.get("from_date"), "%m/%d/%Y")
        till_date = datetime.datetime.strptime(
            request_dict.get("till_date"), "%m/%d/%Y")
        from_date = datetime.datetime.combine(from_date, datetime.time.min)
        till_date = datetime.datetime.combine(till_date, datetime.time.max)

        if request_dict.get('pending'):
            complete_payment = False
        else:
            complete_payment = True

        service_obj = Service.objects.filter(service_date__gt=from_date,
                                             service_date__lt=till_date,
                                             complete_payment=complete_payment,
                                             is_serviced=True)

        total_cost = 0
        total_paid = 0
        total_pending = 0
        for service in service_obj:
            total_cost += service.total_cost
            total_paid += service.total_paid
            total_pending += service.total_pending

        context = RequestContext(request, {
            "services": service_obj,
            "from_date": from_date.date(),
            "till_date": till_date.date(),
            'total_pending': total_pending,
            'total_paid': total_paid,
            'total_cost': total_cost})
        return render_to_response('service/reportpdf.html',
                                  context_instance=context)


@require_http_methods(["GET", "POST"])
@login_required(login_url='/admin/')
def generate_delivery_invoice(request, id):
    if request.method == "GET":
        service_obj = Service.objects.filter(invoice_number=id)
        if service_obj:
            context = RequestContext(request, {
                "service": service_obj[0]})
            return render_to_response('service/addeditdeliverychalan.html',
                                      context_instance=context)
        return HttpResponseRedirect("/home/")

    if request.method == "POST":
        data = request.POST.dict()
        del data['csrfmiddlewaretoken']
        service_obj = Service.objects.filter(
            invoice_number=data.get('service_id'))
        if service_obj:
            service_obj = service_obj[0]
            if service_obj.delivery_invoice_details:
                delivery_invoice_obj = service_obj.delivery_invoice_details
                delivery_invoice_obj.vehical_number = data.get(
                    'vehical_number')
                delivery_invoice_obj.remark = data.get('remark')
                delivery_invoice_obj.save()
            else:
                delivery_invoice_obj = DeliveryDetail.objects.create(
                    vehical_number=data.get('vehical_number'),
                    remark=data.get('remark'))
                service_obj.delivery_invoice_details = delivery_invoice_obj
                service_obj.save()
            redirect_url = "/service/generate/delivery/invoice/"+str(service_obj.invoice_number)+"/"
            return HttpResponseRedirect(redirect_url)
        return HttpResponseRedirect("/home/")


@require_http_methods(["GET"])
@login_required(login_url='/admin/')
def delivery_invoice(request, id):
    if request.method == "GET":
        service_obj = Service.objects.filter(invoice_number=id)
        if service_obj:
            context = RequestContext(request, {
                "service": service_obj[0]})
            return render_to_response('service/deliveryinvoice.html',
                                      context_instance=context)
        return HttpResponseRedirect("/home/")
