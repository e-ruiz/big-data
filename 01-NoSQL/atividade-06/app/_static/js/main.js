// Change the selector if needed
function _grid() {
	
	var $table = $('table.printable'),
    $bodyCells = $table.find('tbody tr:first').children(),
    colWidth;

	// Get the tbody columns width array
	colWidth = $bodyCells.map(function() {
	    return $(this).width();
	}).get();
	
	// Set the width of thead columns
	$table.find('thead tr').children().each(function(i, v) {
	    $(v).width(colWidth[i]);
	});    
}