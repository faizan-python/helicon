$(document).ready(function() {
    var csrftoken = getCookie('csrftoken');

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

    $("#customerform").submit(function(event){
        event.preventDefault();
        $.ajax({
             type:"POST",
             url:"/customer/create/",
             data: $("#customerform").serialize(),
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
   });
});
