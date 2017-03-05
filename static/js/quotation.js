$(document).ready(function() {
    var csrftoken = getCookie('csrftoken');
    var table_id = 1
    var labour_table_id = 1

    function checkifblank(data) {
        if (data){
            return data
        }
        return 0
    }

    function special_character_check(data) {
        data = data.replace(/"/g, "'")
        data = encodeURIComponent(data)
        return data
    }

    function special_character_check_for_json(data) {
      response_data = {}
        $.each(data, function(k, v) {
          if (k != "k") {
              response_data[k] = special_character_check(v);
          }
        });
        return response_data
    }

    function calculateSum() {
        var tbl = $('#itemtable');
        var sum = 0;
        var parts_list = []

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
            $(this).find('#description').each(function () {
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

            sum += quantity * price

            $(this).find('.total').val(sum.toFixed(2));
        });

        var tax = checkifblank(parseFloat($('#tax').val()))
        var tax_cost = (tax*sum)/100
        sum += tax_cost
        $('#tax_amount').val(tax_cost);

        $('#totalcost').val(sum);

        return parts_list
    }

    $("#calculateamount").click(function(event){
        if ($('#tabledata').valid() && $('#costform').valid()) {
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
        var row3='<td><input type="text" name="description" id="description" class="form-control"></td>'
        var row4='<td><input type="text" name="part_quantity" id="part_quantity" class="form-control" onKeyPress="return floatonly(this, event)"required></td>'
        var row5='<td><input type="text" name="price" id="price" class="form-control" onKeyPress="return floatonly(this, event)" required></td>'
        var row6='<td><button class="btn btn-sm btn-default deletepart" type="button">Delete</button></td>'
        $('#itemtable > tbody:last-child').append('<tr>'+row1+row2+row3+row4+row5+row6+'</tr>')
        labour_table_id += 1
    });

    $("#itemtable").on("click", ".deletepart", function(){

        $(this).parent().parent().remove(); 
    });

    function submitdata(data) {
        $.ajax({
             type:"POST",
             url:"/quotation/generate/",
             data: JSON.stringify(data),
            beforeSend: function(xhr) {
                var csrftoken = getCookie('csrftoken');
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            },
             success: function(data){
                $('body').loading('stop');
                window.location = "/quotation/view/"+data+"/";
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

    (function( $ ){
        $.fn.serializeJSON=function() {
            var json = {};
            jQuery.map($(this).serializeArray(), function(n, i){
                json[n['name']] = n['value'];
            });
            return json;
        };
    })( jQuery );

    $("#makepayment").click(function(event){
    	event.preventDefault();
        if ($('#tabledata').valid() && $('#costform').valid() && $('#customerform').valid()) {
            $('body').loading({stoppable: false}, 'start');
            var list = calculateSum()
            var part_list = list
            var data = {
                'total_cost': checkifblank($('#totalcost').val()),
                'tax' : checkifblank($('#tax').val()),
                'tax_amount' : checkifblank($('#tax_amount').val()),
                "customer": special_character_check_for_json($('#customerform').serializeJSON()),
                'part_data': part_list
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
});
