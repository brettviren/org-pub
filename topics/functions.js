$( document ).ready (function () {
    $("pre.src-sh").each(function () {
	var lines = $( this ).text().split('\n');
	for (var ind = 0 ; ind < lines.length ; ind++) {
            if ( ! lines[ind] ) {
		continue;
	    }
	    lines[ind] = '<span class="shell-line"></span>' + lines[ind];
	}
	$( this ).html(lines.join("\n"));
    });
});

