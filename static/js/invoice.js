$(document).ready(function() {

    var csrftoken = getCookie('csrftoken');
    var table_id = 1
    var labour_table_id = 1

    var dateToday = new Date(); 
    $("#challan_date").datepicker();

    function special_character_check(data) {
        data = data.replace(/"/g, "'")
        data = encodeURIComponent(data)
        return data
    }

    function roundofpendingamount(total) {

        totalsplit = total.toString()
        totalsplit = totalsplit.split(".")
        if (totalsplit.length > 1) {
            paisa = totalsplit[1]
            paisa = parseInt(paisa)
            if (paisa > 50) {
                total = parseInt(total) + 1
                return total
            }
            else {
                total = totalsplit[0]
                return total
            }
        }
        return total
    }

    $("#cash").attr('checked', false);
    $("#cheque").attr('checked', false);

    function checkifblank(data) {
        if (data){
            return data
        }
        return 0
    }

    payment_type = ""
    
    $("#cheque").click(function(event) {
        if ($("#cheque").is(':checked')) {
            $("#chequeform").show();
            payment_type = "Cheque";
            $("#cash").attr('checked', false);
            $("#cheque_date").datepicker();
        }
        else{
            $("#chequeform").hide();
            payment_type = "";
        }
    });

    $("#cash").click(function(event) {
        if ($("#cash").is(':checked')) {
            payment_type = "Cash";
            $("#chequeform").hide();
            $("#cheque").attr('checked', false);
        }
        else{
            payment_type = "";
        }
    });

    $("#sgst").attr('checked', false);
    $("#igst").attr('checked', false);

    gst_type = ""
    
    $("#sgst").click(function(event) {
        if ($("#sgst").is(':checked')) {
            gst_type = "SGST and CGST";
            $("#igst").attr('checked', false);
        }
        else{
            gst_type = "";
        }
    });

    $("#igst").click(function(event) {
        if ($("#igst").is(':checked')) {
            gst_type = "IGST";
            $("#sgst").attr('checked', false);
        }
        else{
            gst_type = "";
        }
    });

    function checkGSTValidations() {
        if (gst_type == "") {
            $.toast({
                heading: 'Error',
                text: 'Please Select GST Type !!!',
                icon: 'error',
                hideAfter: 4000,
                position: 'mid-center'
            })
            return false;
        }
        else {
            return true
        }
    }

    function calculateSum() {
        var tbl = $('#itemtable');
        var sum = 0;
        var part_sum = 0;
        var parts_list = []
        var labour_cost_list = []
        var total_labour_cost = 0
        var total_part_cost = 0
        var labour_sum = 0

        /*Part Table*/
        tbl.find('tr').each(function () {
            var quantity = 0
            var price = 0
            var sub_dict = {}
            $(this).find('#part_name').each(function () {
                if (this.value.length != 0) {
                    sub_dict[this.id] = special_character_check(this.value);
                }
            });
            $(this).find('#part_code').each(function () {
                if (this.value.length != 0) {
                    sub_dict[this.id] = special_character_check(this.value);
                }
            });
            $(this).find('#part_quantity').each(function () {
                if (!isNaN(this.value) && this.value.length != 0) {
                    quantity = checkifblank(parseInt(this.value));
                    sub_dict[this.id] = this.value;
                }
            });
            $(this).find('#price').each(function () {
                if (!isNaN(this.value) && this.value.length != 0) {
                    price = checkifblank(parseFloat(this.value));
                    sub_dict[this.id] = this.value
                }
            });
            parts_list.push(sub_dict)

            part_sum = quantity * price
            total_part_cost += part_sum

            $(this).find('.total').val(part_sum.toFixed(2));
        });

       /* Labour Table*/
        $('#labouritemtable').find('tr').each(function () {
            var labour_price = 0
            var labour_sub_dict = {}
            var labour_quantity = 0
            $(this).find('#name').each(function () {
                if (this.value.length != 0) {
                    labour_sub_dict[this.id] = special_character_check(this.value);
                }
            });
            $(this).find('#labour_quantity').each(function () {
                if (!isNaN(this.value) && this.value.length != 0) {
                    labour_quantity = checkifblank(parseInt(this.value));
                    labour_sub_dict[this.id] = this.value;
                }
            });
            $(this).find('#labour_price').each(function () {
                if (!isNaN(this.value) && this.value.length != 0) {
                    labour_price = checkifblank(parseFloat(this.value));
                    labour_sub_dict[this.id] = this.value
                }
            });
            labour_cost_list.push(labour_sub_dict)
            labour_sum = labour_quantity * labour_price
            total_labour_cost += labour_sum
            $(this).find('.total').val(labour_sum.toFixed(2));
        });

        $('#labour_cost').val(total_labour_cost)
        var tax = checkifblank(parseFloat($('#tax').val()))
        var service_tax = checkifblank(parseFloat(15))
        var paid = checkifblank(parseFloat($('#total_paid').val()))
        var labour_cost = checkifblank(parseFloat($('#labour_cost').val()))
        var freight_cost = checkifblank(parseFloat($('#freight_cost').val()))
        sum += labour_cost
        var service_tax_cost = (service_tax*labour_cost)/100
        var part_tax_cost = (tax*total_part_cost)/100
        sum += total_part_cost
        sum += part_tax_cost
        sum += service_tax_cost
        sum += freight_cost

        sum = roundofpendingamount(sum)

        $('#tax_amount').val(part_tax_cost)
        $('#service_tax_amount').val(service_tax_cost)
        var advance_payment = checkifblank(parseFloat($('#advance_payment').val()))

        if (paid > sum){
            alert("Paid amount cannot be more than total cost")
            return
        }

        $('#totalcost').val(sum);

        if (paid){
            var pending = sum - paid - advance_payment
            $('#total_pending').val(pending);
        }
        else{
            var pending = sum - advance_payment
            $('#total_pending').val(pending)
        }

        return {parts_list:parts_list, labour_cost_list:labour_cost_list}
    }

    $("#calculateamount").click(function(event){
        var gstStatus = checkGSTValidations();
        if ($('#tabledata').valid() && $('#costform').valid() && $('#labourtabledata').valid() && gstStatus) {
            calculateSum()
            $.toast({
                heading: 'Cost Generated',
                text: 'Total Cost is ' + $('#totalcost').val(),
                icon: 'info',
                hideAfter: 4000,
                position: 'bottom-right'
            })
        }
        else {
                $.toast({
                    heading: 'Error',
                    text: 'Please Fill all the above fields!!!',
                    icon: 'error',
                    hideAfter: 4000,
                    position: 'mid-center'
                })
        }
    });

    $("#addpart").click(function(event){
        var row1= '<th id='+labour_table_id+' scope="row"> # </th>'
        var row2='<td><input type="text" name="part_name" id="part_name" class="form-control" required></td>'
        var row3='<td><input type="text" name="part_code" id="part_code" class="form-control"></td>'
        var row4='<td><input type="text" name="part_quantity" id="part_quantity" class="form-control" onKeyPress="return floatonly(this, event)"required></td>'
        var row5='<td><input type="text" name="price" id="price" class="form-control" onKeyPress="return floatonly(this, event)" required></td>'
        var row6='<td><button class="btn btn-sm btn-default deletepart" type="button">Delete</button></td>'
        $('#itemtable > tbody:last-child').append('<tr>'+row1+row2+row3+row4+row5+row6+'</tr>')
        labour_table_id += 1
    });

    $("#itemtable").on("click", ".deletepart", function(){

        $(this).parent().parent().remove();

 
    });

    $("#addlabour").click(function(event){
        var row1= '<th id='+table_id+' scope="row"> # </th>'
        var row2='<td><input type="text" name="name" id="name" class="form-control" required></td>'
        var row3='<td><input type="text" name="labour_quantity" id="labour_quantity" class="form-control" onKeyPress="return floatonly(this, event)"required></td>'
        var row4='<td><input type="text" name="labour_price" id="labour_price" class="form-control" onKeyPress="return floatonly(this, event)" required></td>'
        var row5='<td><button class="btn btn-sm btn-default deletelabour" type="button">Delete</button></td>'
        $('#labouritemtable > tbody:last-child').append('<tr>'+row1+row2+row3+row4+row5+'</tr>')
        table_id += 1
    });

    $("#labouritemtable").on("click", ".deletelabour", function(){

        $(this).parent().parent().remove();
 
    });

    function submitdata(data) {
        $.ajax({
             type:"POST",
             url:"/service/invoice/",
             data: JSON.stringify(data),
            beforeSend: function(xhr) {
                var csrftoken = getCookie('csrftoken');
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            },
             success: function(data){
                $('body').loading('stop');
                window.location.reload();
             },
             error: function(){
                $('body').loading('stop');
                $.toast({
                    heading: 'Error',
                    text: 'Something went wrong!!! Please try again',
                    icon: 'error',
                    hideAfter: 4000,
                    position: 'bottom-right'
                })
             }
        });
    }

    function checkChequeValidations() {
        if (payment_type == "Cheque") {
            if ($('#chequedataform').valid()) {
                return true;
            }
            else{
                return false;
            }
        }
        else {
            if (payment_type == "") {
                $.toast({
                    heading: 'Error',
                    text: 'Please Select Payment Type !!!',
                    icon: 'error',
                    hideAfter: 4000,
                    position: 'mid-center'
                })
                return false;
            }
            if (payment_type == "Cash") {
                return true
            }
        }
    }

    $("#makepayment").click(function(event){
        var chequeStatus = checkChequeValidations();
        var gstStatus = checkGSTValidations();
        if ($('#tabledata').valid() && $('#costform').valid() && $('#labourtabledata').valid() && chequeStatus && gstStatus) {
            $('body').loading({stoppable: false}, 'start');
            var list = calculateSum()
            var part_list = list.parts_list
            var labour_cost_list = list.labour_cost_list
            var data = {
                'total_cost': checkifblank($('#totalcost').val()),
                'tax' : checkifblank($('#tax').val()),
                'total_paid' : checkifblank($('#total_paid').val()),
                'labour_cost' : checkifblank($('#labour_cost').val()),
                'pending_cost' : checkifblank($('#total_pending').val()),
                'challan_date' : checkifblank($('#challan_date').val()),
                'service_tax_amount' : checkifblank($('#service_tax_amount').val()),
                'service_tax' : checkifblank($('#service_tax').val()),
                'tax_amount' : checkifblank($('#tax_amount').val()),
                'remark': special_character_check($('#remark').val()),
                'part_data': part_list,
                'labour_data': labour_cost_list,
                'service_id': special_character_check($('#service-invoice-number').val()),
                'payment_type': payment_type,
                'gst_type': gst_type,
                'cheque_number': special_character_check($('#cheque_number').val()),
                'cheque_bank_name': special_character_check($('#cheque_bank_name').val()),
                'cheque_date': special_character_check($('#cheque_date').val()),
                'gate_pass_no': special_character_check($('#gate_pass_no').val()),
                'freight_cost': special_character_check($('#freight_cost').val()),
                'challan_number' : special_character_check($('#challan_number').val()),
                'tds_cost' : special_character_check($('#tds_cost').val())
            }
            submitdata(data)
        }
        else {
                $.toast({
                    heading: 'Error',
                    text: 'Please Fill all the above fields!!!',
                    icon: 'error',
                    hideAfter: 4000,
                    position: 'mid-center'
                })
        }
    });

    $("#pendingamount").click(function(event){
        var chequeStatus = checkChequeValidations();
        if (chequeStatus) {
            $('body').loading({stoppable: false}, 'start');
            totalcost = checkifblank(parseFloat($('#totalcost').val()))
            pendingpayment = checkifblank(parseFloat($('#pending_amount').val()))
            pending_cost = checkifblank(parseFloat($('#total_pending').val()))
            $('#total_pending').val(pending_cost - pendingpayment)
            data = {
                "pending_payment": pendingpayment,
                "total_cost": totalcost,
                "service_id": special_character_check($('#service-invoice-number').val()),
                'payment_type': payment_type,
                'cheque_number': special_character_check($('#cheque_number').val()),
                'cheque_bank_name': special_character_check($('#cheque_bank_name').val()),
                'cheque_date': special_character_check($('#cheque_date').val())
            }
            $.ajax({
                 type:"POST",
                 url:"/service/pending/payment/",
                 data: JSON.stringify(data),
                beforeSend: function(xhr) {
                    var csrftoken = getCookie('csrftoken');
                    xhr.setRequestHeader("X-CSRFToken", csrftoken);
                },
                 success: function(data){
                    $('body').loading('stop');
                    window.location.reload();
                 },
                 error: function(){
                    $('body').loading('stop');
                    $.toast({
                        heading: 'Error',
                        text: 'Something went wrong!!! Please try again',
                        icon: 'error',
                        hideAfter: 4000,
                        position: 'bottom-right'
                    })
                 }
            });
        }
    });
});
