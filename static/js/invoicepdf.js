$(document).ready(function() {
	$('#print_id').on('click', function() {
	    $("#demoprint").print({
	    	globalStyles: true,
	    	append: null,
            prepend: null,
            timeout: 250,
                title: null,
                doctype: '<!doctype html>'
	    });
	});
});
