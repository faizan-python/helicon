$(document).ready(function() {
	$('#print_id').on('click', function() {
	    $("#demoprint").print({
	    	append : "Free jQuery Plugins<br/>",
	    	prepend : "<br/>jQueryScript.net"
	    });
	});
});
