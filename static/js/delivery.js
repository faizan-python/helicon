$(document).ready(function() {
    var csrftoken = getCookie('csrftoken');

    $("#editDeliveryDetails").click(function(event) {
      event.preventDefault();
      $("#viewdeliveryform").hide();
      $("#editdeliveryform").show();
    });
});
