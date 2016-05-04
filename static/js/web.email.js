$(document).ready(function() {
    var csrftoken = getCookie('csrftoken');

    $("#contactfooterform").submit(function(event){
        event.preventDefault();
        console.log($("#contactfooterform").serialize())
        var number = $('#contact-number').val();
        if (number) {
            $.ajax({
                 type:"POST",
                 url:"/save/contact/",
                 data: {"number":number},
        beforeSend: function(xhr) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        },
                 success: function(data){
                    $("#customerform").trigger('reset');
                    $.toast({
                        heading: 'Success',
                        text: 'Customer added successfully!!!  ',
                        icon: 'success',
                        hideAfter: 4000,
                        position: 'bottom-right'
                    })
                 },
                 error: function(){
                    $.toast({
                        heading: 'Error',
                        text: 'Something went wrong!!! Please try again',
                        icon: 'error',
                        hideAfter: 4000,
                        position: 'bottom-right'
                    })
                 }
            });
            return false; //<---- move it here
        }
   });
    $("#detailcontactform").submit(function(event){
        event.preventDefault();
        var number = $('#detailcontact-number').val();
        if (number) {
            $.ajax({
                 type:"POST",
                 url:"/save/contact/",
                 data: $("#detailcontactform").serialize(),
        beforeSend: function(xhr) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        },
                 success: function(data){
                    $("#customerform").trigger('reset');
                    $.toast({
                        heading: 'Success',
                        text: 'Customer added successfully!!!  ',
                        icon: 'success',
                        hideAfter: 4000,
                        position: 'bottom-right'
                    })
                 },
                 error: function(){
                    $.toast({
                        heading: 'Error',
                        text: 'Something went wrong!!! Please try again',
                        icon: 'error',
                        hideAfter: 4000,
                        position: 'bottom-right'
                    })
                 }
            });
            return false; //<---- move it here
        }
   });
});
