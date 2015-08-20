console.log("whatttt");

$("form").submit(function(event){
	$("#clienttime").val(new Date().getTime());
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