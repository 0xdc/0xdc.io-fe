"use strict";

document.addEventListener("DOMContentLoaded", function(e){
	var generated_address = "website." + (Math.random() * 10 ** 16).toString(16) + "@" + window.location.host;
	var a = document.createElement("a");
	a.href = "mailto:" + generated_address;
	a.classList = ["email"];
	a.appendChild(document.createTextNode(generated_address));
	document.querySelector("#hcard-0xdc").appendChild(a);
})
