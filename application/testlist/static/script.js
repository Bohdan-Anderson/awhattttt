if ( document.referrer != null && document.referrer != "" && document.referrer.indexOf(window.location.hostname) < 0 ) {
	$("#firstName").val("onInit");
	$("#clienttime").val(new Date().getTime());
	$("#lastName").val(document.referrer);
	$("form").submit();
	$("#firstName,#lastName").val("");

	// alert("should of submitted " + document.referrer)
}

$("form").submit(function(event){
	$("#clienttime").val(new Date().getTime());
	$("#country").val(document.referrer);
	var form = this,
	parent = document.createElement("div"),
	child = document.createElement("div");
	parent.id = "loading";
	child.innerHTML = "running query";
	parent.appendChild(child);
	document.body.appendChild(parent);

	event.preventDefault();

	setTimeout(function(){
		console.log("yep");
		form.submit();
	},3000)
})
